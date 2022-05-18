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



#103 -------------------------------------------------------------------------------------------------
# support vector regression machine algorythm

path = r"https://drive.google.com/uc?export=download&id=1xxDtrZKfuWQfl-6KA9XEd_eatitNPnkB"
df = pd.read_csv(path)
print(df.tail)

# DATA NE SPLITE KARVANO

X = df.drop('price',axis=1)
y = df['price']

X_train,X_test,y_train,y_test =  train_test_split(X,y,test_size=0.2,random_state=51)

print(X_train)

#       bath  balcony  total_sqft_int  ...  location_Domlur  location_Mahadevpura  location_Tumkur Road
# 7112   5.0      2.0          2500.0  ...                0                     0                     0
# 2169   2.0      0.0           995.0  ...                0                     0                     0
# 47     2.0      2.0          1180.0  ...                0                     0                     0
# 446    2.0      1.0          1450.0  ...                0                     0                     0
# 2650   2.0      1.0          1197.0  ...                0                     0                     0
# ...    ...      ...             ...  ...              ...                   ...                   ...
# 6672   2.0      1.0          1246.0  ...                0                     0                     0
# 1733   2.0      1.0          1010.0  ...                0                     0                     0
# 1760   2.0      2.0          1080.0  ...                0                     0                     0
# 485    2.0      2.0           982.0  ...                0                     0                     0
# 2105   2.0      1.0          1000.0  ...                0                     0                     0


print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)
# (5696, 107) (1424, 107) (5696,) (1424,)

# support vector machine no use karvo hoy tyare tene featurescale thayelo data devo important che 
# standardsaler thi data ne feature scaling karsu

sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

print("X_train",X_train)
print("x_test",X_test)

# featurescaling ma data a -1 to 1 ni vacchhe set thay jay

#  [-1.59851179  0.55008644 -1.03304852 ... -0.05630391 -0.05630391
#   -0.05138463]
#  [-0.44274597 -0.74630813 -0.38550655 ... -0.05630391 -0.05630391
#   -0.05138463]
#  [-0.44274597 -2.0427027   0.12917322 ... -0.05630391 -0.05630391
#   -0.05138463]]

"""
have support vector regression machine a lgorythem machine nu model banavanu
ane train karvamnu

support vector machine ne import karvanu
"""

svr_rbf = SVR(kernel='rbf')

svr_rbf.fit(X_train, y_train)
print(svr_rbf.score(X_test, y_test))
# 0.20638035840828173

# 20% j accricy api che to a model a good model nathi

# kernel ma change karine check karvamni accuricy good ave che k nai 

svr_linear = SVR(kernel='linear')
svr_linear.fit(X_train, y_train)
print(svr_linear.score(X_test, y_test))
# 0.7962656700653191

# 79% j accricy api che to a model a good che

# kernel ma change karine check karvamni accuricy good ave che k nai 

svr_poly = SVR(kernel='poly')
svr_poly.fit(X_train, y_train)
print(svr_poly.score(X_test, y_test))
# 0.3039932069927379

# 30% j accricy api che to a model a good nathi


# polynomial kernel ma degree vadhari ne check karo k accurycy su ave ch
 
svr_poly = SVR(kernel='poly',degree=2)
svr_poly.fit(X_train, y_train)
print(svr_poly.score(X_test, y_test))
# 0.18266215211874637

# 18% j accricy api che to a model a good nathi


y_pred = svr_linear.predict(X_test)
print(y_pred)

# have root mean square errorr find karvamate

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("MMMMMMMMM",mse)
# MMMMMMMMM 4093.6210385966133
print("Rmse",rmse)
# Rmse 63.98141166461251


# 104-------------------------------------------------------------------------------------

"""
linear support vector classifier for(lsvm)

supervised machine algo ma be type hoy che 
1) clasification
2) regression 

jyare continuous value no problem hoy tyare regression no use thay
ane classifictaion karvu pade tyare classification tec no use thay

-- support vector machine a banne type na problem ne solve kare che.

-- support vector machine a supervised learning no powerfull algorythem che  


"""

data = load_breast_cancer()

print(data.data)
# [[1.799e+01 1.038e+01 1.228e+02 ... 2.654e-01 4.601e-01 1.189e-01]
#  [2.057e+01 1.777e+01 1.329e+02 ... 1.860e-01 2.750e-01 8.902e-02]
#  [1.969e+01 2.125e+01 1.300e+02 ... 2.430e-01 3.613e-01 8.758e-02]
#  ...
#  [1.660e+01 2.808e+01 1.083e+02 ... 1.418e-01 2.218e-01 7.820e-02]
#  [2.060e+01 2.933e+01 1.401e+02 ... 2.650e-01 4.087e-01 1.240e-01]
#  [7.760e+00 2.454e+01 4.792e+01 ... 0.000e+00 2.871e-01 7.039e-02]]

