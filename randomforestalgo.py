import enum
from random import random
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
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor

"""
what is random forest algo ?
main daatset mathi randomly thoda dataaset banavana but bija nava banavela detaset ni size main dataset karta ochi hovi joiye
ane a bdha dataset na decision tree banavi ne te badaha mathi value find karcvani ane 
temathi j value vadhare var avi hoy te value ne predicted value manvani 
"""

# data = load_breast_cancer()

# df = pd.DataFrame(np.c_[data.data,data.target],columns=[list(data.feature_names)+['target']])

# X = df.iloc[:,0:-1]
# y = df.iloc[:,-1]

# X_train,X_test,y_train,y_test =  train_test_split(X,y,test_size=0.2,random_state=51)

# randomcls = RandomForestClassifier(n_estimators=100,criterion='gini')

# randomcls.fit(X_train,y_train)
# print(randomcls.score(X_test,y_test))
# # 0.9473684210526315

# y_pred = randomcls.predict(X_test)

# print(y_pred)

# [1. 1. 1. 1. 1. 1. 1. 0. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 0. 1.
#  1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 0. 1. 0. 0. 0.
#  1. 1. 1. 1. 0. 1. 0. 1. 0. 0. 1. 1. 1. 1. 1. 0. 1. 1. 0. 1. 1. 1. 1. 1.
#  0. 0. 1. 0. 0. 0. 1. 0. 0. 1. 1. 0. 0. 1. 1. 1. 0. 1. 0. 1. 1. 1. 1. 1.
#  1. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1.]


# -------------------------------------------------------------------------

path = r"https://drive.google.com/uc?export=download&id=1xxDtrZKfuWQfl-6KA9XEd_eatitNPnkB"
df = pd.read_csv(path)

X = df.drop('price',axis=1)
y = df['price']

X_train,X_test,y_train,y_test =  train_test_split(X,y,test_size=0.2,random_state=51)

randomcls = RandomForestRegressor(n_estimators=500,criterion='mse')

randomcls.fit(X_train,y_train)
print(randomcls.score(X_test,y_test))
# 0.8984272739875576

y_pred = randomcls.predict(X_test)

print(y_pred)











































