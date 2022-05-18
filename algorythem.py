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


# https://www.opcito.com/blogs/integrating-django-with-salesforce

"""
what is train test split function
train_test_split() a sklearn no ak class che te help kare data che tene dataset ma split karva mate.
x_train,x_test,y_train,y_test
x mins independent variable, 
y mins dependent variable
"""

df = sns.load_dataset("titanic")

df2 = df[["survived","pclass","age","parch"]]

df3 = df2.fillna(df2.mean())

print(df3.head())

#    survived  pclass   age  parch
# 0         0       3  22.0      0
# 1         1       1  38.0      0
# 2         1       3  26.0      0
# 3         1       1  35.0      0
# 4         0       3  35.0      0

# a data frame ne x ane y ma mins k dependent ane independent variable ma spilit karvna 

X = df3.drop("survived",axis=1)

y = df3["survived"]

# X capital ma lakhvano matlb mashine learning ma matrics kahevay
# y ne small ma lakhvama ave minsk y vector che mashine learning ma vector ne small define karvama ave 

print(X.shape, y.shape)
# (891, 3) (891,)

# have a main dataset ne train ane test dataset ma split karvama ave 

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=51)

# random_state a pattern ma j badhivakhte data split thay jethi data badhi  vakhte sarkho ave tena nmate random_state no use thy 

print(X_train.shape)
# (712, 3)
print(X_test.shape)
# (179, 3)
print(y_train.shape)
# (712,)
print(y_test.shape)
# (179,)
print(X_train)

# train_test_split randomly data ne select kare train k test mate tethi game te inex ni row ne select thay 

#      pclass        age  parch
# 770       3  24.000000      0
# 152       3  55.500000      0
# 731       3  11.000000      0
# 775       3  18.000000      0
# 324       3  29.699118      2
# ..      ...        ...    ...
# 528       3  39.000000      0
# 709       3  29.699118      1
# 736       3  48.000000      3
# 485       3  29.699118      1
# 57        3  28.500000      0

# ---------------------------------------------------------------------
"""
    linear regression   
        
simple linear regression ?
apdi pase x data ane y data che to apde mcmodel ne train karsu       
ama single dependent ane single independent variable hoy      
    
multiple linear regression?
independent feture par thi value dependent karvani

         
"""

# supervised mashinelearning algorythm

path = r"https://drive.google.com/uc?export=download&id=1xxDtrZKfuWQfl-6KA9XEd_eatitNPnkB"

# pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)

df = pd.read_csv(path)

print(df)

#       bath  balcony   price  ...  location_Domlur  location_Mahadevpura  location_Tumkur Road
# 0      3.0      2.0  150.00  ...                0                     0                     0
# 1      3.0      3.0  149.00  ...                0                     0                     0
# 2      3.0      2.0  150.00  ...                0                     0                     0
# 3      2.0      2.0   40.00  ...                0                     0                     0
# 4      2.0      2.0   83.00  ...                0                     0                     0
# ...    ...      ...     ...  ...              ...                   ...                   ...
# 7115   3.0      2.0  325.00  ...                0                     0                     0
# 7116   3.0      1.0   84.83  ...                0                     0                     0
# 7117   2.0      1.0   48.00  ...                0                     0                     0
# 7118   2.0      1.0   55.00  ...                0                     0                     0
# 7119   2.0      1
#  .0   78.00  ...                0                     0                     0


print(df.isnull().sum().sum())
# 0

# have a a data ne split karvano depebndent ane independent

# price upar prediction karvanu che tethi tene dependent var kahevay to tene remove karvama ave X ma only independent var j hoy

X = df.drop("price",axis=1)
y = df["price"]

print(X.shape)
# (7120, 107)

print(y.shape)
# (7120,)

X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2,random_state=51)

print(X_train.shape)
# (5696, 107)

print(X_test.shape)
# (1424, 107)

