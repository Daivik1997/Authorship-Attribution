
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from keras.models import Sequential
from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from keras.callbacks import EarlyStopping
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


def process(path,input):
	data = pd.read_csv(path, usecols=['text', 'author'])
	data=data[:4000]
	data.author.value_counts()


	#I do aspire here to have balanced classes
	num_of_categories = 45000
	shuffled = data.reindex(np.random.permutation(data.index))
	Alcott = shuffled[shuffled['author'] == 'Alcott'][:num_of_categories]
	Austen = shuffled[shuffled['author'] == 'Austen'][:num_of_categories]
	Bronte = shuffled[shuffled['author'] == 'Bronte'][:num_of_categories]
	Collins = shuffled[shuffled['author'] == 'Collins'][:num_of_categories]
	Doyle = shuffled[shuffled['author'] == 'Doyle'][:num_of_categories]
	Montgomery = shuffled[shuffled['author'] == 'Montgomery'][:num_of_categories]
	Stoker = shuffled[shuffled['author'] == 'Stoker'][:num_of_categories]
	Twain = shuffled[shuffled['author'] == 'Twain'][:num_of_categories]
	

	concated = pd.concat([Alcott,Austen,Bronte,Collins,Doyle,Montgomery,Stoker,Twain], ignore_index=True)
	#Shuffle the dataset
	concated = concated.reindex(np.random.permutation(concated.index))
	concated['LABEL'] = 0
	#One-hot encode the lab
	concated.loc[concated['author'] == 'Alcott', 'LABEL'] = 0
	concated.loc[concated['author'] == 'Austen', 'LABEL'] = 1
	concated.loc[concated['author'] == 'Bronte', 'LABEL'] = 2
	concated.loc[concated['author'] == 'Collins', 'LABEL'] = 3
	concated.loc[concated['author'] == 'Doyle', 'LABEL'] = 4
	concated.loc[concated['author'] == 'Montgomery', 'LABEL'] = 5
	concated.loc[concated['author'] == 'Stoker', 'LABEL'] = 6
	concated.loc[concated['author'] == 'Twain', 'LABEL'] = 7
	print(concated)

	print(concated['LABEL'][:10])
	labels = to_categorical(concated['LABEL'], num_classes=8)
	print(labels)
	print(labels[:10])
	if 'author' in concated.keys():
	    concated.drop(['author'], axis=1)
    
    
	n_most_common_words = 3000
	max_len = 130
	tokenizer = Tokenizer(num_words=n_most_common_words, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
	tokenizer.fit_on_texts(concated['text'].values)
	sequences = tokenizer.texts_to_sequences(concated['text'].values)
	word_index = tokenizer.word_index
	print('Found %s unique tokens.' % len(word_index))
	
	X = pad_sequences(sequences, maxlen=max_len)



	X_train, X_test, y_train, y_test = train_test_split(X , labels, test_size=0.25, random_state=42)




	epochs = 1
	emb_dim = 128
	batch_size = 10
	labels[:2]
	
	print((X_train.shape, y_train.shape, X_test.shape, y_test.shape))

	model = Sequential()
	model.add(Dense(activation="relu", input_dim=X_train.shape[1], units=1, kernel_initializer="uniform"))
	# Adding the output layer 
	model.add(Dense(8,activation="sigmoid"))
		

	# Compiling the NN
	model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
	
	print(model.summary())
	history = model.fit(X_train, y_train, epochs=100, batch_size=10,validation_split=0.2,callbacks=[EarlyStopping(monitor='val_loss',patience=7, min_delta=0.0001)])


	accr = model.evaluate(X_test,y_test)
	pred = model.predict(X_test[:10])

	print(pred)
	#labels = ["Alcott", "Austen", "Bronte", "Collins","Doyle","Montgomery", "Stoker","Twain"]
	#r=pred[0]
	#print(r)
	print(y_test[:10])
	#print(r, labels[np.argmax(r)])
	#print('Test set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}'.format(accr[0],accr[1]))


	#txt = ["Which was not quite a correct statement, by the way"]
	seq = tokenizer.texts_to_sequences(input)
	padded = pad_sequences(seq, maxlen=max_len)
	
	pred = model.predict(padded)
	labels = ["Alcott", "Austen", "Bronte", "Collins","Doyle","Montgomery", "Stoker","Twain"]
	print(pred, labels[np.argmax(pred)])
	return labels[np.argmax(pred)]

