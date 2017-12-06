import re
from nltk.corpus import wordnet as wn

class Ontology():
    def __init__(self) :
        self.histWords = ['history']
        self.chemWords = ['chemistry', 'elements']
        self.phyWords = ['physics', 'nasa', 'superposition', 'space']
        self.bioWords = ['biology', 'human']
        self.mathsWords = ['maths', 'mathematical', 'graphs']
        self.robWords = ['robot', 'robots', 'robotics', 'robotic',  'autonomou']
        self.aiWords = ['ai', 'machine', 'arfiticial', 'intelligence']
        self.hciWords = ['hci', 'human']
        self.visWords = ['vision']
        self.techWords = ['computing', 'programming', 'apple', 'technology', 'computer science', 'computer', 'algorithms']
        self.pureWords = ['engineering']
        self.talkWords = ['talk', 'talks', 'environmental']
        self.miscWords = []
        self.ontology = {
            'Top' : {
                "Arts": {
                    "History": self.histWords, 'talks': list()
                 },
                 "Engineering": {
                     "Computing": {
                        "Robotics": self.robWords, 'talks': list(),
                        "AI": self.aiWords, 'talks': list(),
                        "HCI": self.hciWords, 'talks': list(),
                        "Vision": self.visWords, 'talks': list(),
                        "General_computing": self.techWords, 'talks': list(),
                      },    
                     "Pure": self.pureWords, 'talks': list()
                 },
                 "Science": {
                     "Physics": self.phyWords, 'talks': list(),
                     "Biology": self.bioWords, 'talks': list(),
                     "Chemistry": self.chemWords, 'talks': list(),
                     "Mathematics": self.mathsWords, 'talks': list()
                 },
                 "Other": {
                      "Talks": self.talkWords, 'talks': list(),
                      "Misc": self.miscWords, 'talks': list()
                 }
             }
        }

def check (self, word) :
    #checks word against list of words - returns match if there is one
    if word in self.histWords :
        return("history")
    elif word in self.chemWords :
        return ("chemistry")
    elif word in self.phyWords :
        return ("physics")
    elif word in self.bioWords :
        return ("biology")
    elif word in self.mathsWords :
        return ("maths")
    elif word in self.robWords :
        return ("robotics")
    elif word in self.aiWords :
        return ("AI")
    elif word in self.hciWords :
        return ("HCI")
    elif word in self.visWords :
        return ("vision")
    elif word in self.techWords :
        return ("tech")
    elif word in self.pureWords :
        return ("pure")
    elif word in self.talkWords :
        return ("talks")
    else :
        return ("unknown")

def trasverse(self, location=None, key=None):
    if location is None :
        location = self.ontology
    keys = location.keys()
    if 'topic_words' in keys :
        self.traversal_info[key] = location[key]
        return
    for key in keys :
        self.traverse(location[key], key)
    return

def returnSecond(a) :
    toReturn = ""
    for val in a :
        dis, thisOne, dis2 = val
        toReturn = thisOne
    return thisOne

def wordNet(words, cat):
    #for each word in the list, compare its similarity to the catergory
    #if the overall toatl lis above 0.5, add it to that category 
    totalSum = 0
    length = len(words)
    synRe = 'Synset\(\'(.*)\'\)'
    asynCat = wn.synsets(cat)
    if (asynCat == []) :
        pass
    else :
        a = asynCat[0]
        b = re.findall(synRe, str(a))
        if b == [] :
            pass
        else :
            synCat = wn.synset(b[0])
            avoid = ['the', 'be', 'by', 'who', 'when', 'why', 'where', 'how', 'what', 'this',
                     'being', 'with', 'a', 'an', 'of']
            index = 0
            for aword in words:
                word = aword.lower()
                if word not in avoid :
                    asynWord = wn.synsets(word)
                    if (asynWord == []) :
                        pass
                    else :
                        a = asynWord[0]
                        b = re.findall(synRe, str(a))
                        if (b == []):
                            pass
                        else :
                            synWord = wn.synset(b[0])
                            similarity = synWord.path_similarity(synCat)
                            if (similarity == None):
                                similarity = 0
                            if (index == length):
                                #the last one is email type - many email types are robotics and so this may effect results
                                similarity = similarity / 4
                            totalSum = totalSum + similarity
                            index = index + 1
    print("TOTAL SUM : " + str(totalSum))
    print(cat)
    if(totalSum > 0.5):
        return cat
    else :
        return 'Misc'
    
