from __future__ import print_function
import numpy as np 
import os
from sklearn import datasets,linear_model


# link data file
data_file = str(os.getcwd()) + '\\data\\Pearson.txt' 


x = []  #heigh of father 
y= []   #heigh of son

f = open(data_file,'r')
f.readline()    #Read first line
#Get heigh from line 2 to final
for line in f:
    heigh =list(map(float,line.split('\t')))
    x.append(heigh[0])
    y.append(heigh[1])

#Convert list to array
X = np.array(x)[np.newaxis] #khi co np.newaxis = T
X = X.T
Y = np.array(y)[np.newaxis]
Y= Y.T

#Building Xbar
one = np.ones((X.shape[0],1))
Xbar = np.concatenate((one,X),axis=1)
A = np.dot(Xbar.T,Xbar)
b = np.dot(Xbar.T,Y)
w = np.dot(np.linalg.pinv(A),b)
#Cong thu tinh w = (X*X.T)^-1 *X*y
print("Ket qua tu tinh: w0= ",w[0]," w1= ",w[1])



#Dung thu vien.
regr = linear_model.LinearRegression()
regr.fit(X,Y)
print("Ket qua dung thu vien: w0= " ,regr.intercept_ ," w1=" ,regr.coef_[0])
