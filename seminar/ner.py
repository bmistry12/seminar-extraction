import nltk
import re
from nltk.corpus import brown
from nltk.corpus import treebank

daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
titles = ["Professor", "Prof", "Dr", "Doctor", "Mr", "Mrs", "Miss", "Ms", "prof", "professor", "dr", "doctor", "mr", "mrs", "miss", "ms"]
person_pattern = re.compile("<ENAMEX\sTYPE='PERSON'>(.*?)</ENAMEX>") 
punct = "!#$%&()*+,-.:;?@[\]^_`{|}~"

def capital (word, index):
    printWord = " "
    if (word in daysOfWeek) :
        return  ('<day>' +  word + '</day>')
    elif (word in months) :
        return ('<month>' +  word + '</month>')
    elif (word in titles):
        #we have a name coming up fam
        nextWord = tokens[index+1]
        nextNextWord = tokens[index+2]
        if (nextWord.matches(person_pattern)) :
            a = [word] ++ [nextWord]
    else :
        return (word)
	
	
