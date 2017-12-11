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
    


    H
    
* seminars.py



    H   
* ner.py


    H
* posTagger.py



    H
* wikification.py


    H
* evaluate.py


    H

## 2) Ontology Construction
Uses ontology.py

     There is a tree that contains the various subjects I had extracted by looking through the text files. 
     For each subject, I assigned a list of key words to them to help with categorising the emails. 
     I included a miscellaneous category as I knew that there would be some emails that my system would fail to categorise.
     In order to run the Ontology Classification the method main() must be run from command line
     The text file is opened using openTextFile, and anything following the ‘Type:’ and ‘Topic’ segments of the email using regex. I split the sentence that comes directly after topic into words, and categorise each word. To do this, I passed it into the check() method. Here the word is checked against the list of keywords for each branch respectively, returning the appropriate string. This is also done for type. These tags are all accumulated into a list of tuples of the following format: (category, word). This list is then passed through to the analyseTags() method.
     Here, the number of occurrences for each category is counted and stored in a dictionary. If the highest category has a count greater than two, the email is classified with that category. 
     If the highest category has count of one, we pass it through to the wordNet() method.
     If there are 0 occurrences for everything we simple return ‘Misc’ as we cannot effectively classify the email based on the given data set.
     
     I use word net to calculate the distance between each word in the list and the category of choice. I have filtered out some words – in the avoid list – as they would not contribute positively to the outcome due to their neutrality. The similarity of each word to the category is added to the variable ‘totalSum,’ which I use to evaluate whether the email should be categorised or not. I chose my minimum sum value to be 0.5, as that means that for an average of a five-word description each one will have a similarity of around 0.1.
     Finally, I add the text file to the appropriate category according to the tree and once all text files have been classified, I print a list of each text file in each category.

--------------
        getFileToTag.py     -> This class is simply used to get the data from a text file to be tagged. It is used in the majority of files that manipulate/tag data
    						   It tokenizes the corpus using nltk.word_tokenize. This removes elements such as \n and \r as well as splitting the corpus into a list of words
    						   The method getTokens() allows the tokens to be passed through to other files. 
    	seminars.py         -> This class is currently the main class to run as all other classes are imported into it (apart from dataFromTraining)
    						   There is only one method - printStuff() which prints out the actual tagged version of the file and my tagged version -> this is for testing purposes at this stage
    						   The for loop in the class goes through each element of the list called tokens (explained in getFileToTag.py) and compares it to a set of regex to see whether it is a time or starts with a capital
    						   If it is one of the above, the relevant method in ner.py is called, else it is simplt appended to newDoc (list of my tagged data)
    	ner.py              -> Named Entity Recognition class. 
    						   tagTime() - Tags start and end times depending on elements that come before and after the passed in time
    						               (e.g  if prevWord == - then it is an endTime)
    									   The time regex in seminars.py does not currently account for cases like 12.00pm-1.00pm where the time is not split into separate words due to lack of whitespace.
    							tagLocation() - Iterates through the tokens, comparing the resulting word against values in location.txt (known locations)
    							                Once we reach a point where it no longer matches a value, we know the maximum location string has been found and so this is tagged
    											If this method isn't carried out, words such as 'center' will be tagged, despite it not being a full location name
    							capital() - This is the method called in seminars.py. Currently VOID is used to represent removed words - this is simply for error checking
    		
    
 