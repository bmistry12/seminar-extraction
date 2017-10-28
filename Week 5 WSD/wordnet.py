import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import semcor

##
print (wn.synsets('dog')) #set of synonyms with a common meaning
print (wn.synsets('dog', pos=wn.VERB)) #synsets that are verbs

var = input ("Would you like to process user input 'u' or SemCor 's': ")
if (var == 'u') :
    word = input ("Please enter a word to process: ")
    senses = (wn.synsets(word))
    for x in senses :
        print(x , " - " , x.definition())
    print("------------- hypernyms --------------")
    print(senses[0].hypernyms())
    print("------------- hyponyms --------------")
    print(senses[0].hyponyms())
    print("------------- hypernyms closure--------------")
    hyper = lambda s: s.hypernyms()
    print(list(senses[0].closure(hyper)))         
elif (var == 's' ) :
    sentences = semcor.sents()
    i = 0
    for sent in sentences :
        if ( i < 100 ) :
            print(sent)
            for word in sent :
                senses = (wn.synsets(word))
                for x in senses :
                    print(x , " - " , x.definition())
            i = i + 1

    

