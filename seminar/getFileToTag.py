import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

'''
This file is used to get the file to be tagged
Will be editted so that a user can choose a file to tag
'''

mypath = "seminars_training/8test.txt"

#Load the text file to tag
corpus2 = nltk.data.load(mypath)
print(corpus2) #print text just for purposes of checking

#tokenise text
tokens = nltk.word_tokenize(corpus2)
#sents = sent_tokenize(corpus2)

#get tokens - for other files
def getTokens() :
    return tokens
