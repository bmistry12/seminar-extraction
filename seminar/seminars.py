import re
import ner
import nltk
from os import listdir
from os.path import isfile, join
from nltk.tokenize import sent_tokenize, word_tokenize

mypath = "seminars_training"
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#corpus_root = mypath
#corpus = nltk.corpus.reader.plaintext.PlaintextCorpusReader(corpus_root, onlyfiles)

#Load the text file to tag
corpus2 = nltk.data.load('seminars_training/8test.txt')
#corpus2 = nltk.data.load('seminars_untagged/301.txt')
print(corpus2) #print text just for purposes of checking

sents = sent_tokenize(corpus2)
#tokenise text
tokens = nltk.word_tokenize(corpus2)


def getTokens() :
    #get tokens - for other files
    return tokens

#list of regex used
timeReg = '([0-9]+(\s|:|pm|am){1}[0-9]*$)' #([0-9]+(\s|:|pm|am){1}[0-9]*(-)?[0-9]+(\s|:|pm|am){1}[0-9]*)
capitalReg = '(([A-Z]+[a-z]*)+)'

index = 0 #word index for for loop
newDoc = list();

#loops through text and if it needs to be tagged calls correct method to tag it
for word in tokens :
    if (word.upper() != 'AM' or word.upper() != 'PM'):
        if re.match(timeReg, word):
            newDoc.append(ner.tagTime(word, index))
            #print(ner.tagTime(word, index)) 
        elif re.match(capitalReg, word):
            newDoc.append(ner.capital(word, index))
            #print(ner.capital(word, index))
        else :
            newDoc.append(word)
            #print(word)
    index = index + 1

#newDocs is currently just a list of words
print (' ---------------------------------------------------------')
print (' |                TAGGED VERSION                         | ')
print (' ---------------------------------------------------------')
print(newDoc)

