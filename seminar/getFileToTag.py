import re
import sys
import nltk
import nltk.data
from nltk.tokenize import sent_tokenize, word_tokenize

'''
This file is used to get the file to be tagged
It also deals with the tagging of sentences and paragraphs
And outputs newly tagged file to a new text file
'''
textFileID = 300
tokens = ""
sents = ""
mypath = ""
print("Enter the number of the file you would like to tag : ");
userFile = input()
mypath = "seminar_test_data/test_untagged/" + userFile + ".txt"  
#regex for headers
header1 = '<[0-9].+([a-z]{2}[0-9]{2})[+]{1}[@]{1}[A-z].*[0-9]{1}>'
header2 = '<[0-9].+[a-z]{3}[+]{1}[@]{1}[A-z].*[0-9]{1}>'
header = '<([0-9]+.)*[A-z]*\+?\@?([1-z]*.)*>'
#Load the text file to tag
corpus2 = nltk.data.load(mypath)
print(corpus2) #print text just for purposes of checking
taggedPath = "seminar_test_data/test_tagged/" + userFile + ".txt"
file = nltk.data.load(taggedPath)


pos = 0
def tagSentsandParas():
    '''
    splits corpus into header (based on abstract so not going to work with everything_
    and body      -- used for sentence and paragraph tagging
    '''
    typeReg = '[A-z]+:'
    taggedDoc = ""
    index = 0
    abstract = ""
    restOfText = ""
    foundAbstract = False
    with open(mypath, "r") as file :
        corpus = file.read()
        abstractReg = '[Aa]bstract\:\s*'
        sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
        newSents = sent_tokenizer.tokenize(corpus)
        for line in newSents :
            if (not foundAbstract and re.search(abstractReg, line) != None) :
                abstract = line
                foundAbstract = True
            else :
                restOfText = restOfText + "<sentence>" + line + "</sentence>"

        paragraphs = restOfText.split("\n\n")
        i = 0
        for para in paragraphs :
            if (re.search(typeReg, para) == None) :
                paragraphs[i] = ("<paragraph>" + para + "</paragraph>")
            i = i + 1

        newCorpus2 = abstract + '\n'.join(paragraphs)
        tokens2 = nltk.word_tokenize(newCorpus2)
    return tokens2

tokens = tagSentsandParas()

#get tokens - for other files
def getTokens() :
    return tokens

def tagNextFile():
    textFileID = textFileID + 1

def outputNewFile(contents):
    newPath = "my_seminars_tagged/" + userFile + ".txt"
    print("New tagged version being saved to " + newPath)
    f = open(newPath, "w+")
    f.write(contents)
    f.close()
                 
