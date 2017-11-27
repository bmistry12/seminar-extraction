import re
import nltk
import getFileToTag

tokens = getFileToTag.getTokens()
#used to filter out known capitals that may cause trouble
daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
regexHERE = '([!-/]*[[-`]*[{-}]*)'
locFile = "location.txt"
speakFile = "speakers.txt"

#tags any times correctly
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

'''
---------------------
|      TO DO        |
---------------------
doesnt consider cases like
12:00pm-1:00pm
'''

#check to see if a word already exists in the training data text file
def checkFile(word, file):
    with open(file) as f:
        if word in f.read() :
            return True
    return False
'''
Doesn't work how it needs to -
need to get it to check against first words of each line only
'''

#tag speakers - currently only tags speakers who exist in training data
def tagSpeaker (word, index, i):
    isName = True
    join = tokens[index+i]
    toPrint = ' '
    while isName :
        if re.match(regexHERE, tokens[index+i]) :
            toPrint = join
            isName = False
        else :
            join = join + ' ' + tokens[index+i]
            print("JOIN : " + join)
            i = i + 1        
    return word + ' ' + tokens[index+1] + ' ' + "<speaker> " + toPrint + "</speaker>"

#tag locations - currently only those that exists in training data 
def tagLocation (word,tokens, index) :
    theLocation = word
    jointWord = word
    i = 1
    isLocation = True
    while isLocation :
        #keep iterating through until we get a phrase which is not a known location
        jointWord = jointWord + ' ' + tokens[index+i]
        if checkFile(jointWord, locFile) :
            #avoidWords.append(tokens[index+i])
            theLocation = theLocation + ' ' + tokens[index+i]
            i = i + 1
        else :
            isLocation = False
            while (index+i) > index+1 :
                #act of removing words which have now been tagged from original corpus
                tokens[index+i] = "VOID"
                i = i - 1
            #if tokens[index+i] in theLocation:
             #   avoidWords.append(tokens[index+i])
            if theLocation == word :
                return theLocation
    return "<location> " + theLocation + " </location>"
'''
I'm currently using void to represent removed words - this is because in some cases
the entry being removed shouldn't be being removed - e.g. '('
'''

def capital(word, index) :
    if ((word in daysOfWeek) or (word in months)) : #filter out known capitals
        return word
    else :
        word2 = tokens[index+1]
        word3 = tokens[index+2]
        join2 = word + ' ' + word2
        join3 = join2 + ' ' + word3
        #checking for known names of length 3 (e.g. dr __ ___ )
        if (checkFile(join3, speakFile)):
            tokens[index+1] = "VOID"
            tokens[index+2] = "VOID"
            return "<speaker> " + join3 + "</speaker>"
        #check for known names of length 2 (e.g ___ ____ )
        elif (checkFile(join2, speakFile)):
            tokens[index+1] = "VOID"
            return "<speaker> " + join2 + "</speaker>"
        elif (checkFile(word, locFile)) :
            return (tagLocation(word, tokens, index))
        else :
            return word

'''
There may be occassions where names have a greater length than 3
TO DO - Implement a similar method to the location checking for name
'''

def checkForName(name):
    #add wikification into this
    isName = False
    title = ['Mr', 'Dr', 'Prof', 'Professor', 'Mrs', 'Miss', 'Ms']
    if (checkFile(name, "names.male") or checkFile(name, "names.female") or checkFile(name, "names.family")):
        isName = True
    elif (name in title) :
        isName = True
    elif (wikification.query(name)) :
        isName = True
    else :
        isName = False
