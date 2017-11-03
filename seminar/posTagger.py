import nltk
import re
    
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

