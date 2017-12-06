import re
from nltk.corpus import wordnet as wn

class Ontology():
    def __init__(self) :
        #keywords
        self.histWords = ['history']
        self.chemWords = ['chemistry', 'elements']
        self.phyWords = ['physics', 'nasa', 'superposition', 'space']
        self.bioWords = ['biology', 'human']
        self.mathsWords = ['maths', 'mathematical', 'graphs']
        self.robWords = ['robot', 'robots', 'robotics', 'robotic',  'autonomous']
        self.aiWords = ['ai', 'machine', 'arfiticial', 'intelligence']
        self.hciWords = ['hci', 'human']
        self.visWords = ['vision', 'graphics']
        self.techWords = ['computing', 'programming', 'apple', 'technology', 'computer science', 'computer', 'algorithms']
        self.pureWords = ['engineering', 'buildings', 'steel']
        self.talkWords = ['talk', 'talks', 'environmental']
        self.miscWords = []
        #items
        self.history = list()
        self.chem = list()
        self.phy = list()
        self.bio = list()
        self.maths = list()
        self.robotics = list()
        self.AI = list()
        self.HCI = list()
        self.vision = list()
        self.general_computing = list()
        self.pure = list()
        self.talks = list()
        self.misc = list()
        #ontology tree
        self.ontology = {
            'Top' : {
                "Arts": {
                    "History": self.histWords, 'talks': self.history
                 },
                 "Engineering": {
                     "Computing": {
                        "Robotics": self.robWords, 'talks': self.robotics,
                        "AI": self.aiWords, 'talks': self.AI,
                        "HCI": self.hciWords, 'talks': self.HCI,
                        "Vision": self.visWords, 'talks': self.vision,
                        "General_Computing": self.techWords, 'talks': self.general_computing
                      },    
                     "Pure": self.pureWords, 'talks': self.pure
                 },
                 "Science": {
                     "Physics": self.phyWords, 'talks': self.phy,
                     "Biology": self.bioWords, 'talks': self.bio,
                     "Chemistry": self.chemWords, 'talks': self.chem,
                     "Mathematics": self.mathsWords, 'talks': self.maths
                 },
                 "Other": {
                      "Talks": self.talkWords, 'talks': self.talks,
                      "Misc": self.miscWords, 'talks': self.misc
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

def returnSecond(a) :
    #return second from a tuple
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
    print("Total sum : " + str(totalSum))
    if(totalSum >= 0.5):
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
    #dictionary = category: number of occurances in sentence
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

def cats(self, cat, textFile):
    #add text file to correct category list
    if cat == "history":
        self.history.append(textFile)
    elif cat == "chemistry":
        self.chem.append(textFile)
    elif cat == "physics" :
        self.phy.append(textFile)
    elif cat == "biology":
        self.bio.append(textFile)
    elif cat == "maths":
        self.maths.append(textFile)
    elif cat == "robotics":
        self.robotics.append(textFile)
    elif cat == "AI":
        self.AI.append(textFile)
    elif cat == "HCI":
        self.HCI.append(textFile)
    elif cat == "vision":
        self.vision.append(textFile)
    elif cat == "tech":
        self.general_computing.append(textFile)
    elif cat == "pure":
        self.pure.append(textFile)
    elif cat == "talks":
        self.talks.append(textFile)
    else :
        self.misc.append(textFile)

def printTree(self):
    #print
    print("Arts/History: " + str(self.history) + "\n")
    print("Science/Chemistry: " + str(self.chem) + "\n")
    print("Science/Physics: " + str(self.phy)+ "\n")
    print("Science/Biology: " + str(self.bio)+ "\n")
    print("Science/Maths: " + str(self.maths)+ "\n")
    print("Engineering/Computing/Robotics: " + str(self.robotics)+ "\n")
    print("Engineering/Computing/AI: " + str(self.AI)+ "\n")
    print("Engineering/Computing/HCI: " + str(self.HCI)+ "\n")
    print("Engineering/Computing/Vision: " + str(self.vision)+ "\n")
    print("Engineering/Computing/General_Computing: " + str(self.general_computing)+ "\n")
    print("Engineering/Pure: " + str(self.pure)+ "\n")
    print("Other/Talks: " + str(self.talks)+ "\n")
    print("Other/Misc: " + str(self.misc)+ "\n")
    
def main() :
    #main method - this is to be run from command line
    ontology = Ontology()
    notTagged = True
    textFile = 301
    while(notTagged) :
        print("----------------- " +str(textFile)+ " -----------------")
        category = openTextFile(ontology, textFile)
        print(category)
        cats(ontology, category, textFile)
        if (textFile == 484) :
            notTagged = False
        else :
            textFile = textFile + 1
    print("--------------------------- Print Tree ---------------------------")
    printTree(ontology)
        
