# Information Extraction of Seminars

## 1) Entity Tagging
Currently Tags: Time, Location, Speakers, Paragraphs and Sentences

Class Files:
* dataFromTraining.py


    The class extracts tagged data from all of the training data (seminars_training/).
    The corpus is split up into sentences and tokenized using sents().
    Speakers and Locations are then extracted and is saved to two text files found in (training_data/). This data is used when tagging the test data and is known as previously seen data.
    This class is currently only run initially when new data is given to initialise the data in the text files and so is not currently linked to any other class.

* getFileToTag.py
    


    Gets the next file that needs to be tagged from (seminar_test_data/test_untagged).
    It tags the sentences and paragraphs in the file and tokenizes it.
    Imported into all classes that require the tokens of the email

* posTagger.py



    Part Of Speech Tagger - trained on the Brown Corpus using the brown corpus. 
    Uses a bigram tagger, with a unigram back off, to tag each token of the corpus.
    I save and load the pos tagger between the classes using pickle, creating the pos_tagger.pkl file
    
* ner.py


    Named Entity Recognition - Identify names and tags them if required
    Uses wikification.py
    
* wikification.py


    Uses the Wikipedia API to compare certain entires against wikipedia 
    Used to help identify names and filter out company names
    
* seminars.py



    This is the main class file.
    Tokens are POS Tagged, analysed with the NER and tagged accordingly
    
* evaluate.py


    Evaluates my tagged data (my_seminars_tagged) against the actual tagged data (seminars_test_data/test_tagged).
    Calculates accuracy, precision and f measure.

## 2) Ontology Construction
* Uses ontology.py


    There is a tree that contains the various subjects I had extracted by looking through the text files. 
    For each subject, I assigned a list of key words to them to help with categorising the emails. 
    I included a miscellaneous category as I knew that there would be some emails that my system would fail to categorise.
    In order to run the Ontology Classification the method main() must be run from command line
    The text file is opened using openTextFile, and anything following the ‘Type:’ and ‘Topic’ segments of the email using regex. 
	I split the sentence that comes directly after topic into words, and categorise each word. 
	To do this, I passed it into the check() method. 
	Here the word is checked against the list of keywords for each branch respectively, returning the appropriate string. 
	This is also done for type. These tags are all accumulated into a list of tuples of the following format: (category, word). 
	This list is then passed through to the analyseTags() method.
    Here, the number of occurrences for each category is counted and stored in a dictionary. 
	If the highest category has a count greater than two, the email is classified with that category. 
    If the highest category has count of one, we pass it through to the wordNet() method.
    If there are 0 occurrences for everything we simple return ‘Misc’ as we cannot effectively classify the email based on the given data set.
	
    I use word net to calculate the distance between each word in the list and the category of choice. 
	I have filtered out some words – in the avoid list – as they would not contribute positively to the outcome due to their neutrality. 
	The similarity of each word to the category is added to the variable ‘totalSum,’ which I use to evaluate whether the email should be categorised or not. 
	I chose my minimum sum value to be 0.5, as that means that for an average of a five-word description each one will have a similarity of around 0.1.
    Finally, I add the text file to the appropriate category according to the tree and once all text files have been classified, I print a list of each text file in each category.

    
 