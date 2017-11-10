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

    speakerF = open('speakers.txt', 'w')
    for a in speakers :
        speakerF.write('%s\n' % a)
    speakerF.close()

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

    locF = open('location.txt', 'w')
    for a in location :
        locF.write('%s\n' % a)
    locF.close()
