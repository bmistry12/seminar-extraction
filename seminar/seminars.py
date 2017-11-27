import re
import ner
import nltk
import pickle
import getFileToTag
from os import listdir
from os.path import isfile, join
from nltk.tokenize import sent_tokenize, word_tokenize

sents = getFileToTag.getSentences()
tokens = getFileToTag.getTokens()
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

def printStuff():
    print (' ----------------------------------------------------------')
    print (' |                TAGGED VERSION                           |')
    print (' ----------------------------------------------------------')
    #load in tagged version
    corpus3 = nltk.data.load('seminars_training/8.txt')
    print(nltk.word_tokenize(corpus3))
    #newDocs is currently just a list of words
    print (' ---------------------------------------------------------')
    print (' |               MY TAGGED VERSION                        |')
    print (' ---------------------------------------------------------')
    print(newDoc)
    
def checkForNoneType(word, index):
    if (re.match('NONE{1}', word)):
        return True
        
def foundNP(word, index2):
    name = "";
    if (ner.checkForName(word))  :
        prevWord = newCorpus[index2-1]
        nextWord = newCorpus[index2+1]
        if (checkForNoneType(prevWord)):
            if(ner.checkForName(prevWord)):
                name = name + prevWord + " "
                tokens[index2-1] = "BAH"
        name = name + word + " "
        if (checkForNoneType(nextWord)):
            if(ner.checkForName(nextWord)):
                name = name + nextWord + " "   
                tokens[index2+1] = "BAH"
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
newDoc = list()
replace = ""

for tup in newCorpus :
    val , tag = tup
    if (re.match('NP{1}', str(tag))): #Finding all noun parts!
        print("Found NP")
        replace = foundNP(val, index2)
        print("replace with: " + replace)
        tokens[index2] = replace
    index2 = index2 + 1

print("_______________________")
print (tokens)
'''
#loops through text and if it needs to be tagged calls correct method to tag it
for word in tokens :
    if (word.upper() == 'AM' or word.upper() == 'PM'):
        avoidWords.append(word)
    else :
        if re.match(timeReg, word):
            #matches to a time
            newDoc.append(ner.tagTime(word, index))
        elif (word == "SPEAKER"):
            newDoc.append(ner.tagSpeaker(word, index, 2))
        elif re.match(capitalReg, word):
            #matches to a capital
            newDoc.append(ner.capital(word, index))
        else :
            newDoc.append(word)
    index = index + 1
   
print("----------------------")
printStuff()
'''



