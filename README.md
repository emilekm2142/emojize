# emojize
Appends emoji to a text in polish language.
## Example
Changes

Zabierz swój długopis na spacer
Pokaż mu sklepy papiernicze
Niech wie jakie ma szczęście
Że trafił w twoje ręce
Bo do sklepu  zaraz wpadnie
Zaśliniony tłusty dzieciak
Cukiernia dziś zamknięta
A zjadł już wszystko ze swego piórnika

into:


Zabierz✊ swój 😊👈długopis🖊️ na spacer🏡🏞️🚶🏻‍♀
Pokaż 👀 mu sklepy🏪 papiernicze📜📃📄📰
Niech wie🤠☝️jakie ma 🤲 szczęście 🤱🎉🎰
Że trafił 🎯🎯w twoje😯👈 ręce🖐️🖐️
Bo do sklepu 🏪 zaraz🔜 wpadnie🕳️🏃🏻‍♀🤰
Zaśliniony🤤🤤 tłusty 🍔🍟dzieciak👦
Cukiernia🏪🍨🍰🍦 dziś📆 zamknięta🙅🏻‍♀❌
A zjadł 😋😋 już wszystko💯💯 ze swego piórnika👝

## How to run
You need to install polish nlp tool - morfeusz2 
http://morfeusz.sgjp.pl
```
wget -O - http://download.sgjp.pl/apt/sgjp.gpg.key|sudo apt-key add -

sudo apt-add-repository http://download.sgjp.pl/apt/ubuntu

sudo apt update
```
`sudo apt install morfeusz2`
`sudo apt install python3-morfeusz2`
`sudo pip3 install -r requirements.txt`
`flask run`
or run using gunicorn
