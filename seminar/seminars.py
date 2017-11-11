import re
import ner
import nltk
import getFileToTag
from os import listdir
from os.path import isfile, join
from nltk.tokenize import sent_tokenize, word_tokenize

tokens = getFileToTag.getTokens()
avoidWords = []

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
    
#list of regex used
timeReg = '([0-9]+(\s|:|pm|am){1}[0-9]*$)' #([0-9]+(\s|:|pm|am){1}[0-9]*(-)?[0-9]+(\s|:|pm|am){1}[0-9]*)
capitalReg = '(([A-Z]+[a-z]*)+)'

index = 0 #word index for for loop
newDoc = list()

#loops through text and if it needs to be tagged calls correct method to tag it
for word in tokens :
    if (word.upper() == 'AM' or word.upper() == 'PM'):
        avoidWords.append(word)
    else :
        if re.match(timeReg, word):
            #matches to a time
            newDoc.append(ner.tagTime(word, index))
        #elif (word == "SPEAKER"):
        #    newDoc.append(ner.tagSpeaker(word, index, 2))
        elif re.match(capitalReg, word):
            #matches to a capital
            newDoc.append(ner.capital(word, index))
        else :
            newDoc.append(word)
    index = index + 1
    
print("----------------------")
printStuff()




