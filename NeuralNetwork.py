import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import accuracy_score
import keras 
from keras.models import Sequential
from keras.layers import Dense 
from keras.models import load_model
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from keras.callbacks import EarlyStopping
import numpy as np	
	
def process(path):
	adata=["Alcott", "Austen", "Bronte", "Collins","Doyle","Montgomery", "Stoker","Twain"]
	data = pd.read_csv(path, encoding="utf-8")
	print(data.head())
	#data[['author']] = data[['author']].replace(["Alcott", "Austen", "Bronte", "Collins","Doyle","Montgomery", "Stoker","Twain"], [0,1,2,3,4,5,6,7])
	data=data[:4000]
	print(data)
	
	# Create feature (text) and label (author) lists
	x = data['text'].values
	y = data['author'].values

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

	vectorizer = TfidfVectorizer()
	data_vec = vectorizer.fit_transform(concated['text'].values)
	df = pd.DataFrame(data_vec.toarray())

	print(df)

	# Standardizing the features
	scaler1 = StandardScaler()
	
	x = scaler1.fit_transform(df)
	
	from sklearn.decomposition import PCA
	pca = PCA(n_components=8)
	principalComponents = pca.fit_transform(x)
	principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2','principal component 3','principal component 4','principal component 5','principal component 6','principal component 7','principal component 8'])
	finalDf = pd.concat([principalDf, data[['author']]], axis = 1)

	fig = plt.figure(figsize = (8,8))
	ax = fig.add_subplot(1,1,1) 
	ax.set_xlabel('Principal Component 1', fontsize = 15)
	ax.set_ylabel('Principal Component 2', fontsize = 15)
	ax.set_title('2 component PCA', fontsize = 20)
	targets = ["Alcott", "Austen", "Bronte", "Collins","Doyle","Montgomery", "Stoker","Twain"]
	colors = ['r', 'g', 'b','c','r','y','m','k']
	for target, color in zip(targets,colors):
	    indicesToKeep = finalDf['author'] == target
	    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
	               , finalDf.loc[indicesToKeep, 'principal component 2']
	               , c = color
	               , s = 50)
	ax.legend(targets)
	ax.grid()
	plt.pause(5)
	plt.show(block=False)
	plt.close()

	x = data['text'].values
	y = data['author'].values


	# test_size: what proportion of original data is used for test set
	X_train, X_test, y_train, y_test = train_test_split(df, labels, test_size=1/7.0, random_state=0)

	
	scaler = StandardScaler()
	# Fit on training set only.
	scaler.fit(X_train)
	# Apply transform to both the training set and the test set.
	X_train = scaler.transform(X_train)
	X_test = scaler.transform(X_test)


	from sklearn.decomposition import PCA
	# Make an instance of the Model
	pca = PCA(.95)

	pca.fit(X_train)

	X_train = pca.transform(X_train)
	X_test = pca.transform(X_test)


	print(X_train.shape)

	model = Sequential()
	model.add(Dense(activation="relu", input_dim=X_train.shape[1], units=1, kernel_initializer="uniform"))
	# Adding the output layer 
	model.add(Dense(8,activation="sigmoid"))
		
	
	# Compiling the NN
	model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
	
	print(model.summary())
	history = model.fit(X_train, y_train, epochs=100, batch_size=10,validation_split=0.2,callbacks=[EarlyStopping(monitor='val_loss',patience=7, min_delta=0.0001)])

	
	# Predicting the Test set results
	y_pred = model.predict(X_test)
	print(y_pred)
	print("ytest")
	print(y_test)
	# save the model for later use
	model.save('model.h5')
	print(y_pred)
	labels = ["Alcott", "Austen", "Bronte", "Collins","Doyle","Montgomery", "Stoker","Twain"]
	for v in y_pred:
		print(v, labels[np.argmax(v)])

	result2=open("results/resultNeuralNetwork.csv","w")
	result2.write("ID,Predicted Value" + "\n")
	for j in range(len(y_pred)):
	    m=labels[np.argmax(y_pred[j])]
	    result2.write(str(j+1) + "," + str(m) + "\n")
	result2.close()
	
	mse=mean_squared_error(y_test, y_pred)
	mae=mean_absolute_error(y_test, y_pred)
	r2=r2_score(y_test, y_pred)
	ac = model.evaluate(X_test,y_test)
	ac=ac[1]
	
	
	print("---------------------------------------------------------")
	print("MSE VALUE FOR Neural Network IS %f "  % mse)
	print("MAE VALUE FOR Neural Network IS %f "  % mae)
	print("R-SQUARED VALUE FOR Neural Network IS %f "  % r2)
	rms = np.sqrt(mean_squared_error(y_test, y_pred))
	print("RMSE VALUE FOR Neural Network IS %f "  % rms)
	#ac=accuracy_score(y_test,y_pred.round())
	print ("ACCURACY VALUE Neural Network IS %f" % ac)
	print("---------------------------------------------------------")
	
	result2=open('results/NNMetrics.csv', 'w')
	result2.write("Parameter,Value" + "\n")
	result2.write("MSE" + "," +str(mse) + "\n")
	result2.write("MAE" + "," +str(mae) + "\n")
	result2.write("R-SQUARED" + "," +str(r2) + "\n")
	result2.write("RMSE" + "," +str(rms) + "\n")
	result2.write("ACCURACY" + "," +str(ac) + "\n")
	result2.close()
	
	
	df =  pd.read_csv('results/NNMetrics.csv')
	acc = df["Value"]
	alc = df["Parameter"]
	colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
	explode = (0.1, 0, 0, 0, 0)  
	
	fig = plt.figure()
	plt.bar(alc, acc, align='center', alpha=0.5,color=colors)
	plt.xlabel('Parameter')
	plt.ylabel('Value')
	plt.title(' Neural Network Metrics Value')
	fig.savefig('results/NNMetricsValue.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()
