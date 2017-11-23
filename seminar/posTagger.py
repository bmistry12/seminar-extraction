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

'''
tagged_corpus = pos_tag(corpus)
#this is trained using treebank
print(tagged_corpus)
nppReg = "([!-z]*, 'NNP')"
randomShit = []
#randomShit = [re.findall(nppReg, tagged_corpus)]
#print(randomShit)

for word, tag in tagged_corpus :
    if (tag == 'None') :
        #we have a word not known in training
        print('none')
    print (word, ' -> ' , tag)

'''
#train_sents = treebank.tagged_sents()[:6000]]
train_sents = brown.tagged_sents()[4000:]
unigram_tagger = UnigramTagger(train_sents, cutoff = 3)
bigram_tagger = BigramTagger(train_sents, backoff=unigram_tagger)

def backoff_tagger(train_sents, tagger_classes, backoff=None):
    for cls in tagger_classes :
        backoff = cls(train_sents, backoff=backoff)
    return backoff
tagged_corpus = bigram_tagger.tag_sents(corpus2)
print(tagged_corpus)
pickle.dump(bigram_tagger, open( 'pos_tagger.pkl', 'wb' ) )

