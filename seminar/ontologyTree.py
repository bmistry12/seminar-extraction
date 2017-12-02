
def main() :

    ontology = ontology()
    for file_data in data :

        if in_training :
            save_tagged_data(tagged_data)
            ontology.add_topics_interactive(topic, file_name)

        ontology.add_to(file_name, topic_info)



class ontology():
    def __init__() :
        ontology = {
            'Top' : {
                'arts' : {
            'history' : { 'topic_words' : ['histroy', 'war']
                          'talks' : list()
            }
            'science': {


            }
            traversal_info = dict()
            self.traverse()

    def add_topics_interactive( self, topic, file_name ) 
    def add_to( self, topic, file_name )

def traverse( self, location=None, key=None ) :
	if location is None : 
		location = self.ontology
	keys =  location.keys() : 
	if  ‘topic_words’ in keys : 
		self.traversal_info[ key ] = location[ key ]
		return 
	for key in keys : 
		self.traverse( location[key], key )

	return

def add_topics_interactive( self, topic, file_name ) :
	
	# or do this manually.
	
	print( “Topic: ” + topic ) 
	print( self.print() )  ## define this.
	input_class   = input( “Enter Class”: ) 
	input_words = input( “Class words:” )
	self.traverse[ input_class.rstrip() ][‘topic_words’] += 
input_words.rsrip().split( ‘,’ )

def add_to( self, topic, file_name ) :
	# use word2vec to find similarity between words in topic
	#	and ‘topic_words’. Closest is correct class.
	scores = \\
[ 
 ( dist_measure( topic, traversal_info[key][‘topic_words’], 
 	    key  )
 for key in self.traversal_info.keys() 
      ] 
max_key = \\
   scores.sort(key=lambda tup: tup[0], reverse=True)[0][1]
	self.traverse[ max_key ][‘talks’].append( file_name) 



