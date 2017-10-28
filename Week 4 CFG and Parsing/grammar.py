import nltk

def grammar1() :
	grammar1 = nltk.CFG.fromstring("""
	 S -> NP VP 
	 VP -> V NP | V NP PP | V PP | PP
	 PP -> Prep NP  | V N | PP 
	 V -> "enjoyed" | "going" | "watches" | "didn't" | "went" | "walked" | "watch" | "likes" | "used" | "like" | adj V
	 NP -> "John" | "Smith" | "Jane" | "Lee" | "Kim" | "Mary" | NP NP | Det N | NP V | PN
	 Det -> "the" | "The"
	 N -> "telescope" | "cinema" |  | "child" | "december" | "home" | "Man" | "movies"  | adj N
	 Prep -> "to" | "with" | "in" 
	 PN   ->  "He" | "They" | "this" | "she"
	 adj  -> "sometimes" | "Every" | "horror" | "western"
	 """) 

