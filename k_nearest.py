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


# k nearest neighbor classifier

data = load_breast_cancer()
df = pd.DataFrame(np.c_[data.data,data.target],columns=[list(data.feature_names)+['target']])

X = df.iloc[:,0:-1]
y= df.iloc[:,-1]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=51) 


classifier =  KNeighborsClassifier(n_neighbors=5)

classifier.fit(X_train,y_train)

print(classifier.score(X_train,y_train))

# 0.9516483516483516

print(classifier.predict(X_test))
# [1. 1. 1. 1. 1. 1. 1. 0. 0. 0. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1.
#  1. 1. 0. 1. 1. 1. 0. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 0. 1. 0. 0. 0.
#  1. 1. 1. 1. 0. 1. 0. 1. 0. 0. 1. 1. 1. 1. 1. 0. 1. 1. 0. 1. 1. 0. 1. 1.
#  0. 0. 1. 0. 0. 0. 1. 0. 0. 1. 0. 0. 0. 1. 1. 1. 0. 1. 0. 1. 1. 1. 1. 1.
# #  1. 0. 0. 0. 1. 1. 1. 0. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1.]


# ------------------------------------------------------------
# k nearest neighbor regresion


path = r"https://drive.google.com/uc?export=download&id=1xxDtrZKfuWQfl-6KA9XEd_eatitNPnkB"
df = pd.read_csv(path)
print(df.tail)

# DATA NE SPLITE KARVANO

X = df.drop('price',axis=1)
y = df['price']

X_train,X_test,y_train,y_test =  train_test_split(X,y,test_size=0.2,random_state=51)


regressor  = KNeighborsRegressor(n_neighbors=5)
print("regressionnnnnnnnnnnnnnn")
regressor.fit(X_train,y_train)
print(regressor.score(X_test,y_test))
# 0.8858214084886539

x_pred = regressor.predict(X_test)
print(x_pred)


















































