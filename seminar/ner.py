import nltk
import re
from nltk.corpus import brown
from nltk.corpus import treebank

#tags any times correctly
def tagTime(word, index):
    import seminars
    tokens = seminars.getTokens()
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
TO DO
---------------------
doesnt consider casese like
12:00pm-1:00pm
'''

daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
titles = ["Professor", "Prof", "Dr", "Doctor", "Mr", "Mrs", "Miss", "Ms", "prof", "professor", "dr", "doctor", "mr", "mrs", "miss", "ms"]
punct = "!#$%&()*+,-.:;?@[\]^_`{|}~"
locFile = "location.txt"
speakFile = "speakers.txt"
avoidWords = []

#check to see if a word already exists in the training data text file
def checkFile(word, file):
    with open(file) as f:
        if word in f.read() :
            return True
    return False            

#tag speakers - currently only tags speakers who exist in training data
def tagSpeakers (word):
    return "<speaker> " + word + "</speaker>"

#tag locations - currently only those that exists in training data 
def tagLocation (word,tokens, index) :
    print("HI : " + word)
    theLocation = word
    jointWord = word
    i = 1
    isLocation = True
    while isLocation :
        jointWord = jointWord + ' ' + tokens[index+i]
        if checkFile(jointWord, locFile) :
            avoidWords.append(tokens[index+i])
            theLocation = theLocation + ' ' + tokens[index+i]
            i = i + 1
        else :
            isLocation = False
            if tokens[index+i] in theLocation:
                avoidWords.append(tokens[index+i])
    return "<location> " + theLocation + " </location>"
'''
still tags stuff like IN just because its in the text file somewhere
need to get rid of this somehow
'''
    
def capital (word, index):
    if ((word in daysOfWeek) or (word in months)) :
        avoidWords.append(word)
        return word
    else :
        import seminars
        tokens = seminars.getTokens()
        word2 = tokens[index+1]
        word3 = tokens[index+2]
        join2 = word + ' ' + word2
        join3 = join2 + ' ' + word
        if (checkFile(join3, speakFile)):
            return tagSpeakers(join3)
        elif (checkFile(join2, speakFile)):
            return tagSpeakers(join2)
        #elif (word not in avoidWords) :
        elif (checkFile(word, locFile)) :
            return (tagLocation(word, tokens, index))
        else :
            avoidWords.append(word)
            return word

