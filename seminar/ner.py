import re
import nltk
import getFileToTag
import wikification

tokens = getFileToTag.getTokens()
#used to filter out known capitals that may cause trouble
daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
title = ['Mr', 'Dr', 'Prof', 'Professor', 'Mrs', 'Miss', 'Ms']
numReg = '[0-9]+'
reg = '([!-/]*[[-`]*[{-}]*)' # I have no idea what this is for
locFile = "training_data/location.txt"
speakFile = "training_data/speakers.txt"

#tags any time - uses regex
def tagTime(word, index):
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

def tagLocation(word, index):
    theLocation = word
    location = word
    isLocation = True
    i = 1
    while isLocation :
        #keep iterating through until there is no longer a location
        nextWord = tokens[index+i]
        if (re.matches(numReg, nextWord)):
            theLocation = theLocation + ' ' + nextWord
            i = i + 1
        elif (checkFile(locFile, nextWord)):
            theLocation = theLocation + ' ' + nextWord
            i = i + 1
        elif (nextWord.toUpper == "ROOM"):
            theLocation = theLocation + ' ' + nextWord
            i = i + 1
        else:
            isLocation = False
    while (index+i) > index :
        tokens[index+i] = 'BAH'
        i = i - 1
    return " <location> " + theLocation + "</location>"
        
    
    
    
#check to see if a word already exists in a text file
def checkFile(word, file):
    with open(file) as f:
        if word in f.read() :
            return True
    return False

#calls wikification class
def wikify(word) :
    wikification.execute(word)
    return True

def checkForName(word):
    #add wikification into this
    isName = False
    if ((word in daysOfWeek) or (word in months)) :
        #filter out known words that will be passed through
        isName = False
    elif (checkFile(word, "res/names.male") or checkFile(word, "res/names.female") or checkFile(word, "res/names.family")):
        #word is in file of names
        isName = True
    elif (word in title) :
        #the word is a title - indicates a name will be coming
        isName = True
    elif (checkFile(word, speakFile)):
        #the word is a name in the data extracted from the original training set
        isName = True
    elif (wikify(word)) :
        #the name returns an entry that is a name when it is wikified 
        isName = True
    else :
        isName = False
    return isName

def checkForLocation(word):
    isLocation = False
    if (checkFile(word, locFile)):
        #the word is in data extracted from original training set
        isLocation = True
    elif (wikify(word)):
        isLocation = True
    else :
        isLocation = False
    return isLocation
