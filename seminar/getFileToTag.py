import re
import sys
import nltk
import nltk.data
from nltk.tokenize import sent_tokenize, word_tokenize

'''
This file is used to get the file to be tagged
Will be editted so that a user can choose a file to tag
'''
mypath = ""
print("Enter the number of the file you would like to tag : ");
userFile = input()
mypath = "seminars_training/" + userFile + ".txt"  

#textFileID = 300
#automatedpath "seminars_training/" + textFileId + ".txt"

print("b : " + mypath)
#Load the text file to tag
corpus2 = nltk.data.load(mypath)
print(corpus2) #print text just for purposes of checking

#tokenise text
tokens = nltk.word_tokenize(corpus2)
sents = sent_tokenize(corpus2)

def getSentences():
    return sents

#get tokens - for other files
def getTokens() :
    return tokens

############
abstractReg = re.compile("[Aa]bstract\:\s*")
def doStuffWithData():
    with open("seminars_training/8test.txt", "r") as file :
        corpus = file.read()
        #theLines = corpus.split("\n")
        print(corpus)
        paragraphs = []
        paragraphs = corpus.split("\n\n")
        print("----paragraphs------")
        print(paragraphs)
        for paragraph in paragraphs :
            paragraph= re.sub("\n\n", "<paragraph> " + paragraph + " </paragraph>", paragraph)
        

def tagNextFile():
    pass
    

def outputNewFile():
    newPath = "my_seminars_tagged/"
