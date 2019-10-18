import morfeusz2, os, glob, re, emoji, json,sys, copy
morf =morfeusz2.Morfeusz(aggl="permissive", praet="composite")
e = emoji.get_emoji_regexp().pattern#re.compile("\s?([^:\s]+?)\s?(:[^\s]+:)")
emoji_pattern =re.compile(f"(\w+?)\s?((?:(?:\s*)?(?:{e})(?:\s*)?)+)")
dict = {}
dict_data_folder = "dict_data"
output_file = "dict.json"
for filename in glob.glob(f"{dict_data_folder}/*"):
    print(filename)
    dict_entry = {}
    with open(filename, encoding="utf-8") as data_file:
        content = data_file.read().replace(".", "").replace(",", "").replace(":","").replace("-","").replace("!","").replace("?","")
        for group in emoji_pattern.findall(content):
            word = group[0]
            if word in ['i', 'lub', 'też', "się", "sie"]: continue
            emojis = emoji.demojize(group[1])
            #warunki
            emojis_list =  list(dict.fromkeys([x for x in emojis.split(":") if len(x)>1 and 'keycap' not in x]))
          
            lemma = morf.analyse(word);
         
            for meaning in lemma:
                base_word = meaning[2][1]
                if "być" in base_word or base_word in ['i:i', 'i:q', 'i:j']: continue
                #print(base_word)
                #print(dict)
                if base_word in dict:
                    dict[base_word]["emoji_after"]+=copy.deepcopy(emojis_list)
                    dict[base_word]["emoji_after"]=list(dict.fromkeys( dict[base_word]["emoji_after"]))
                else:
                    dict_entry["emoji_after"] = emojis_list
                    dict[base_word] = copy.deepcopy(dict_entry)
with open(output_file, "w+", encoding="utf-8") as f:             
    json.dump(dict,f, ensure_ascii=False)
         
        