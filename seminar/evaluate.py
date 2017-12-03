import re
import nltk
'''
evaluate my tagged version against the actual tagged version

TP correctly retrieved instances
TN correctly ignored non-instances
FP incorrectly classed instances
FN actual instances which are missed.


'''
spReg = '<speaker>(([A-z]+\s?)+)</speaker>'
locReg = '<location>(([0-z]+\s?)+)</location>'
sTimeReg = '<stime>(([0-z]+\s?)+)</stime>'
eTimeReg = '<etime>(([0-z]+\s?)+)</etime>'
#paragraohs and sents

def removeSecond(taggedSet) :
    i = 0
    for val in taggedSet :
        thisOne, discard = val
        taggedSet[i] = thisOne
        i = i + 1

textFileID = 301

path = "seminar_test_data/test_tagged/" + str(textFileID) + ".txt"
tagged = nltk.data.load(path)
taggedSpeakers = re.findall(spReg, tagged)
taggedLoc = re.findall(locReg, tagged)
taggedSTime = re.findall(sTimeReg, tagged)
taggedETime = re.findall(eTimeReg, tagged)

removeSecond(taggedSpeakers)
removeSecond(taggedLoc)
removeSecond(taggedSTime)
removeSecond(taggedETime)


path = "my_seminars_tagged/" + str(textFileID) + ".txt"
tagged = nltk.data.load(path)
Speakers = re.findall(spReg, tagged)
Location = re.findall(locReg, tagged)
STime = re.findall(sTimeReg, tagged)
ETime = re.findall(eTimeReg, tagged)

removeSecond(Speakers)
removeSecond(Location)
removeSecond(STime)
removeSecond(ETime)

print(taggedSpeakers)
print(taggedLoc)
print(taggedSTime)
print(taggedETime)

print(Speakers)
print(Location)
print(STime)
print(ETime)
'''
accuracy = (TP + TN) / (TP + TF + FP + FN)
precision = (TPclass) / (classified)
recall = (TPclass) / (TP_in_corpus)
F =  2 * (precison * recall) / (precision + recall)
'''
