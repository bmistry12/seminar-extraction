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

#Load the text file to tag
corpus2 = nltk.data.load(mypath)
print(corpus2) #print text just for purposes of checking
taggedPath = "seminar_test_data/test_tagged/" + userFile + ".txt"
file = nltk.data.load(taggedPath)
#tokenise text
#tokens = nltk.word_tokenize(corpus2)
sents = sent_tokenize(corpus2)


pos = 0
def tagParagraphs():
    '''
    splits corpus into header (based on abstract so not going to work with everything_
    and body      -- used for sentence and paragraph tagging
    '''
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
    return tokens2

tokens = tagParagraphs()

def getSentences():
    return sents

#get tokens - for other files
def getTokens() :
    return tokens

'''
abstractReg = '[Aa]bstract\:\s*'
sentences = list()

def tagSentences():
    sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    text = nltk.data.load('seminars_training/8test.txt')
    newSents = sent_tokenizer.tokenize(text)
    for line in newSents :
        if (re.match(abstractReg, line)) :
            print("FOUND ABSTRACT")
        #sentences.append(line)
        #if(re.match(header1, line) or re.match(header2, line)):
        print(line)

############
def doStuffWithData():
    with open("seminars_training/8test.txt", "r") as file :
        corpus = file.read()
        print(sentances)
        #theLines = corpus.split("\n")
        print(corpus)
        paragraphs = []
        paragraphs = corpus.split("\n\n")
        print("----paragraphs------")
        print(paragraphs)
        for paragraph in paragraphs :
            paragraph= re.sub("\n\n", "<paragraph> " + paragraph + " </paragraph>", paragraph)
        
'''
def tagNextFile():
    textFileID = textFileID + 1

def split() :
    pass
'''
        abstractReg = '[Aa]bstract\:\s'
        for line in lines :
            if (re.match(abstractReg, line)):
                print("WE FOUND ABSTRACT")
                pos = index
            else :
                index = index + 1
        header = "".join(lines[:pos])
        abstractWord = "".join(lines[pos])
        body = "".join(lines[pos+1:])
        
        sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
        #paragraphs_sentences = list(map(sent_tokenizer.tokenize, paragraphs))
'''        

def outputNewFile(contents):
    newPath = "my_seminars_tagged/" + userFile + ".txt"
    print("New tagged version being saved to " + newPath)
    f = open(newPath, "w+")
    f.write(contents)
    f.close()

def main():
    tagNextFile()
    path = "seminar_test_data/test_untagged/" + textFileId + ".txt"
    corpus2 = nltk.data.load(mypath)
    print(corpus2) #print text just for purposes of checking

    #tokenise text
    tokens = nltk.word_tokenize(corpus2)
    sents = sent_tokenize(corpus2)
    print ("--------------------------------")
    print ("|        Tagged Version         |")
    print ("--------------------------------")
    filePath = "seminar_test_data/test_tagged/" + textFileID + ".txt"
    file = nltk.data.load(filePath)
    print (file)                          
