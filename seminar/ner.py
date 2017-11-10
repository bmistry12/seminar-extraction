import nltk
import re
from nltk.corpus import brown
from nltk.corpus import treebank

daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
titles = ["Professor", "Prof", "Dr", "Doctor", "Mr", "Mrs", "Miss", "Ms", "prof", "professor", "dr", "doctor", "mr", "mrs", "miss", "ms"]
punct = "!#$%&()*+,-.:;?@[\]^_`{|}~"
locFile = "location.txt"
speakFile = "speakers.txt"

def checkFile(word, file):
    with open(file) as f :
        found = False
        for line in f :
            if line == word :
                found = True
        
def capital (word, index):
    import seminars
    tokens = seminars.getTokens()
    print("HELLO")
    printWord = " "
    nextWord = tokens[index+1]
    nextNextWord = tokens[index+2]
    name = word + ' ' + nextWord
    print("NAME:: " + name)
    isInFile = checkFile(name, speakFile)
    print(isInFile)
    if (isInFile):
        "WE HAVE A NAME IN THE FILE BITCHES"
    elif (word in daysOfWeek) :
        return  ('<day>' +  word + '</day>')
    elif (word in months) :
        return ('<month>' +  word + '</month>')
    else :
        return (word)
	
	
