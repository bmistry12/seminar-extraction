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
mypath = "../seminar_test_data/test_untagged/" + userFile + ".txt"  
#regex for headers
header1 = '<[0-9].+([a-z]{2}[0-9]{2})[+]{1}[@]{1}[A-z].*[0-9]{1}>'
header2 = '<[0-9].+[a-z]{3}[+]{1}[@]{1}[A-z].*[0-9]{1}>'
header = '<([0-9]+.)*[A-z]*\+?\@?([1-z]*.)*>'
#Load the text file to tag
corpus2 = nltk.data.load(mypath)
print(corpus2) #print text just for purposes of checking
taggedPath = "seminar_test_data/test_tagged/" + userFile + ".txt"
file = nltk.data.load(taggedPath)

def tagSentsandParas():
    '''
    splits corpus into header and body
    as it is split based on the word Abstract it won't work for all emails
    used for sentence and paragraph tagging
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
        #tokenize corpus into sentences
        sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
        newSents = sent_tokenizer.tokenize(corpus)
        for line in newSents :
            #if we havent yet found abstract and the line contains abstract, we have found abstract! 
            if (not foundAbstract and re.search(abstractReg, line) != None) :
                abstract = line
                foundAbstract = True
            else :
                #as we are using a sentence tokenizer we simply need to wrap each line with the tags
                restOfText = restOfText + "<sentence>" + line + "</sentence>"
        #split new corpus into paragraphs
        paragraphs = restOfText.split("\n\n")
        i = 0
        for para in paragraphs :
            #filter out any paragraphs that contain Where: etc. as they are not paragraphs according to tagged data
            if (re.search(typeReg, para) == None) :
                paragraphs[i] = ("<paragraph>" + para + "</paragraph>")
            i = i + 1
        #rejoin the new tagged body with the header (abstract) and then word tokenize it
        newCorpus2 = abstract + '\n'.join(paragraphs)
        tokens2 = nltk.word_tokenize(newCorpus2)
    return tokens2

tokens = tagSentsandParas()

#get tokens - for other files
def getTokens() :
    return tokens

def outputNewFile(contents):
    newPath = "../my_seminars_tagged/" + userFile + ".txt"
    print("New tagged version being saved to " + newPath)
    f = open(newPath, "w+")
    f.write(contents)
    f.close()
                 
