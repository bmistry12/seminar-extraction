import nltk
import re
import seminars
from nltk.corpus import brown
from nltk.corpus import treebank


from nltk.tag import BigramTagger
testData = corpus2
bigram_tagger = BigramTagger(testData)
