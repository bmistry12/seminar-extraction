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
#paragraphs and sents

def removeSecond(taggedSet) :
    i = 0
    for val in taggedSet :
        thisOne, discard = val
        taggedSet[i] = thisOne
        i = i + 1

def getTP(actual, generated):
    count = 0
    for elem in generated :
        if elem in actual :
            count = count + 1
    return count

def getTN(actual, generated):
    #what is this??
    return 1

def getFP(actual, generated):
    count = 0
    for elem in generated :
        if elem not in actual :
            count = count + 1
    return count


def getFN(actual, generated):
    count = 0
    for elem in actual :
        if elem not in generated :
            count = count + 1
    return count

notEnd = True
textFileID = 301
overallAccuracy = 0
fileNumber = 0

while(notEnd) :
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

    print("actual")
    print(taggedSpeakers)
    print(taggedLoc)
    print(taggedSTime)
    print(taggedETime)
    print("tagged")
    print(Speakers)
    print(Location)
    print(STime)
    print(ETime)


    TP = getTP(taggedSpeakers, Speakers) + getTP(taggedLoc, Location) + getTP(taggedSTime, STime) + getTP(taggedETime, ETime) 
    TN = getTN(taggedSpeakers, Speakers) + getTN(taggedLoc, Location) + getTN(taggedSTime, STime) + getTN(taggedETime, ETime) 
    FP = getFP(taggedSpeakers, Speakers) + getFP(taggedLoc, Location) + getFP(taggedSTime, STime) + getFP(taggedETime, ETime) 
    FN = getFN(taggedSpeakers, Speakers) + getFN(taggedLoc, Location) + getFN(taggedSTime, STime) + getFN(taggedETime, ETime) 

    accuracy = (TP + TN) / (TP + TN + FP + FN) 
    print("accuracy for text file " + str(textFileID) + ": " + str(accuracy*100))
    fileNumber = fileNumber + 1
    overallAccuracy = overallAccuracy + accuracy
    if(textFileID == 330):
        notEnd = False
    else :
        textFileID = textFileID + 1

print("Overall Accuracy : " + str(overallAccuracy * 100 / fileNumber))
'''
precision = (TPclass) / (classified)
recall = (TPclass) / (TP_in_corpus)
F =  2 * (precision * recall) / (precision + recall)

print("precision: " + str(precision))
print("recall: " + str(recall))
print("F: " + str(F))
'''
