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
import numpy as np

def process(path):
	data = pd.read_csv(path, encoding="utf-8")
	adata=["Alcott", "Austen", "Bronte", "Collins","Doyle","Montgomery", "Stoker","Twain"]
	
	print(data.head())

	data=data[:4000]
	print(data)

	# Create feature (text) and label (author) lists
	x = data['text'].values
	y = data['author'].values


	vectorizer = TfidfVectorizer()
	data_vec = vectorizer.fit_transform(x)
	df = pd.DataFrame(data_vec.toarray())

	print(df)

	# Standardizing the features
	x = StandardScaler().fit_transform(df)
	
	from sklearn.decomposition import PCA
	pca = PCA(n_components=8)
	principalComponents = pca.fit_transform(x)
	principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2','principal component 3','principal component 4','principal component 5','principal component 6','principal component 7','principal component 8'])
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

	data[['author']] = data[['author']].replace(["Alcott", "Austen", "Bronte", "Collins","Doyle","Montgomery", "Stoker","Twain"], [0,1,2,3,4,5,6,7])
	x = data['text'].values
	y = data['author'].values


	# test_size: what proportion of original data is used for test set
	train_img, test_img, train_lbl, test_lbl = train_test_split(df, y, test_size=1/7.0, random_state=0)

	scaler = StandardScaler()
	# Fit on training set only.
	scaler.fit(train_img)
	# Apply transform to both the training set and the test set.
	train_img = scaler.transform(train_img)
	test_img = scaler.transform(test_img)


	from sklearn.decomposition import PCA
	# Make an instance of the Model
	pca = PCA(.95)

	pca.fit(train_img)

	train_img = pca.transform(train_img)
	test_img = pca.transform(test_img)

	print(train_img.shape)

	

	# all parameters not specified are set to their defaults
	# default solver is incredibly slow which is why it was changed to 'lbfgs'
	logisticRegr = LogisticRegression(solver = 'lbfgs')

	logisticRegr.fit(train_img, train_lbl)

	# Predict for One Observation (image)
	y_pred=logisticRegr.predict(test_img)
	print(y_pred)
	
	result2=open("results/resultLogisticRegression.csv","w")
	result2.write("ID,Predicted Value" + "\n")
	for j in range(len(y_pred)):
	    result2.write(str(j+1) + "," + str(adata[y_pred[j]]) + "\n")
	result2.close()
	
	mse=mean_squared_error(test_lbl, y_pred)
	mae=mean_absolute_error(test_lbl, y_pred)
	r2=r2_score(test_lbl, y_pred)
	
	
	print("---------------------------------------------------------")
	print("MSE VALUE FOR Logistic Regression IS %f "  % mse)
	print("MAE VALUE FOR Logistic Regression IS %f "  % mae)
	print("R-SQUARED VALUE FOR Logistic Regression IS %f "  % r2)
	rms = np.sqrt(mean_squared_error(test_lbl, y_pred))
	print("RMSE VALUE FOR Logistic Regression IS %f "  % rms)
	ac=accuracy_score(test_lbl,y_pred)*100
	print ("ACCURACY VALUE Logistic Regression IS %f" % ac)
	print("---------------------------------------------------------")
	
	result2=open('results/LogisticRegressionMetrics.csv', 'w')
	result2.write("Parameter,Value" + "\n")
	result2.write("MSE" + "," +str(mse) + "\n")
	result2.write("MAE" + "," +str(mae) + "\n")
	result2.write("R-SQUARED" + "," +str(r2) + "\n")
	result2.write("RMSE" + "," +str(rms) + "\n")
	result2.write("ACCURACY" + "," +str(ac) + "\n")
	result2.close()
	
	
	df =  pd.read_csv('results/LogisticRegressionMetrics.csv')
	acc = df["Value"]
	alc = df["Parameter"]
	colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
	explode = (0.1, 0, 0, 0, 0)  
	
	fig = plt.figure()
	plt.bar(alc, acc, align='center', alpha=0.5,color=colors)
	plt.xlabel('Parameter')
	plt.ylabel('Value')
	plt.title(' Logistic Regression Metrics Value')
	fig.savefig('results/LogisticRegressionMetricsValue.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()

	# Predict for One Observation (image)
	print(logisticRegr.predict(test_img[0:10]))

	print(logisticRegr.score(test_img, test_lbl))

