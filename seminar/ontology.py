
class Ontology():
    def __init__(self) :
        histWords = ['history']
        chemWords = ['chemistry', 'elements']
        phyWords = ['physics', 'NASA']
        bioWords = ['biology', 'human']
        robWords = ['robot', 'robotics', 'machines']
        aiWords = ['AI', 'machine', 'robots', 'arfiticial', 'intelligence']
        hciWords = ['HCI' 'human']
        visWords = ['vision']
        techWords = ['computing', 'technology', 'computer science', 'computer']
        pureWords = ['engineering']
        talkWords = ['talk', 'talks']
        miscWords = []
        self.ontology = {
            'Top' : {
                "Arts": {
                    "History": histWords
                 },
                 "Engineering": {
                     "Computing": {
                        "Robotics": robWords,
                        "AI": aiWords,
                        "HCI": hciWords,
                        "Vision": visWords,
                        "Tech": techWords
                      },    
                     "Pure": pureWords
                 },
                 "Science": {
                     "Physics": phyWords,
                     "Biology": bioWords,
                     "Chemistry": chemWords
                 },
                 "Other": {
                      "Talks": talkWords,
                       "Misc": miscWords
                 }
             }
        }

def main() :
    ontology = Ontology()
    

def transverse(self, location=None, key=None):
    if location is None :
        location = self.ontology
    keys = location.keys()
    if 'topic_words' in keys :
        self.traversal_info[key] = location[key]
        return
    for key in keys :
        self.traverse(location[key], key)
    return

