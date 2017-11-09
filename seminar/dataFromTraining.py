import nltk
from nltk import sent_tokenize
import re
#regex
capitals = '^[A-Z]'
#spReg = '< speaker >{1}[A-z]*\s[A-z]*</ speaker >{1}'
#spReg = '<\sspeaker\s>\s[A-z]*\s[A-z]*\s</\sspeaker\s>'
spReg = '<\sspeaker\s>\s([!-z]+\s)+</\sspeaker\s>'
#read from training data
from os import listdir
from os.path import isfile, join
trainPath = "seminars_training"
onlyfiles = [f for f in listdir(trainPath) if isfile(join(trainPath, f))]
corpus_root = trainPath
training = nltk.corpus.reader.plaintext.PlaintextCorpusReader(corpus_root, onlyfiles)
#training =  nltk.data.load('seminars_training/12.txt')
train_sents = training.sents() #split corpus into sentences
#train_sents =  sent_tokenize(training)
speakers = []
join_sents = "";
for sents in train_sents :
    join_sents = ' '.join(sents)
    match = re.search(spReg, join_sents)
    if (match is not None):
        speaker = match.group()
        speakers.append(speaker)

print('--------')
print(speakers)

f = open('speakers.txt', 'a')
for a in speakers :
    f.write('%s\n' % a)
f.close()
