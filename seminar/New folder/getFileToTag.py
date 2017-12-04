import re
import sys
import nltk
import nltk.data
from nltk.tokenize import sent_tokenize, word_tokenize

'''
This file is used to get the file to be tagged
Will be editted so that a user can choose a file to tag
It also deals with the tagging of sentences and paragraphs
'''
textFileID = 301
pos = 0
tokens = []
sents = []

def tagParagraphs(mypath):
    typeReg = '[A-z]+:'
    taggedDoc = ""
    index = 0
    with open(mypath, "r") as file :
        corpus = file.read()
        paragraphs = corpus.split("\n\n")
        i = 0
        for para in paragraphs :
            if (re.search(typeReg, para) == None) :
                paragraphs[i] = ("<paragraph> " + para + " </paragraph>")
            i = i + 1
        newCorpus = '\n'.join(paragraphs)
        tokens2 = nltk.word_tokenize(newCorpus)
    tokens = tokens2
    return tokens2

def getCurrentTextFileID():
    return textFileID

def getSentences():
    return sents

#get tokens - for other files
def getTokens() :
    return tokens

def tagNextFile():
    textFileID = getCurrentTextFileID() + 1
    loadNext(textFileID)

def split() :
    pass

def setTokens(tokens2):
    tokens = tokens2
    
def outputNewFile(contents):
    newPath = "my_seminars_tagged/" + str(getCurrentTextFileID()) + ".txt"
    print("New tagged version being saved to " + newPath)
    f = open(newPath, "w+")
    f.write(contents)
    f.close()

def loadNext(textFileID):
    path = "seminar_test_data/test_untagged/" + str(textFileID) + ".txt"
    corpus = nltk.data.load(path)
    sents = sent_tokenize(corpus)
    #tokenise text
    tokens = tagParagraphs(path)
    setTokens(tokens)
    #print(tokens)

