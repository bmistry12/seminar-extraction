#Information Extraction of Seminars

1) Entity Tagging
   Currently tags:     Time, Location and Speaker
   Still need to tag:  Sentences, Paragraphs
    dataFromTraining.py -> This class extracts tagged data from all of the training data (seminars_training/*.txt)
						   The corpus is split up into sentences and tokenized using sents().
						   There are two methods - getSpeakers() and getLocation().
													|                  |
													|                  |----------> returns anything contained in a location tag and writes it to location.txt
													|
													|------> returns anything contained in a speaker tag and writes it to speakers.txt
	                       This class is currently only run initially when new data is given to initialise the data in the text files and so is not currently linked to any other class
						   Once the act of extracting data is finalised, I will import it to the seminars.py file so that they're automatically updated
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
		    						   

2) Ontology Construction
   Not yet started
   Create a classificataion for announcements 
   Text file id for all announcements related to a specific topic
   Needs structured classificataion 