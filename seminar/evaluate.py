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
maxAcc = 0
overallSpeakAcc = 0
overallLocAcc = 0
overallSTimeAcc = 0
overallETimeAcc = 0
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

    accSpeakers = (getTP(taggedSpeakers, Speakers) + getTN(taggedSpeakers, Speakers)) / (getTP(taggedSpeakers, Speakers) + getTN(taggedSpeakers, Speakers) + getFP(taggedSpeakers, Speakers) + getFN(taggedSpeakers, Speakers))
    accLoc = (getTP(taggedSpeakers, Speakers) + getTN(taggedLoc, Speakers)) / (getTP(taggedLoc, Speakers) + getTN(taggedLoc, Speakers) + getFP(taggedLoc, Speakers) + getFN(taggedLoc, Speakers))
    accSTime = (getTP(taggedSpeakers, Speakers) + getTN(taggedSTime, Speakers)) / (getTP(taggedSTime, Speakers) + getTN(taggedSTime, Speakers) + getFP(taggedSTime, Speakers) + getFN(taggedSTime, Speakers))
    accETime = (getTP(taggedSpeakers, Speakers) + getTN(taggedETime, Speakers)) / (getTP(taggedETime, Speakers) + getTN(taggedETime, Speakers) + getFP(taggedETime, Speakers) + getFN(taggedETime, Speakers))

    TP = getTP(taggedSpeakers, Speakers) + getTP(taggedLoc, Location) + getTP(taggedSTime, STime) + getTP(taggedETime, ETime) 
    TN = getTN(taggedSpeakers, Speakers) + getTN(taggedLoc, Location) + getTN(taggedSTime, STime) + getTN(taggedETime, ETime) 
    FP = getFP(taggedSpeakers, Speakers) + getFP(taggedLoc, Location) + getFP(taggedSTime, STime) + getFP(taggedETime, ETime) 
    FN = getFN(taggedSpeakers, Speakers) + getFN(taggedLoc, Location) + getFN(taggedSTime, STime) + getFN(taggedETime, ETime) 

    accuracy = (TP + TN) / (TP + TN + FP + FN)
    if (accuracy > maxAcc):
        maxAcc = accuracy
    
    print("accuracy for text file " + str(textFileID) + ": " + str(accuracy*100))
    print("Speaker accuracy " + str(accSpeakers*100))
    print("Location accuracy " + str(accLoc*100))
    print("Start Time accuracy " + str(accSTime*100))
    print("End Time accuracy " + str(accETime*100))
    print("--------------------------------------------------")
    fileNumber = fileNumber + 1
    overallAccuracy = overallAccuracy + accuracy
    overallSpeakAcc = overallSpeakAcc + accSpeakers
    overallLocAcc = overallLocAcc + accLoc
    overallSTimeAcc = overallSTimeAcc + accSTime
    overallETimeAcc = overallETimeAcc + accETime
    if(textFileID == 484):
        notEnd = False
    else :
        textFileID = textFileID + 1

print("Overall Accuracy : " + str(overallAccuracy * 100 / fileNumber))
print("Speaker Accuracy : " + str(overallSpeakAcc * 100 / fileNumber))
print("Location Accuracy : " + str(overallLocAcc * 100 / fileNumber))
print("Start Time Accuracy : " + str(overallSTimeAcc * 100 / fileNumber))
print("End Time Accuracy : " + str(overallETimeAcc * 100 / fileNumber))
print("Highest Overall Accuracy: " + str(maxAcc*100))
'''
precision = (TPclass) / (classified)
recall = (TPclass) / (TP_in_corpus)
F =  2 * (precision * recall) / (precision + recall)

print("precision: " + str(precision))
print("recall: " + str(recall))
print("F: " + str(F))
'''
