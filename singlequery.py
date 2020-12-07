
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.tree import DecisionTreeClassifier

def process(path,input):
	data = pd.read_csv(path, usecols=['text', 'author'])
	
	data=data[:4000]
	data[['author']] = data[['author']].replace(["Alcott", "Austen", "Bronte", "Collins","Doyle","Montgomery", "Stoker","Twain"], [0,1,2,3,4,5,6,7])
	x = data['text'].values
	y = data['author'].values

	print(x)
	print(y)
	n_most_common_words = 3000
	max_len = 130
	tokenizer = Tokenizer(num_words=n_most_common_words, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
	tokenizer.fit_on_texts(x)
	sequences = tokenizer.texts_to_sequences(x)
	word_index = tokenizer.word_index
	print('Found %s unique tokens.' % len(word_index))
	
	X = pad_sequences(sequences, maxlen=max_len)

	X_train=X
	y_train=y
	
	seq = tokenizer.texts_to_sequences(input)
	padded = pad_sequences(seq, maxlen=max_len)


	model2= DecisionTreeClassifier()
	model2.fit(X_train, y_train)
	y_pred = model2.predict(padded)
	labels = ["Alcott", "Austen", "Bronte", "Collins","Doyle","Montgomery", "Stoker","Twain"]
	print(y_pred, labels[int(y_pred)])

	return labels[int(y_pred)]


#input=[]
#input.append("Where would I go to?”  “Well, looky here, boss, dey's sumf'n wrong, dey is.")
#path="author_data.csv"
#process(path,input)