print(y_train.shape)
# (5696,)

print(y_test.shape)
# (142 4,)

# feature scaling

sc = StandardScaler()
sc.fit(X_train)

X_train = sc.transform(X_train)

X_test = sc.transform(X_test)

print(X_train)

print(X_test)

# linear regration

lr = LinearRegression()

lr.fit(X_train,y_train)

print(lr.coef_)
# [-5.70206143e+00 -1.25679916e+00  8.27341833e+01 -1.44906911e+01
#   5.75662723e+01  1.88468905e-01 -1.72593897e+00 -4.51058311e+00
#  -2.22589244e+00 -4.28978455e+00 -2.44590976e+00  5.40246226e-01
#  -1.03633400e+00  1.43064873e+00 -6.25029424e-02 -1.51548783e+00
#  -2.14422789e-01  2.16244155e+00 -1.48710228e+00  1.95250816e+00
#  -3.10761125e+00 -1.28138668e+00 -1.01367155e+00  1.37968545e-02
#   1.10383858e+00  1.26497611e+00 -3.52405517e+00 -1.21398741e+00
#  -5.04622019e-01  1.46299181e+00 -5.50064233e-01 -8.46468162e-02
#   6.84882188e-01 -1.39849820e+00 -1.94761710e-02 -1.57716300e+00
#   4.20886278e-01  8.03443207e-01  2.99182164e+00  3.86430413e-03
#   1.05037261e-01  2.89115612e-01 -3.16916626e-01  1.05625868e+00
#  -1.39649279e+00 -3.10533604e+00  1.01764011e-01 -7.49672917e-02
#  -8.03271555e-01 -1.27061856e+00 -8.54046164e-01  2.64566484e-01
#   9.10688839e-01 -8.23059458e-01 -9.07215234e-01  1.22059216e+00
#   2.11418894e+00 -5.38187400e-01 -1.32164338e+00 -8.28349340e-01
#   1.28167980e+00 -1.92911295e-01  6.65824485e-02  3.65563139e-02
#  -1.85069853e+00  1.49068024e+00 -9.57964753e-01 -9.36110163e-01
#  -7.45634897e-01  7.22643165e-02 -6.79260144e-01 -1.70853833e-01
#  -1.72288643e+00 -1.15833746e+00  5.78931788e-01  1.37836966e+00
#  -1.14424496e+00  3.96188294e-01 -6.08013157e-01 -2.20959218e+00
#   3.45270810e-01  1.01747431e-03  1.06563895e-01  3.04728530e+00
#   2.09496392e+00 -8.13481923e-01 -4.18437282e-01  2.30993396e+00
#   3.31858800e-02  8.07865914e-02  5.37064987e-02  1.55347699e+00
#   8.13889657e-01 -1.14636462e+00  3.41805788e-01 -8.28022037e-01
#   1.68897360e+00  2.97657524e-01  9.59437517e-01  4.57297702e-01
#  -2.22729515e-01 -1.48290835e+00 -6.26342867e-01  5.86538254e-01
#  -1.78547310e+00  2.19020231e-01 -3.45032599e-01]

print(lr.intercept_)
# 95.0802729985955

# predict the value of home and test

print(X_test[0,:])
# x_test ni 0 number ni row ni badhi 107 column no data 

