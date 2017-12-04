
topic_words = getDictionary()
class Ontology():
    def __init__(self) :
        self.ontology = {
            'Top' : {
                'arts' : {
                    'history' : { 'topic_words' : ['history'] },                
                },
                'science' : {
                    'chemistry' : { 'topic_words' : ['chemistry', 'elements' ] },
                    'physics' : { 'topic_words' : ['physics', 'NASA' ] },
                    'biology' : { 'topic_words' : ['biology', 'human'] },   
                        
                }
                'engineering' : {
                    'computing' : {
                        'robotics' : { 'topic_words' : ['Robot', 'Robotics', 'machines' ] },
                        'AI' : { 'topic_words' : ['AI', 'machine', 'robots', 'Arfiticial', 'intelligence' ] },
                        'HCI' : { 'topic_words' : ['HCI'] },
                        'vision' : { 'topic_words' : ['vision' ] },
                        'computer_systems' : { 'topic_words' : ['System', 'Computer']}
                        'other' : { 'topic_words' : ['computing', 'technology', 'computer science']}
                     },
                    'pure' : { 'topic_words' : ['engineering'] },   
                } 'other' : { 'topic_words' : ['Talks'] },
            }
        }

def main() :
    ontology = Ontology()
    

def transverse(self, location=None, key=None):
    if location is None :
        location = self.ontology
    keys = location.keys() :
    if 'topic_words' in keys :
        self.traversal_info[key] = location[key]
        return
    for key in keys :
        self.traverse(location[key], key)
    return
                                            
def dictionary():
    topic_words = {'arts': 'history', 'science':  'chemistry'   }
    
