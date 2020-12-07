
from nltk import tokenize
import numpy as np
import random
import pandas as pd
import nltk
nltk.download('punkt')
def split_text(filepath, min_char):
    # Load data into string variable and remove new line characters
    file = open(filepath, "r", encoding="utf8")
    text = file.read().replace('\n', ' ')
    text = text.replace('."', '".').replace('."', '".').replace('?"', '"?').replace('!"', '"!')
    text = text.replace('--', ' ').replace('. . .', '').replace('_', '')
    file.close()
    
    # Split text into a list of sentences
    sentences = tokenize.sent_tokenize(text)
    
    # Remove sentences that are less than min_char long
    sentences = [sent for sent in sentences if len(sent) >= min_char]

    return list(sentences)
    
def process():    
	# Set parameter values
	min_char = 5
	
	# Create lists
	alcott = split_text('Books/Little_Women.txt', min_char = min_char)
	austen = split_text('Books/Pride_and_Prejudice.txt', min_char = min_char)\
	         + split_text('Books/Emma.txt', min_char = min_char)
	bronte = split_text('Books/Jane_Eyre.txt', min_char = min_char)
	collins = split_text('Books/Woman_in_White.txt', min_char = min_char)
	doyle = split_text('Books/Study_in_Scarlet.txt', min_char = min_char)\
	        + split_text('Books/Sign_of_the_Four.txt', min_char = min_char)\
	        + split_text('Books/Hound_of_the_Baskervilles.txt', min_char = min_char)
	montgomery = split_text('Books/Anne_of_Green_Gables.txt', min_char = min_char)\
	             + split_text('Books/Anne_of_Avonlea.txt', min_char = min_char)
	stoker = split_text('Books/Dracula.txt', min_char = min_char)
	twain = split_text('Books/Tom_Sawyer.txt', min_char = min_char)\
	        + split_text('Books/Huckleberry_Finn.txt', min_char = min_char)
        
        
        
	# Print length of each list

	text_dict = {'Alcott': alcott, 'Austen': austen, 'Bronte': bronte, 'Collins': collins,
             'Doyle': doyle, 'Montgomery': montgomery, 'Stoker': stoker, 'Twain': twain}

	for key in text_dict.keys():
	    print(key, ':', len(text_dict[key]))
    
    
	# Set random seed
	np.random.seed(1)
	
	# Set length parameter
	max_len = 8500

	# Select sentences
	names = [alcott, austen, bronte, collins, doyle, montgomery, stoker, twain]
	combined = []

	for name in names:
	    name = np.random.choice(name, max_len, replace = True)
	    combined += list(name)

	print('The length of the combined list is:', len(combined))


	labels = ['Alcott']*max_len + ['Austen']*max_len + ['Bronte']*max_len + ['Collins']*max_len\
	         + ['Doyle']*max_len + ['Montgomery']*max_len + ['Stoker']*max_len + ['Twain']*max_len

	print('The length of the labels list is:', len(labels))

	# Set random seed
	random.seed(3)

	# Randomly shuffle data
	zipped = list(zip(combined, labels))
	random.shuffle(zipped)
	combined, labels = zip(*zipped)


	# Create pandas dataframe
	out_data = pd.DataFrame()
	out_data['text'] = combined
	out_data['author'] = labels

	print(out_data.head())

	# Export as a csv file
	out_data.to_csv('author_data.csv', index=False)