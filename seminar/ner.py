import nltk
import re
from nltk.corpus import brown
from nltk.corpus import treebank


from nltk.tag import BigramTagger
bigram_tagger = BigramTagger()
print(bigram_tagger)
