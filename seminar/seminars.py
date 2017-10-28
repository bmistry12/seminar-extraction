import nltk
import re
from os import listdir
from os.path import isfile, join
mypath = "seminars_training"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
corpus_root = mypath
corpus = nltk.corpus.reader.plaintext.PlaintextCorpusReader(corpus_root, onlyfiles)
print(corpus.words())

#Load the text file to tag
corpus2 = nltk.data.load('seminars_training/258.txt')
#corpus2 = nltk.data.load('seminars_untagged/301.txt')
print(corpus2) #print text just for purposes of checking

#tokenise text
tokens = nltk.word_tokenize(corpus2)

#list of regex used
timeReg = '([0-9]+(\s|:|pm|am){1}[0-9]*$)'

#word index for for loop
index = 0

#tags any times correctly
def tagTime(word , index):
    printWord = " "
    nextWord = tokens[index+1].upper()
    prevWord = tokens[index-1]
    if (prevWord == '-') :
        if (nextWord == 'AM' or nextWord == 'PM') :
            printWord = '<etime>' + word + nextWord + '</etime>'
        else :
            printWord = '<etime>' + word + '</etime>'
    elif(nextWord == 'AM' or nextWord == 'PM') :
        printWord = ('<stime>' + word + nextWord + '</stime>')
    else :
        printWord = '<stime>' + word + '</stime>'
    return printWord

#loops through text and if it needs to be tagged calls correct method to tag it
for word in tokens :
    if (word.upper() != 'AM' or word.upper() != 'PM'):
        if re.match(timeReg, word):
            print(tagTime(word, index))
        else :
            print(word)
    index = index + 1
