import re
import ner
import nltk
import pickle
import getFileToTag
from os import listdir
from os.path import isfile, join
from nltk.tokenize import sent_tokenize, word_tokenize

location = ''
tokens = getFileToTag.getTokens()
print("--------------tokens-------------")
print(tokens)
avoidWords = []
tagger = pickle.load(open( 'pos_tagger.pkl', 'rb' ) )
corpus = []
for word in tokens :
    corpus.append([word])
tagged_corpus = tagger.tag_sents(corpus)

newCorpus = list()

#add POS tags into the corpus
for [word] in tagged_corpus:
    newCorpus.append(word)

def checkForNoneType(word):
    if (re.match('None{1}', str(word))):
        return True
    
def foundVB (word, index2):
    #print(word)
    if (word.upper() == "PLACE" or word.lower() == "location" or word.lower() == "where"):
        #index = Place, index+1 = : therefore first place of location = index +2
        location = ner.tagLocation(tokens[index2+2], index2+2)
        return word + tokens[index2 + 1] + location
    else :
        return word

def nameCheck(word, index2):
    name = "";
    #first check for names
    if (ner.checkForName(word))  :
        twoBack = newCorpus[index2-2]
        t1, t2 = twoBack
        if (t1.upper() != "HOST") :
            prevWord = newCorpus[index2-1]
            p1, p2 = prevWord
            nextWord = newCorpus[index2+1]
            n1, n2 = nextWord
            if (checkForNoneType(p2)):
                if(ner.checkForName(p1)):
                    name = name + p1 + " "
                    tokens[index2-1] = ""
            name = name + word + " "
            if (checkForNoneType(str(n2))):
                if(ner.checkForName(n1)):
                    name = name + n1 + " "   
                    tokens[index2+1] = ""
            name = "<speaker>" + name  + "</speaker>"
        else :
            name = word
    return name
        
    
#list of regex used
timeReg = '([0-9]+(\s|:|pm|am){1}[0-9]*$)'
capitalReg = '(([A-Z]+[a-z]*)+)'

index = 0 #word index tokens for loop
index2 = 0 #word index for tuple corpus
replace = ""

for tup in newCorpus :
    val , tag = tup
    if (val.upper() == "WHO") :
        nextTup = newCorpus[index2 + 2]
        val2, tag2 = nextTup
        replace = nameCheck(val2, index2+2)
        tokens[index2+2] = replace
    elif (re.match('VB{1}', str(tag)) or val.lower() == "location" or val.lower() == "where"):
        replace = foundVB(val, index2)
        tokens[index2] = replace
    elif (re.match('NP{1}', str(tag))): #Finding all noun parts!
        replace = nameCheck(val, index2)
        tokens[index2] = replace
    elif (val in location) :
        pass
    else :
        if (re.match(timeReg, val)):
            replace = ner.tagTime(val, index2)
            tokens[index2] = replace
    index2 = index2 + 1


#then go through once we reassemble and replace other occurances of said location
print("_______________________")
print (tokens)
print("_______________________")
newDocument = ' '.join(tokens)
a = ''.join(newDocument)

#output new file
getFileToTag.outputNewFile(a)



