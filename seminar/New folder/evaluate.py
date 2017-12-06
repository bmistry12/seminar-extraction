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
overallPrec = 0
overallRec = 0
overallF = 0
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
    
    speakStuff =(getTP(taggedSpeakers, Speakers) + getTN(taggedSpeakers, Speakers) + getFP(taggedSpeakers, Speakers) + getFN(taggedSpeakers, Speakers))
    if speakStuff > 0 :
        accSpeakers = (getTP(taggedSpeakers, Speakers) + getTN(taggedSpeakers, Speakers)) / speakStuff
    else :
        accSpeakers = 0
    locStuff = (getTP(taggedLoc, Speakers) + getTN(taggedLoc, Speakers) + getFP(taggedLoc, Speakers) + getFN(taggedLoc, Speakers))
    if locStuff > 0 :
        accLoc = (getTP(taggedSpeakers, Speakers) + getTN(taggedLoc, Speakers)) / locStuff
    else :
        accLoc = 0
    stimeStuff = (getTP(taggedSTime, Speakers) + getTN(taggedSTime, Speakers) + getFP(taggedSTime, Speakers) + getFN(taggedSTime, Speakers))
    if stimeStuff > 0 :
        accSTime = (getTP(taggedSpeakers, Speakers) + getTN(taggedSTime, Speakers)) / stimeStuff
    else :
        accSTime = 0
    etimeStuff = (getTP(taggedETime, Speakers) + getTN(taggedETime, Speakers) + getFP(taggedETime, Speakers) + getFN(taggedETime, Speakers))
    if etimeStuff > 0 :
        accETime = (getTP(taggedSpeakers, Speakers) + getTN(taggedETime, Speakers)) / etimeStuff
    else :
        accETime = 0

    TP = getTP(taggedSpeakers, Speakers) + getTP(taggedLoc, Location) + getTP(taggedSTime, STime) + getTP(taggedETime, ETime) 
    TN = getTN(taggedSpeakers, Speakers) + getTN(taggedLoc, Location) + getTN(taggedSTime, STime) + getTN(taggedETime, ETime) 
    FP = getFP(taggedSpeakers, Speakers) + getFP(taggedLoc, Location) + getFP(taggedSTime, STime) + getFP(taggedETime, ETime) 
    FN = getFN(taggedSpeakers, Speakers) + getFN(taggedLoc, Location) + getFN(taggedSTime, STime) + getFN(taggedETime, ETime) 

    accuracy = (TP + TN) / (TP + TN + FP + FN)
    TPClass = (len(Speakers) + len(Location) + len(STime) + len(ETime))
    if (TPClass > 0 ):
        precision = (TP) / TPClass
    else :
        precision = 0
    TPCorpus = len(taggedSpeakers) + len(taggedLoc) + len(taggedSTime) + len(taggedETime)
    if (TPCorpus > 0):
        recall = TP / TPCorpus
    else :
        recall = 0
    if (precision + recall > 0 ):
        fmes =  2 * (precision * recall) / (precision + recall)
    else :
        fmes = 0
    if (accuracy > maxAcc):
        maxAcc = accuracy
    
    print("accuracy for text file " + str(textFileID) + ": " + str(accuracy*100))
    print("Speaker accuracy " + str(accSpeakers*100))
    print("Location accuracy " + str(accLoc*100))
    print("Start Time accuracy " + str(accSTime*100))
    print("End Time accuracy " + str(accETime*100))
    print("Precision " + str(precision*100))
    print("Recall " + str(recall * 100))
    print("F Measure " + str(fmes))
    print("--------------------------------------------------")
    fileNumber = fileNumber + 1
    overallAccuracy = overallAccuracy + accuracy
    overallSpeakAcc = overallSpeakAcc + accSpeakers
    overallLocAcc = overallLocAcc + accLoc
    overallSTimeAcc = overallSTimeAcc + accSTime
    overallETimeAcc = overallETimeAcc + accETime
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

'''
precision = (TPclass) / (classified)
recall = (TPclass) / (TP_in_corpus)
F =  2 * (precision * recall) / (precision + recall)

print("precision: " + str(precision))
print("recall: " + str(recall))
print("F: " + str(F))
'''
