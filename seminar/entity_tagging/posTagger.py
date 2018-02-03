import re
import nltk
import pickle
import getFileToTag
from nltk import pos_tag
from nltk.corpus import brown
from nltk.corpus import treebank
from nltk.tag import UnigramTagger, BigramTagger, DefaultTagger

corpus2 = []
corpus = getFileToTag.getTokens()
for word in corpus :
    corpus2.append([word])

#training POS tagger using brown corpus
train_sents = brown.tagged_sents()[4000:]
unigram_tagger = UnigramTagger(train_sents, cutoff = 3)
bigram_tagger = BigramTagger(train_sents, backoff=unigram_tagger)

tagged_corpus = bigram_tagger.tag_sents(corpus2)
print(tagged_corpus)
pickle.dump(bigram_tagger, open( 'pos_tagger.pkl', 'wb' ) )

