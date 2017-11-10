import nltk
from nltk import sent_tokenize
import re

#regex
capitals = '^[A-Z]'
spReg = '<\sspeaker\s>\s([!-z]+\s)+</\sspeaker\s>'
locReg = '<\slocation\s>\s([!-z]+\s)+</\slocation\s>'

#read from training data
from os import listdir
from os.path import isfile, join
trainPath = "seminars_training"
onlyfiles = [f for f in listdir(trainPath) if isfile(join(trainPath, f))]
corpus_root = trainPath
training = nltk.corpus.reader.plaintext.PlaintextCorpusReader(corpus_root, onlyfiles)
train_sents = training.sents() #split corpus into sentences

#get anthing in the corpus that is surrounded in speaker tags
def getSpeakers() :
    speakers = []
    join_sents = "";
    for sents in train_sents :
        join_sents = ' '.join(sents)
        match = re.search(spReg, join_sents)
        if (match is not None):
            speaker = match.group()
            #if ('and' in speaker) : split if and is in word
            s = (speaker.strip('< speaker >')).strip('</ speaker >') #strip of tags
            speakers.append(s)
    #add to speakers.txt text file
    speakerF = open('speakers.txt', 'w')
    for a in speakers :
        speakerF.write('%s\n' % a)
    speakerF.close()

#get anthing in the corpus that is surrounded in location tags
def getLocation() :
    location = []
    join_sents = "";
    for sents in train_sents :
        join_sents = ' '.join(sents)
        match = re.search(locReg, join_sents)
        if (match is not None):
            place = match.group()
            p = (place.strip('< location >')).strip('</ location >')
            location.append(p)
    #add to location.txt text file
    locF = open('location.txt', 'w')
    for a in location :
        locF.write('%s\n' % a)
    locF.close()

'''
There are still some adjustments to make to this
e.g. split when there is an 'and'
'''
