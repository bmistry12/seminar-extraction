import nltk
nltk.download()
from nltk.corpus import brown
from nltk.corpus import treebank
brown.words()
treebank.words()
brown.tagged_words()
brown.tagged_words(tagset='universal')
treebank.words()
treebank.tagged_words()
#print(treebank.parsed_sents('wsj_0003.mrg')[0])
from nltk.tag import DefaultTagger
tagger = DefaultTagger('NN')
tagger.tag_sents([['Hello','.'],['My','name','is','Steve']])
[[('Hello', 'NN'), ('.', 'NN')], [('My', 'NN'), ('name', 'NN'), ('is', 'NN'), ('Steve', 'NN')]]
train_sents = treebank.tagged_sents()[:3000]
test_sents = treebank.tagged_sents()[3000:]
tagger.evaluate(test_sents)
from nltk.tag import UnigramTagger
unigram_tagger = UnigramTagger(train_sents)
unigram_tagger.evaluate(train_sents)
unigram_tagger = UnigramTagger(train_sents)
unigram_tagger.evaluate(test_sents)
tagger = UnigramTagger(train_sents, cutoff=3)
tagger.evaluate(train_sents)
from nltk.tag import BigramTagger
bigram_tagger = BigramTagger(train_sents)
bigram_tagger.evaluate(train_sents)
from nltk.tag import TrigramTagger
trigram_tagger = TrigramTagger(train_sents)
trigram_tagger.evaluate(train_sents)
biagram_tagger.evaluate(train_sents)
trigram_tagger.evaluate(train_sents)
bigram_tagger.evaluate(train_sents)
unigram_tagger.evaluate(train_sents)
tagger = UnigramTagger(train_sents, cutoff=3)
tagger.evaluate(train_sents)
tagger = BigramTagger(train_sents, cutoff=3)
tagger.evaluate(train_sents)
tagger = TrigramTagger(train_sents, cutoff=3)
tagger.evaluate(train_sents)
from brill_tagger_wrapper import *
