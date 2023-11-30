import re
import pronouncing
import random
import requests
from bs4 import BeautifulSoup
import os
import nltk
from nltk.corpus import cmudict

choice = input("""
Input 1 to generate words that rhyme:
Input 2 to generate a song:
""")

if choice == "2":
    
    def rhyme(inp, level):
        entries = nltk.corpus.cmudict.entries()
        syllables = [(word, syl) for word, syl in entries if word == inp]
        rhymes = []
        for (word, syllable) in syllables:
                rhymes += [word for word, pron in entries if pron[-level:] == syllable[-level:]]
        return set(rhymes)

    def doTheyRhyme(word1, word2):
        if word1.find(word2) == len(word1) - len(word2):
            return False
        if word2.find(word1) == len(word2) - len(word1): 
            return False

        return word1 in rhyme(word2, 1)

    alphabets= "([A-Za-z])"
    prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
    suffixes = "(Inc|Ltd|Jr|Sr|Co)"
    starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
    acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
    websites = "[.](com|net|org|io|gov)"
    digits = "([0-9])"

    #write function that scrapes songs off google. 

    def split_into_sentences_loop(text, x):
        text = " " + text + "  "
        text = text.replace("\n"," ")
        text = re.sub(prefixes,"\\1<prd>",text)
        text = re.sub(websites,"<prd>\\1",text)
        text = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
        if "..." in text: text = text.replace("...","<prd><prd><prd>")
        if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
        text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
        text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
        text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
        text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
        text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
        text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
        text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
        if "”" in text: text = text.replace(".”","”.")
        if "\"" in text: text = text.replace(".\"","\".")
        if "!" in text: text = text.replace("!\"","\"!")
        if "?" in text: text = text.replace("?\"","\"?")
        text = text.replace(".",".<stop>")
        text = text.replace("?","?<stop>")
        text = text.replace("!","!<stop>")
        text = text.replace("<prd>",".")
        sentences = text.split("<stop>")
        sentences = sentences[:-1]
        sentences = [s.strip() for s in sentences]
        return sentences[x]

    def split_into_sentences(text):
        text = " " + text + "  "
        text = text.replace("\n"," ")
        text = re.sub(prefixes,"\\1<prd>",text)
        text = re.sub(websites,"<prd>\\1",text)
        text = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
        if "..." in text: text = text.replace("...","<prd><prd><prd>")
        if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
        text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
        text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
        text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
        text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
        text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
        text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
        text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
        if "”" in text: text = text.replace(".”","”.")
        if "\"" in text: text = text.replace(".\"","\".")
        if "!" in text: text = text.replace("!\"","\"!")
        if "?" in text: text = text.replace("?\"","\"?")
        text = text.replace(".",".<stop>")
        text = text.replace("?","?<stop>")
        text = text.replace("!","!<stop>")
        text = text.replace(",",",<stop>")
        text = text.replace(";",";<stop>")
        text = text.replace("<prd>",".")
        sentences = text.split("<stop>")
        sentences = sentences[:-1]
        sentences = [s.strip() for s in sentences]
        return sentences
    


    def scrapelyrics(songname):
        songname.split()
        newsongname = ""
        for i in range(len(songname)):
            newsongname = newsongname+songname[i]+"+"
        URL = "https://search.azlyrics.com/search.php?q" + newsongname  + "&x=98ea1fff545c613ec9f69b0209651a09e335b485f475199f909aea3e5228405a"


    songs = []
    sentenceofsongs = []
    numofsongs = int(input("Enter the Number of songs you would like to put in: "))

    for i in range(numofsongs):
        songs.append(input("Enter the song: "))

    for i in range(numofsongs):
        temp = len(split_into_sentences(songs[i]))
        for x in range(temp):
            sentenceofsongs.append(split_into_sentences_loop(songs[i]))


    for i in range(len(sentenceofsongs)):
        print("sentence " + str(i+1) + " :" + sentenceofsongs[i] + "\n")

    def lastWord(string):
    
        newstring = ""
        
        length = len(string)
        
        for i in range(length-1, 0, -1):
        
            if(string[i] == " "):
            
                return newstring[::-1]
            else:
                newstring = newstring + string[i]

    thelastword = []

    for i in range(len(sentenceofsongs)):
        tmpvar = lastWord(sentenceofsongs[i])
        tmpvar = tmpvar[:-1]
        thelastword.append(tmpvar)

    print(sentenceofsongs)
    print(thelastword)

    newsong = []

    for i in range(len(sentenceofsongs)):
        col = []
        col.append(sentenceofsongs[i])
        for x in range(len(sentenceofsongs)):
            ifrhyme = doTheyRhyme(thelastword[i], thelastword[x])
            if i != x:
                if ifrhyme == True:
                    col.append(sentenceofsongs[x])
        newsong.append(col)


    if newsong[0] is not None:
        for i in range(len(newsong[0])):
            print(newsong[0][i]+"\n")
    else:
        print("song not found")


#https://openai.com/blog/jukebox/

elif choice == "1":
    rhymeword = input("enter a word to rhyme with:")
    wtr = pronouncing.rhymes(rhymeword)
    print("Words that thyme with "+rhymeword+" :")
    for i in range(len(wtr)):
        print(wtr[i] + "  ")

