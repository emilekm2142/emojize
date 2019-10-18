import emoji, random, morfeusz2, json
morf = morfeusz2.Morfeusz(aggl="permissive", praet="composite")
dictionary = None
with open("dict.json", 'r', encoding="utf-8") as f:
    dictionary = json.load(f)
#print(dictionary)
def get_random_emoji(l)->str:
    try:
        return emoji.emojize(":"+random.choice(l)+":")
    except:
        return ""
def translate(text:str)->str:
    out_str = ""
    current_token_index = 0
    a=morf.analyse(text)
    print(a)
    for i,token in enumerate(a):
        if current_token_index>token[0]: continue
        #search for all lemmas:
        current_lemmas=[x[2][1] for x in a if x[0]==current_token_index]
        #print(current_lemmas)
        current_token_index+=1
        current_token = token[2][0]
        constrained_words = ["ten", "ów", "że:c"]
        max_number=5
        for w in constrained_words:
            if w in current_lemmas:
                max_number=1
                break
        amount = random.randint(1,5)
        emojis = [] 
        errors = 0
        while len(emojis)<amount and len(current_lemmas)>0:
            random_lemma = current_lemmas[0]
            
            try:
                emojis+=[get_random_emoji(dictionary[random_lemma]["emoji_after"])]
            except KeyError:
                errors+=1
                current_lemmas.remove(random_lemma)
        print(current_token)
        out_str+=current_token.replace(" ","")+" "+"".join(emojis)+(" " if len(emojis)>0 else "")
    return out_str

  