# [ 0.71301986  0.0112734   0.30202307  0.65677518 -0.48064341 -1.7385623
#   2.11587407 -0.25430867  0.51007548 -0.18373025 -0.16389438 -0.1473229
#  -0.13023539 -0.12812824 -0.12598816 -0.12454231 -0.12953656 -0.12381344
#  -0.12010681 -0.11551113 -0.10992018 -0.10909925 -0.10660036 -0.11234866
#  -0.09315135 -0.08618799 -0.08923672 -0.09023078 -0.08721571 -0.09023078
#  -0.08721571 -0.08195215 -0.08195215 -0.07633675 -0.0751646  -0.08085949
#  -0.0739743  -0.07975227 -0.07153563 -0.0751646  -0.0677166  -0.08085949
#  -0.07153563 -0.07862985 -0.0751646  -0.07862985 -0.06504853 -0.0751646
#  -0.06901264 -0.0751646  -0.06901264 -0.07028523 -0.07276497 -0.07028523
#  -0.06367332 -0.06226825 -0.06226825 -0.06639573 -0.06504853 -0.05935999
#  -0.06083125 -0.06639573 -0.06639573 -0.06226825 -0.06367332 -0.05935999
#  -0.06639573 -0.06367332 -0.06226825 -0.06226825 -0.05935999 -0.05935999
#  -0.05935999 -0.05630391 -0.05935999 -0.05785186 -0.05935999 -0.05935999
#  -0.06083125 -0.06083125 -0.05471275 -0.06083125 -0.06226825 -0.05935999
#  -0.05935999 -0.06226825 -0.06226825 -0.05785186 -0.06504853 -0.06226825
#  -0.06083125 -0.05935999 -0.05307449 -0.05630391 -0.06226825 -0.05471275
#  -0.05935999 -0.05471275 -0.05471275 -0.05138463 -0.05307449 -0.05307449
#  -0.05471275 -0.05471275 -0.05630391 -0.05630391 -0.05138463]


# x_test ma 0 number ni inndex upar ni row ma price namni column nu prediction karva mate 

predict = lr.predict([X_test[0,:]])

print("priceeeeeeeeeee",predict)
# x_test_data ni 0 number ni column ni price 76 avi
# [76.90661876]

predict_x_all = lr.predict(X_test)
print(predict_x_all)
# raw wise badhi row no data ni price predic karse

# [ 76.90661876  15.25005377 113.6828165  ...  21.30296864  71.43462962
#  230.0414626 ]

# have apde compare karvi hoy k a value predict kari te sachi che k nai te janva mate 

print(y_test)

# 2435     80.00
# 3113     40.00
# 426     120.00
# 1124     79.00
# 1161     45.00
#          ...
# 2078     28.34
# 6855     84.00
# 4381     32.00
# 3862     63.00
# 43      180.00
# Name: price, Length: 1424, dtype: float64


print(lr.score(X_test,y_test))
# upare banavelu linear regression che te 79% accuricy batave che 
# 0.790383709268226


# ------------------------------------------------------------------------------
"""
ridge and lasso regression
"""
# ridge regression

rd = Ridge()

rd.fit(X_train,y_train)
print(rd.score(X_test,y_test))
# 0.790568637433663


# laso regression
ls = Lasso()
ls.fit(X_train,y_train)
print(ls.score(X_test,y_test))
# 0.8036373003525774


rd = Ridge(alpha=2)

rd.fit(X_train,y_train)
print(rd.score(X_test,y_test))
# 0.790568637433663

# laso regression
# alpha ni value change karvathi thodi sari acuricy ave che 
ls = Lasso(alpha=2)
ls.fit(X_train,y_train)
print(ls.score(X_test,y_test))
# alpha ni value badalvathi accuricy ma change thase 
# 0.8160181533703601


# =--------------------------------------------------------------------------------------
"""
root mean square error 
root mean square error direct 0 k o.something ma value batave to te model direct value set kartu hoy to te na chale ane bov vadhare value pan na avvi joiye 
"""

path = r"https://drive.google.com/uc?export=download&id=1xxDtrZKfuWQfl-6KA9XEd_eatitNPnkB"

# pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)

df = pd.read_csv(path)

X = df.drop("price",axis=1)
y = df["price"]

X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2,random_state=51)

sc = StandardScaler()
sc.fit(X_train)

X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

lr = LinearRegression()

# fit metod a apdo j main data set che temathi numerical variable ni mean value nikalse ane a ani pase store rakhse ane a value ne direct fill karse have nan value upar
lr.fit(X_train,y_train)

