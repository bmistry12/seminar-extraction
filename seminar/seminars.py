import re
import ner
import nltk
import pickle
import getFileToTag
from os import listdir
from os.path import isfile, join
from nltk.tokenize import sent_tokenize, word_tokenize

location = ''
sents = getFileToTag.getSentences()
tokens = getFileToTag.getTokens()
print("--------------tokens-------------")
print(tokens)
avoidWords = []
tagger = pickle.load(open( 'pos_tagger.pkl', 'rb' ) )
corpus = []
for word in tokens :
    corpus.append([word])
tagged_corpus = tagger.tag_sents(corpus)

print("pos tagging ")
print(tagged_corpus)
newCorpus = list()

#add POS tags into the corpus
for [word] in tagged_corpus:
    newCorpus.append(word)

def checkForNoneType(word):
    print(word)
    if (re.match('None{1}', str(word))):
        return True
    
def foundVB (word, index2):
    print(word)
    if (word.upper() == "PLACE"):
        print("location is coming up ")
        #index = Place, index+1 = : therefore first place of location = index +2
        print(tokens[index2+2])
        print(str(tokens[index2+2]))
        location = ner.tagLocation(tokens[index2+2], index2+2)
        return word + tokens[index2 + 1] + location
    else :
        return word
    
def foundNP(word, index2):
    print(word)
    name = "";
    #first check for names
    if (ner.checkForName(word))  :
        print("<speaker>" + word + "</speaker>")
        prevWord = newCorpus[index2-1]
        p1, p2 = prevWord
        nextWord = newCorpus[index2+1]
        n1, n2 = nextWord
        if (checkForNoneType(p2)):
            if(ner.checkForName(p1)):
                name = name + p1 + " "
                tokens[index2-1] = ""
        name = name + word + " "
        print(nextWord)
        if (checkForNoneType(str(n2))):
            if(ner.checkForName(n1)):
                name = name + n1 + " "   
                tokens[index2+1] = ""
        print("THE NAME ? " + name)
        name = "<speaker> " + name  + " </speaker>"
    else :
        name = word
    return name
        
    
#list of regex used
timeReg = '([0-9]+(\s|:|pm|am){1}[0-9]*$)' #([0-9]+(\s|:|pm|am){1}[0-9]*(-)?[0-9]+(\s|:|pm|am){1}[0-9]*)
capitalReg = '(([A-Z]+[a-z]*)+)'

index = 0 #word index tokens for loop
index2 = 0 #word index for tuple corpus
replace = ""

for tup in newCorpus :
    val , tag = tup
    if (re.match('VB{1}', str(tag))):
        replace = foundVB(val, index2)
        tokens[index2] = replace
    elif (re.match('NP{1}', str(tag))): #Finding all noun parts!
        print("Found NP")
        replace = foundNP(val, index2)
        print("replace with: " + replace)
        tokens[index2] = replace
    else :
        if (re.match(timeReg, val)):
            print("Found time")
            replace = ner.tagTime(val, index2)
            print("replace with: " + replace)
            tokens[index2] = replace
    index2 = index2 + 1


#then go through once we reassemble and replace other occurances of said location
print("_______________________")
print (tokens)
print("_______________________")
newDocument = ' '.join(tokens)
a = ''.join(newDocument)

getFileToTag.outputNewFile(a)