print(data.feature_names) 
# ['mean radius' 'mean texture' 'mean perimeter' 'mean area'
#  'mean smoothness' 'mean compactness' 'mean concavity'
#  'mean concave points' 'mean symmetry' 'mean fractal dimension'
#  'radius error' 'texture error' 'perimeter error' 'area error'
#  'smoothness error' 'compactness error' 'concavity error'
#  'concave points error' 'symmetry error' 'fractal dimension error'
#  'worst radius' 'worst texture' 'worst perimeter' 'worst area'
#  'worst smoothness' 'worst compactness' 'worst concavity'
#  'worst concave points' 'worst symmetry' 'worst fractal dimension']

print(data.target)
# [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
#  1 0 0 0 0 0 0 0 0 1 0 1 1 1 1 1 0 0 1 0 0 1 1 1 1 0 1 0 0 1 1 1 1 0 1 0 0
#  1 0 1 0 0 1 1 1 0 0 1 0 0 0 1 1 1 0 1 1 0 0 1 1 1 0 0 1 1 1 1 0 1 1 0 1 1
#  1 1 1 1 1 1 0 0 0 1 0 0 1 1 1 0 0 1 0 1 0 0 1 0 0 1 1 0 1 1 0 1 1 1 1 0 1
#  1 1 1 1 1 1 1 1 0 1 1 1 1 0 0 1 0 1 1 0 0 1 1 0 0 1 1 1 1 0 1 1 0 0 0 1 0
#  1 0 1 1 1 0 1 1 0 0 1 0 0 0 0 1 0 0 0 1 0 1 0 1 1 0 1 0 0 0 0 1 1 0 0 1 1
#  1 0 1 1 1 1 1 0 0 1 1 0 1 1 0 0 1 0 1 1 1 1 0 1 1 1 1 1 0 1 0 0 0 0 0 0 0
#  0 0 0 0 0 0 0 1 1 1 1 1 1 0 1 0 1 1 0 1 1 0 1 0 0 1 1 1 1 1 1 1 1 1 1 1 1
#  1 0 1 1 0 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 0 1 0 1 1 1 1 0 0 0 1 1
#  1 1 0 1 0 1 0 1 1 1 0 1 1 1 1 1 1 1 0 0 0 1 1 1 1 1 1 1 1 1 1 1 0 0 1 0 0
#  0 1 0 0 1 1 1 1 1 0 1 1 1 1 1 0 1 1 1 0 1 1 0 0 1 1 1 1 1 1 0 1 1 1 1 1 1
#  1 0 1 1 1 1 1 0 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 0 1 1 1 1 1 0 1 1
#  0 1 0 1 1 0 1 0 1 1 1 1 1 1 1 1 0 0 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 0 1
#  1 1 1 1 1 1 0 1 0 1 1 0 1 1 1 1 1 0 0 1 0 1 0 1 1 1 1 1 0 1 1 0 1 0 1 0 0
#  1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#  1 1 1 1 1 1 1 0 0 0 0 0 0 1]

print(data.target_names)
# ['malignant' 'benign']


#  numpy array ne dataframe ma convert karva mate 

df = pd.DataFrame(np.c_[data.data,data.target],columns=[list(data.feature_names)+['target']])

print(df.head())
#   mean radius mean texture mean perimeter  ... worst symmetry worst fractal dimension target
# 0       17.99        10.38         122.80  ...         0.4601                 0.11890    0.0
# 1       20.57        17.77         132.90  ...         0.2750                 0.08902    0.0
# 2       19.69        21.25         130.00  ...         0.3613                 0.08758    0.0
# 3       11.42        20.38          77.58  ...         0.6638                 0.17300    0.0
# 4       20.29        14.34         135.10  ...         0.2364                 0.07678    0.0

print(df.shape)
# (569, 31)

# a dta frame ne x ane y ma split karyo

X = df.iloc[:,0:-1]
y = df.iloc[:,-1]

X_train,X_test,y_train,y_test =  train_test_split(X,y,test_size=0.2,random_state=51)

classification_rbf = SVC(kernel='rbf')
classification_rbf.fit(X_train,y_train)

print(classification_rbf.score(X_test,y_test))
# 0.9035087719298246

# featuire scaling karine model ne train kaarsu

sc = StandardScaler()

sc.fit(X_train)

X_tarin_sc = sc.transform(X_train)
X_test_sc = sc.transform(X_test)

classification_rbf_2 = SVC(kernel='rbf')
classification_rbf_2.fit(X_tarin_sc,y_train)
print(classification_rbf_2.score(X_test_sc,y_test)) 
# 0.9473684210526315


classification_poly = SVC(kernel='poly',degree=2)
classification_poly.fit(X_tarin_sc,y_train)
print(classification_poly.score(X_test_sc,y_test)) 
# 0.7982456140350878


classification_linear = SVC(kernel='linear',degree=2)
classification_linear.fit(X_tarin_sc,y_train)
print(classification_linear.score(X_test_sc,y_test)) 
# 0.9473684210526315


























































































































