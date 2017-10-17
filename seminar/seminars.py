import nltk
from os import listdir
from os.path import isfile, join
mypath = "seminars_training"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
corpus_root = mypath
corpus = nltk.corpus.reader.plaintext.PlaintextCorpusReader(corpus_root, onlyfiles)
print(corpus.words())
corpus2 = nltk.data.load('seminars_training/0.txt')
print(corpus2)
tokens = nltk.word_tokenize(corpus2)
print(tokens)
