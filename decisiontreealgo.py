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

# 106-----------------------------------------------------------------------

data = load_breast_cancer()
df = pd.DataFrame(np.c_[data.data,data.target],columns=[list(data.feature_names)+['target']])

X = df.iloc[:,0:-1]
y= df.iloc[:,-1]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=51) 


# with gini 
classifier = DecisionTreeClassifier(criterion='gini')
classifier.fit(X_train,y_train)
print(classifier.score(X_test,y_test))
# 0.9385964912280702


# with entropy 
classifier_entopy = DecisionTreeClassifier(criterion='entropy')
classifier_entopy.fit(X_train,y_train)
print(classifier_entopy.score(X_test,y_test))
# 0.9210526315789473


# --------------------------------------------------------
"""with feature calling 
but ahi decision tree algo ne feature scale karvo jaruri nathi
"""
sc  = StandardScaler()
sc.fit(X_train)

X_train_sc = sc.transform(X_train)
X_test_sc = sc.transform(X_test)

classifier_sc = DecisionTreeClassifier(criterion='gini')
classifier_sc.fit(X_train_sc,y_train)
print("CCCCCCCCCC",classifier_sc.score(X_test_sc,y_test))
# CCCCCCCCCC 0.9298245614035088


classifier_sc = DecisionTreeClassifier(criterion='entropy')
classifier_sc.fit(X_train_sc,y_train)
print("EEEEEEEEE",classifier_sc.score(X_test_sc,y_test))
# EEEEEEEEE 0.9210526315789473

# ---------------------------------------------------------------------------------

"""
    decision tree regression algorythem
    
"""

path = r"https://drive.google.com/uc?export=download&id=1xxDtrZKfuWQfl-6KA9XEd_eatitNPnkB"
df = pd.read_csv(path)
print(df.tail)

# DATA NE SPLITE KARVANO

X = df.drop('price',axis=1)
y = df['price']

X_train,X_test,y_train,y_test =  train_test_split(X,y,test_size=0.2,random_state=51)

regressor = DecisionTreeRegressor(criterion='mse')

regressor.fit(X_train,y_train)

print(regressor.score(X_test,y_test))
# 0.889761478519506

x_pred = regressor.predict(X_test)
print(x_pred)
# [ 84.    39.95 120.   ...  32.64  62.5  171.  ]









































    