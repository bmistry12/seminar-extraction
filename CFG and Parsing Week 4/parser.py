import nltk
from nltk.corpus.reader import WordListCorpusReader
from nltk.tag import DefaultTagger
grammar1 = nltk.CFG.fromstring("""
	 S -> NP VP 
	 VP -> V NP | V NP PP | V PP | PP
	 PP -> Prep NP  | V N | PP 
	 V -> "enjoyed" | "going" | "watches" | "didn't" | "went" | "walked" | "watch" | "likes" | "used" | "like" | adj V
	 NP -> "John" | "Smith" | "Jane" | "Lee" | "Kim" | "Mary" | NP NP | Det N | NP V | PN
	 Det -> "the" | "The"
	 N -> "telescope" | "telescopes" | "cinema" |  | "child" | "December" | "home" | "man" | "movies"  | adj N
	 Prep -> "to" | "with" | "in" 
	 PN   ->  "He" | "They" | "this" | "She"
	 adj  -> "sometimes" | "Every" | "horror" | "western"
	 """) 

reader = WordListCorpusReader('text', ['text.txt'])
sentences = reader.words()
print(sentences)
i = 0
newArray = []
for i in range(len(sentences)) :
    print ( sentences[i])
    newArray.append([sentences[i]])
    i = i + 1

#print(newArray)
##print(grammar1)
i = 0
for i in range (len(sentences)) :
    sr_parser = nltk.ShiftReduceParser(grammar1)
    ch_parser = nltk.ChartParser(grammar1)
    sent = sentences[i].split()
    ch_parser.parse(sent)
    sr_parser.parse(sent)

    i = i + 1
    
    
