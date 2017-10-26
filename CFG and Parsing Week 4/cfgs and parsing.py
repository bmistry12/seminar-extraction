import nltk

grammar1 = nltk.CFG.fromstring("""
 S -> NP VP
 VP -> V NP | V NP PP
 PP -> P NP
 V -> "saw" | "ate" | "walked"
 NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
 Det -> "a" | "an" | "the" | "my"
 N -> "man" | "dog" | "cat" | "telescope" | "park"
 P -> "in" | "on" | "by" | "with"
 """)

sent = "Mary saw Bob".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
	print(tree)
sent = "Mary saw Bob with John".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
	print(tree)
sent = "Mary saw the man with the dog".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
	print(tree)
sent = "Mary saw the dog with the man".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
	print(tree)
sent = "Mary saw the man with my dog".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
	print(tree)
sent = "the telescope saw my park".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
	print(tree)
sent = "John ate Mary with the telescope".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
	print(tree)
print("--------------------------------------------")
grammar2 = nltk.CFG.fromstring("""
 S -> NP VP
 VP -> V NP | V NP PP
 PP -> P NP
 V -> "saw" | "ate" | "walked" | "eat" | "Did"
 NP -> "John" | "Mary" | "Bob" | Det N | Det N PP | "who" | "She" | V NP
 Det -> "a" | "an" | "the" | "my" | "The"
 N -> "man" | "dog" | "cat" | "telescope" | "park" | "fork" | "fish"
 P -> "in" | "on" | "by" | "with"
 """)

sent = "She saw the cat".split()
rd_parser = nltk.RecursiveDescentParser(grammar2)
for tree in rd_parser.parse(sent):
	print(tree)
sent = "who eat the fish with the fork".split()
rd_parser = nltk.RecursiveDescentParser(grammar2)
for tree in rd_parser.parse(sent):
	print(tree)
sent = "She ate the fish with the fork".split()
rd_parser = nltk.RecursiveDescentParser(grammar2)
for tree in rd_parser.parse(sent):
	print(tree)
sent = "Did the cat eat the fish".split()
rd_parser = nltk.RecursiveDescentParser(grammar2)
for tree in rd_parser.parse(sent):
	print(tree)
sent = "The cat ate the fish".split()
rd_parser = nltk.RecursiveDescentParser(grammar2)
for tree in rd_parser.parse(sent):
	print(tree)
print("-----------------------------")
tokens = 'Kim likes children'.split()
from nltk import load_parser
cp = load_parser('file.fcfg', trace=2)
for tree in cp.parse(tokens):
        print(tree)
tokens = "Jody disappears".split()
for tree in cp.parse(tokens):
        print(tree)
tokens = "several cars saw these dogs".split()
for tree in cp.parse(tokens):
        print(tree)
tokens = "Kim see car".split()
for tree in cp.parse(tokens):
        print(tree)
tokens = "every children disappears".split()
for tree in cp.parse(tokens):
        print(tree)
print("----changing trace ---------------")
print("----changing trace ------1---------")
tokens = 'Kim likes children'.split()
from nltk import load_parser
cp = load_parser('file.fcfg', trace=1)
for tree in cp.parse(tokens):
        print(tree)
print("----changing trace ----------2-------")
cp = load_parser('file.fcfg', trace=3)
for tree in cp.parse(tokens):
        print(tree)
print("----changing trace --------4-------")
cp = load_parser('file.fcfg', trace=4)
for tree in cp.parse(tokens):
        print(tree)
print("----changing trace --------10-------")
cp = load_parser('file.fcfg', trace=10)
for tree in cp.parse(tokens):
        print(tree)
# `0`` will generate no tracing output and higher numbers will produce more verbose tracing output.
print("-----------Shift Reduce Parsing ---------")
sr_parser = nltk.ShiftReduceParser(grammar1)
sent = 'Mary saw a dog'.split()
for tree in sr_parser.parse(sent):
        tree.draw()
sent = "Mary saw Bob".split()
for tree in sr_parser.parse(sent):
	print(tree)
sent = "Mary saw Bob with John".split()
for tree in sr_parser.parse(sent):
	print(tree)
sent = "Mary saw the man with the dog".split()
for tree in sr_parser.parse(sent):
	print(tree)
sent = "Mary saw the dog with the man".split()
for tree in sr_parser.parse(sent):
	print(tree)
sent = "Mary saw the man with my dog".split()
for tree in sr_parser.parse(sent):
	print(tree)
sent = "the telescope saw my park".split()
for tree in sr_parser.parse(sent):
	print(tree)
sent = "John ate Mary with the telescope".split()
for tree in rd_parser.parse(sent):
	print(tree)
print("-----------Chart Parsing ---------")
chart_parser = nltk.ChartParser(grammar1)
sent = 'Mary saw a dog'.split()
for tree in chart_parser.parse(sent):
        print(tree)
sent = "Mary saw Bob".split()
for tree in chart_parser.parse(sent):
	print(tree)
sent = "Mary saw Bob with John".split()
for tree in chart_parser.parse(sent):
	print(tree)
sent = "Mary saw the man with the dog".split()
for tree in chart_parser.parse(sent):
	print(tree)
sent = "Mary saw the dog with the man".split()
for tree in chart_parser.parse(sent):
	print(tree)
sent = "Mary saw the man with my dog".split()
for tree in chart_parser.parse(sent):
	print(tree)
sent = "the telescope saw my park".split()
for tree in chart_parser.parse(sent):
	print(tree)
sent = "John ate Mary with the telescope".split()
for tree in chart_parser.parse(sent):
	print(tree)
nltk.app.chartparser()
