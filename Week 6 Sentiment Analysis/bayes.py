import math
import re

dict = {"a tasty pizza": "+", "glorious cheese": "+", "the best restaurant ever": "+",
        "cold and gloopy": "-", "poor and slow service": "-", "unbelievably bad": "-"}
D = "the pizza was horrible"
dLength = len(dict)

def trainNaiveBayes(D, C) :
    for aclass in C :
        nDoc = dLength
        nC = sum (x == aclass for x in dict.values())
        logPrior = math.log((nC/nDoc), 2)
        print (logPrior)
        V = getWords(D)
        bigDoc = 
        for word in V :
            
            


def getWords(D) :
    return D.split()
