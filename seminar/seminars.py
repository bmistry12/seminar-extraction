import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import re
import posTagger
import ner
from os import listdir
from os.path import isfile, join
mypath = "seminars_training"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
corpus_root = mypath
corpus = nltk.corpus.reader.plaintext.PlaintextCorpusReader(corpus_root, onlyfiles)
print(corpus.words())

#Load the text file to tag
corpus2 = nltk.data.load('seminars_training/8test.txt')
#corpus2 = nltk.data.load('seminars_untagged/301.txt')
print(corpus2) #print text just for purposes of checking

sents = sent_tokenize(corpus2)
print(sents)
print ("-----------^sents^---------------------")
#tokenise text
tokens = nltk.word_tokenize(corpus2)

def getTokens() :
    return tokens

#list of regex used
timeReg2 = '([0-9]+(\s|:|pm|am){1}[0-9]*$)'
timeReg = '([0-9]+(\s|:|pm|am){1}[0-9]*(-)?[0-9]+(\s|:|pm|am){1}[0-9]*)'
#capitalReg = '(([A-Z]{1}[a-z]+\s*)+)'
capitalReg = '(([A-Z]+[a-z]*)+)'

#word index for for loop
index = 0
newDoc = list();

#loops through text and if it needs to be tagged calls correct method to tag it
for word in tokens :
    if (word.upper() != 'AM' or word.upper() != 'PM'):
        if re.match(timeReg, word):
            newDoc.append(posTagger.tagTime(word, index))
            print(posTagger.tagTime(word, index))
        elif re.match(capitalReg, word):
            #newDoc.append(ner.capital(word, index))
            print(ner.capital(word, index))
        else :
            #newDoc.append(word)
            print(word)
    index = index + 1

#newDocs is currently just a list of words
#print(newDoc)

'''
def tagParagraphs(sents) :
    for p in sents:
        for s in p: 
            p[p.index(s)] = "<sentence>" + s + "</sentence>"
        paragraphs_sentences[paragraphs_sentences.index(p)] = "<paragraph>" + p + "</paragraph>"

    lines = paragraphs_sentences
    return lines
tagParagraphs(sents)
'''