# model evaluation
# root mean squre error 

y_pred = lr.predict(X_test)
print(y_pred)
# [ 76.90661876  15.25005377 113.6828165  ...  21.30296864  71.43462962
#  230.0414626 ]
# according to mean square error y head = our predicted value y_pred and y = actual value y_test

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(rmse)

# 64.89843531105595
# a 64 a accuracy good nathi avti to apde ana mate model  ne change kervu pade to ana mate apde datapreprocessing ne farivar sarkhu impliment karvu pade 


# -----------------------------------------------------------------------------------------------------

"""

R-squared
E-squard a predicted data ane origional data vachhe  ketlo diffrence tene r-squard kahevay
0 thi 1 ni vacchhhe value male 
1 is worst score and 1 is best score

"""


# 93-----------------------------------------------------------------------------------------------------

# polinomial regression model
# jyare data linear format ma na hoy tyare polinomial regression model no use thay.



path = r"https://drive.google.com/uc?export=download&id=1xxDtrZKfuWQfl-6KA9XEd_eatitNPnkB"

# pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)

df = pd.read_csv(path)

X = df.drop("price",axis=1)
y = df["price"]

X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2,random_state=51)

sc = StandardScaler()
sc.fit(X_train)

X_train = sc.transform(X_train)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",X_train.shape)
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX (5696, 107)
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",X_test.shape)
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX (1424, 107)

X_test = sc.transform(X_test)


# polinommial model regression ml model training  

# polinomial regression no use krvo hoy to linearregression no use karvo pade
# 

# PolynomialFeatures ma degree bydefault 2 j hoy 

poly_reg  = PolynomialFeatures()

poly_reg.fit(X_train)

X_train_poly = poly_reg.transform(X_train)
X_test_poly = poly_reg.transform(X_test)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",X_train_poly.shape)
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX (5696, 5886)
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",X_test_poly.shape)
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX (1424, 5886)

# jyare polynomial feature ne apply karvama ave tyare data vadhi jay k jya pela x_train ma 107 column hati tya 5886 thay gay

# have polinimil regression no use karvo hoy tyare linear regression no use karvama ave che 

lr = LinearRegression()

lr.fit(X_train_poly,y_train)

# train the  polynomial regression  lr.fit(X_train_poly,y_train) 

print(lr.score(X_test_poly,y_test))
# 0.9998662794935157
# ahi 99% accurict avi

# X_test_poly na first row ni price predict karva mate 
print(lr.predict([X_test_poly[0,:]]))
# [80.]

y_pred = lr.predict(X_test_poly)


# error find out karva mate root mean square error no use thay

mse = mean_squared_error(y_test,y_pred)
rmse = np.square(mse)


print(mse,rmse)
# 2.6868377008982582 7.219096830968239

# ahi rootmeansquare error a 7.27 no diffrence che tethi amodel a best model che 

# 94-----------------------------------------------------------------------------------------
# support vectore machine ?
# support vectore machime a supervised machine algorythem che 

""" supervised machine algo ma be type hoy che 
1) clasification
2) regression 

jyare continuous value no problem hoy tyare regression no use thay
ane classifictaion karvu pade tyare classification tec no use thay

-- support vector machine a banne type na problem ne solve kare che.

-- support vector machine a supervised learning no powerfull algorythem che  


"""

# 95-------------------------------------------------------------------------------------

# non linear suport vector machine
# jyare non linear data hoy tyare te ne 3d ma conver kari devama ave
# (high dimention ma convert kari devama ave ) tethi te be bhgama vechay 
# jay ground flor ane firstflor am data ne direct first flore ane groundflor upar thi tene data ne inpute kari ne alag padi shakay

# a non linear data ne alag padva ma ave te trick ne kernel trick kahevay


# 1)linear kernel
# 2) polynomial kernel with degree 

 


