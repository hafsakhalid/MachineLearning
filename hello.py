import sys 
import numpy as np 
import matplotlib.pyplot as mpl 
import csv 
import pandas as pd 


with open ('winequality-red.csv', 'r') as f: 
	wines = list(csv.reader(f, delimiter=';'))
	wines = np.array(wines[1:], dtype = np.float)
	quality = np.array(wines[:,11], dtype = np.float) 
	df = pd.DataFrame(quality, columns = ['quality'])
	df.loc[df.quality <=5, 'binary classification'] = 0 
	df.loc[df.quality  >5, 'binary classification'] = 1
	numpy_matrix = df.as_matrix()
	#print(numpy_matrix)
	binaryclassification = (numpy_matrix[:,1])
	#print(binaryclassification)
	#print(binaryclassification.shape)
	#dataset = np.insert(wines, 12, binaryclassification, axis = 1)
	#print(dataset)
	#this is the array of the 1's and 0's 
	#y = []
	#for x in dataset:
		#y.append(x[12])
	#print(y)
	#print(wines)
	#print(y.shape)


class LinearRegression: 

	y = binaryclassification
	print(y)
	#print(y.shape)
	X = wines 
	print(X)
	w = np.zeros((12, 1), dtype=np.int)
	print(w)


	def fit (X, y, w): 
		a = np.dot(w, x)
		sig = 1/(1 + np.exp(-a))
		gradient = np.dot(X.T, (sig - y)) / x.shape[1]
		w = w - .1 * gradient
		return 



    
    
		
	
	#def sigmoid(w, x):
		#a = np.dot(w, x)
		#return 1/(1 + np.exp(-a))

	def loss(s, y):
		arr = []
		for x in y:
			arr.append(-y * np.log(s) - (1 - y) * np.log(1 - h))
		return np.mean(arr)

	def graddes(w, x, y):
		sum = 0
		for i in range(y.size):
			sum += np.dot(x[i], (y[i] - np.dot(w, x[i])))
		return sum
	
	def update(w, a, g):
		return w - (a * g)







	


   
   
    

