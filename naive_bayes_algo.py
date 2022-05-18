import enum
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.metrics import mean_squared_error 
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR,SVC
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB

# k nearest neighbor classifier

data = load_breast_cancer()
df = pd.DataFrame(np.c_[data.data,data.target],columns=[list(data.feature_names)+['target']])

X = df.iloc[:,0:-1]
y= df.iloc[:,-1]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=51) 


classifier =  GaussianNB()

classifier.fit(X_train,y_train)

print(classifier.score(X_train,y_train))
# 0.9538461538461539

# -------------------------------------------------
# MultinomialNB classifier

classifier =  MultinomialNB()

classifier.fit(X_train,y_train)

print(classifier.score(X_train,y_train))
# 0.8989010989010989


# ------------------------------------------------------------------------------

# BernoulliNB classifier 

classifier =  BernoulliNB()

classifier.fit(X_train,y_train)

print(classifier.score(X_train,y_train))
# 0.6175824175824176