def analyseTags(tagList, prior) :
    #all words and tags are seperated by can still be back accessed using index positions
    #first find number of each tag 
    listoftags = list()
    listofwords = list()
    for tup in tagList:
        tag, word = tup
        listoftags.append(tag)
        listofwords.append(word)
    numh = listoftags.count("history")
    numc = listoftags.count("chemistry")
    numb = listoftags.count("biology")
    nump = listoftags.count("physics")
    numm = listoftags.count("maths")
    numr = listoftags.count("robotics")
    numa = listoftags.count("AI")
    numhci = listoftags.count("HCI")
    numv = listoftags.count("vision")
    numt = listoftags.count("tech")
    numpure = listoftags.count("pure")
    numtalk = listoftags.count("talks")
    d = {'history': numh, 'chemistry': numc, 'biology': numb, 'physics': nump,
         'maths': numm, 'robotics': numr, 'AI': numa, 'HCI': numhci,
         'vision': numv, 'tech': numt, 'pure': numpure, 'talks': numtalk}
    dsorted = sorted(d.values())
    length = len(dsorted)
    if prior == 0:
        maxTag = max(d, key=d.get)
    elif prior == 1 :
        erm = dsorted[length-(prior+1)]
        if erm == 0 :
            return 'Misc'
        else :
            maxTag = d.get(erm)
    val = d.get(maxTag)
    if (val > 1):
        return maxTag
    elif (maxTag == "maths"):
        #any that appear to be maths are likely to be maths
        return maxTag
    elif (val == 1) :
        return wordNet(listofwords, maxTag)
    else :
        analyseTags(tagList, (prior+1))
    
def openTextFile(self, tfid):
    #open the text file and identify lines with Type: and Topic: - filter out any tags
    allPossibleTags = list()
    tags = ["stime", "/stime", "<stime>", "</stime>","etime", "/etime", "<etime>", "</etime>", "sentence", "paragraph",
            "speaker", "location", "/sentence", "/paragraph", "/speaker", "/location", ">", "<", "<speaker>", "</speaker>",
            "<location>", "</locamation>", "<paragraph>", "</paragraph>", "<sentence>", "</sentence>"]
    typeReg = 'Type\s:\s([A-z]*.?){3}'
    topicReg = 'Topic\s:(\s)*(([A-z]*\s)*)'
    path = "my_seminars_tagged/" + str(tfid) + ".txt"
    with open (path, "r") as f :
        corpus = f.read()
        #print(corpus)
        a = re.findall(topicReg, corpus)
        #finding the item that comse after Topic:
        if (a == []):
            pass;
        else :
            a = returnSecond(a)
            words = a.split(" ") #split into words so we can analyse each word agains the tree
            for  word in words :
                cat = check(self, word.lower())
                if (cat == "HCI") :
                    return str(cat)
                allPossibleTags.append((cat, word))
        #finding anything after Type:         
        b = re.findall(typeReg, corpus)
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        etype =  str(b[0]).strip()
        emailType = ""
        #strip any random punctuation
        for char in etype:
            if char not in punctuations:
                emailType = emailType + char
        cat = check (self, emailType.lower())
        allPossibleTags.append((cat, emailType))
        tag = analyseTags(allPossibleTags, 0)
        if (tag == None):
            tag = 'Misc'
        return (str(tag))

def main() :
    #main method - this is to be run from command line
    ontology = Ontology()
    notTagged = True
    textFile = 301
    while(notTagged) :
        print("----------------- " +str(textFile)+ " -----------------")
        category = openTextFile(ontology, textFile)
        print(category)
        if (textFile == 484) :
            notTagged = False
        else :
            textFile = textFile + 1
        
