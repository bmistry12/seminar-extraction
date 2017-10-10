from collections import Counter
import re
import sys

#this creates a dictionary look up for all the times a word occurs in the file
#the regex converst all words to lowercase

def words(text):
    return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big.txt').read()))

#generates a list of values
WORDS.values()
#if print is put in front will print the number of times a word occurs
WORDS['a']

#calculate the number of words in the text file
def calcNumWords () :
    num = sum(WORDS.values())
    return num

#work out the probaility of the word occuring
def P (user_word) :
    times_occ = WORDS[user_word]
    totalWords = calcNumWords()
    prob = times_occ/totalWords
    return (prob)

def edits1 (user_word) :
    #one edit 
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    length = len(user_word)
    set1 = set()
    word_list = wordToList(user_word, length)
    #changing one letter 
    for x in range (0, length) :
        for y in range (0, 26):
            word_list[x] = alphabet[y]
            new_word = ''.join(word_list)
           # if WORDS[new_word] > 0 :
            set1.add( new_word )
            y = y + 1
        x = x + 1
        word_list = wordToList(user_word, length)
        
    #removing a letter
    for x in range (0, length):
        del word_list[x]
        new_word = ''.join(word_list)
        #if WORDS[new_word] > 0 :
        set1.add(new_word)
        x = x + 1 
        word_list = wordToList(user_word, length)
        
    #inserting a letter
    addLetter(user_word, length, alphabet, set1)
    
    #swapping two letters
    for x in range (0, length) :
        for y in range (0 , length) :
            temp = word_list[x]
            temp2 = word_list[y]
            word_list[x] = temp2
            word_list[y] = temp
            new_word = ''.join(word_list)
            set1.add(new_word)
            y = y + 1
            word_list = wordToList(user_word, length)
        x = x +1
    return (set1)

#convert a word to a list
def wordToList(word, length):
    word_list = []
    for z in range (0, length) :
        word_list.append(word[z])
    return word_list

#this is to add a letter to any position in the string (for inserting letter in edits1)
def addLetter(word,length, alphabet, set1) :
    word_list = wordToList(word, length)
    word_list.append('')
    for x in range (0,length+1) :
        for y in range (0 , 26) :
            temp = word_list[x] #contain the element that was in the position
            word_list[x] = alphabet[y]
            for z in range (x+1, length+1):
                temp2 = word_list[z]
                word_list[z] = temp
                temp = temp2
            new_word = ''.join(word_list)
            #if WORDS[new_word] > 0 :
            set1.add(new_word )
            word_list = wordToList(word, length)
            word_list.append('')
                

def edits2(user_word): 
    #two edits
    set2 = set(edit2 for edit1 in edits1(user_word) for edit2 in edits1(edit1))
    return (set2)

def knownWords(words) :
   #checking known words
    return set(known_words for known_words in words if known_words in WORDS)

def candidate(word) :
    #all corrections for misspelling
    actualWords = set()
    setWords = set (knownWords(edits1(word)) or knownWords(edits2(word)) or [word])
    my_list = list(setWords)
    for x in range (0 , len(my_list)) :
        new_word = my_list[x]
        if WORDS[new_word] > 0:
            actualWords.add(new_word)
        x = x + 1
    return (actualWords)
    
    
def correction(word) :
    #giving a missplet word generates all possible corrections and chooses most likely
    allCandidates = set(candidate(word))
    all_cand = list(allCandidates)
    bestWord = ''
    for x in range (0, len(all_cand)):
        highProb = -1
        prob_word = P(all_cand[x])
        if prob_word > highProb :
            bestWord = all_cand[x]
        x = x + 1
    print(bestWord)
