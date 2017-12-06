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
    for elem in generated:
        if elem.strip() in actual:
            count = count + 1
    return count
        
def getTN(actual, generated):
    return 0

def getFP(actual, generated):
    count = 0
    for elem in generated :
        if elem.strip() not in actual :
            count = count + 1
    return count


def getFN(actual, generated):
    count = 0
    for elem in actual :
        if elem.strip() not in generated :
            count = count + 1
    return count

def strip(theList):
    index = 0
    for e in theList:
        theList[index] = e.strip()
    return theList

notEnd = True
textFileID = 301
overallAccuracy = 0
maxAcc = 0
overallSpeakAcc = 0
overallLocAcc = 0
overallSTimeAcc = 0
overallETimeAcc = 0
overallPrec = 0
overallRec = 0
overallF = 0
fileNumber = 0

while(notEnd) :
    #actual
    path = "seminar_test_data/test_tagged/" + str(textFileID) + ".txt"
    tagged = nltk.data.load(path)
    ataggedSpeakers = re.findall(spReg, tagged)
    ataggedLoc = re.findall(locReg, tagged)
    ataggedSTime = re.findall(sTimeReg, tagged)
    ataggedETime = re.findall(eTimeReg, tagged)
    removeSecond(ataggedSpeakers)
    removeSecond(ataggedLoc)
    removeSecond(ataggedSTime)
    removeSecond(ataggedETime)
    taggedSpeakers = strip(ataggedSpeakers)
    taggedLoc = strip(ataggedLoc)
    taggedSTime = strip(ataggedSTime)
    taggedETime = strip(ataggedETime)
    #generated
    path = "my_seminars_tagged/" + str(textFileID) + ".txt"
    tagged = nltk.data.load(path)
    aSpeakers = re.findall(spReg, tagged)
    aLocation = re.findall(locReg, tagged)
    aSTime = re.findall(sTimeReg, tagged)
    aETime = re.findall(eTimeReg, tagged)
    removeSecond(aSpeakers)
    removeSecond(aLocation)
    removeSecond(aSTime)
    removeSecond(aETime)
    Speakers = strip(aSpeakers)
    Location = strip(aLocation)
    STime = strip(aSTime)
    ETime = strip(aETime)
    
    print(taggedSpeakers)
    print(taggedLoc)
    print(taggedSTime)
    print(taggedETime)
    print("***")
    print(Speakers)
    print(Location)
    print(STime)
    print(ETime)
    print("***")

    speakAcc = 0
    locAcc = 0
    stimeAcc = 0 
    etimeAcc = 0
    precision = 0
    recall = 0
    fmes = 0
    
    if (taggedSpeakers == [] and Speakers == []):
        speakAcc = 1
    else:
        d = (getTP(taggedSpeakers, Speakers) + getFP(taggedSpeakers, Speakers) + getFN(taggedSpeakers, Speakers))
        speakAcc = getTP(taggedSpeakers, Speakers) / d

    if (taggedLoc == [] and Location == []):
        locAcc = 1
    else :
        d = (getTP(taggedLoc, Location) + getFP(taggedLoc, Location) + getFN(taggedLoc, Location))
        locAcc = getTP(taggedLoc, Location) / d

    if (taggedSTime == [] and STime == []):
        stimeAcc = 1
    else :
        d = (getTP(taggedSTime, STime) + getFP(taggedSTime, STime) + getFN(taggedSTime, STime))
        stimeAcc = getTP(taggedSTime, STime) / d

    if (taggedETime == [] and ETime == []):
        etimeAcc = 1
    else :
        d = (getTP(taggedETime, ETime) + getFP(taggedETime, ETime) + getFN(taggedETime, ETime))
        etimeAcc = getTP(taggedETime, ETime) / d

    TP = getTP(taggedSpeakers, Speakers) + getTP(taggedLoc, Location) + getTP(taggedSTime, STime) + getTP(taggedETime, ETime) 
    FP = getFP(taggedSpeakers, Speakers) + getFP(taggedLoc, Location) + getFP(taggedSTime, STime) + getFP(taggedETime, ETime) 
    FN = getFN(taggedSpeakers, Speakers) + getFN(taggedLoc, Location) + getFN(taggedSTime, STime) + getFN(taggedETime, ETime) 

    accuracy = TP / (TP + FP + FN)
    TPClass = len(Speakers) + len(Location) + len(STime) + len(ETime)
    if TPClass > 0 and TP > 0:
        precision = TP / TPClass
    else :
        precision = 0
    TPCorpus = len(taggedSpeakers) + len(taggedLoc) + len(taggedSTime) + len(taggedETime)
    if (TPCorpus > 0 and TP > 0):
        recall = TP / TPCorpus
    else :
        recall = 0 
    if ((precision + recall ) > 0):
        fmes = 2 * (precision * recall) / (precision + recall)
    else :
        fmes = 0
    print("accuracy for text file " + str(textFileID) + ": " + str(accuracy*100))
    print("Speaker: " + str(speakAcc))
    print("Location:" + str(locAcc))
    print("STime " + str(stimeAcc))
    print("ETime " + str(etimeAcc))
    print("Precision: " + str(precision))
    print("Recall: " + str(recall))
    print("F measure: " + str(fmes))
    print("--------------------------------------------------")

    #add to overall values
    fileNumber = fileNumber + 1
    overallAccuracy = overallAccuracy + accuracy
    overallSpeakAcc = overallSpeakAcc + speakAcc
    overallLocAcc = overallLocAcc + locAcc
    overallSTimeAcc = overallSTimeAcc + stimeAcc
    overallETimeAcc = overallETimeAcc + etimeAcc
    overallPrec = overallPrec + precision
    overallRec = overallRec + recall
    ovareallF = overallF + fmes
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
print("Precision: " + str(overallPrec*100 / fileNumber))
print("Recall: " + str(overallRec*100 / fileNumber))
print("F: " + str(overallF*100 / fileNumber))
