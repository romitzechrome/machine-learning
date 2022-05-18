import enum
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import impute
import sklearn
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

print(train.shape)
# (1460, 81)
print(test.shape)
# (1459, 80)

print(train.head)

# machine learning algorithm ne tarin karta hoiye tyare apdi pase output ane input alag alag hoy che avij rite test ho tema only input j hoy che km k output predict karvu pade 
x_train = train.drop(columns = "SalePrice")
y_train = train["SalePrice"]

print("x_train",x_train.shape)
# x_train (1460, 80)

print("y_train ",y_train.shape)
# y_train  (1460,)

# ___________________numerical missing value imputation

num_vars = x_train.select_dtypes(["int64","float64"]).columns

print(x_train[num_vars].isnull().sum())

# Id                 0
# MSSubClass         0
# LotFrontage      259
# LotArea            0
# OverallQual        0
# OverallCond        0
# YearBuilt          0
# YearRemodAdd       0
# MasVnrArea         8
# BsmtFinSF1         0
# BsmtFinSF2         0
# BsmtUnfSF          0
# TotalBsmtSF        0
# 1stFlrSF           0
# 2ndFlrSF           0
# LowQualFinSF       0
# GrLivArea          0
# BsmtFullBath       0
# BsmtHalfBath       0
# FullBath           0
# HalfBath           0
# BedroomAbvGr       0
# KitchenAbvGr       0
# TotRmsAbvGrd       0
# Fireplaces         0
# GarageYrBlt       81
# GarageCars         0
# GarageArea         0
# WoodDeckSF         0
# OpenPorchSF        0
# EnclosedPorch      0
# 3SsnPorch          0
# ScreenPorch        0
# PoolArea           0
# MiscVal            0
# MoSold             0
# YrSold             0
# dtype: int64

# machine learning algorythem train thay jay ane deploye thay jay pachi jo atyare je column ma aak pan missing value nathi parantu jo pachi tya none
# value avi jay to tayre train dataset che te je value fill karvana chiye te lailevani ane future ma jo koi estdata set ma fill karvani thay to te value ne tya fill kari devani  
 
imputer_mean = SimpleImputer(strategy='mean')

# have apdi pase je data set che te apvano ane ama jetla fetures che temni mean value find karvani ana ,mate 

imputer_mean.fit(x_train[num_vars])

# fit a ak method che tema apde data apvano ahi apde x_train data ni only numeric column apvani che te
# fit metod a apdo j main data set che temathi numerical variable ni mean value nikalse ane a ani pase store rakhse ane a value ne direct fill karse have nan value upar

print(imputer_mean.statistics_)

# badha numerical variable ni mean value ahi ca;lculate thay ne avi jase 
# 
# [7.30500000e+02 5.68972603e+01 7.00499584e+01 1.05168281e+04
#  6.09931507e+00 5.57534247e+00 1.97126781e+03 1.98486575e+03
#  1.03685262e+02 4.43639726e+02 4.65493151e+01 5.67240411e+02
#  1.05742945e+03 1.16262671e+03 3.46992466e+02 5.84452055e+00
#  1.51546370e+03 4.25342466e-01 5.75342466e-02 1.56506849e+00
#  3.82876712e-01 2.86643836e+00 1.04657534e+00 6.51780822e+00
#  6.13013699e-01 1.97850616e+03 1.76712329e+00 4.72980137e+02
#  9.42445205e+01 4.66602740e+01 2.19541096e+01 3.40958904e+00
#  1.50609589e+01 2.75890411e+00 4.34890411e+01 6.32191781e+00
#  2.00781575e+03]


# have main dat set che tya haju sudhi mean value inpute nai thay hoy 
# to tya inpute karva mate transform method no use thay 

imputer_mean.transform(x_train[num_vars])
#  x_train dataset ma num_var ma jay jya nan value che tya a mean value inpute thay gai hase
# note: transform ma ahi apde data dataframe apya hova chata pan te aray ma batavse to ana mate direct dat frame nma j update karva ma ave che ana mate ..

x_train[num_vars] = imputer_mean.transform(x_train[num_vars])
# ana thi apanne ne je nan value mali che te numerical variable ma jya nana value che tya inpute thay jase 

# jyare train dataa ne impute karvama ave tyare test data ne impute karvo pade 

# a test data set ma jyare nan value ni jagya a koi value fill karva ma aave tyare te test dataset mathi teno mean ni value fill karcvama nathi avti te train dataset mathi teni 
# value fill karvama ave che 
# note: jyare test data set ma missing value fill karvama ave tyare te traindataset mathi nikaleli mean,median k a badhi value ne test ma missing value ni jagya afill karvi

test[num_vars] = imputer_mean.transform(test[num_vars])

print(x_train[num_vars].isnull().sum())
print(test[num_vars].isnull().sum())

# banne mathi missing value ne add thay gai successfully


# -------------------------------------------------------------------------------------------------------
'''jayre mean median k mode ni badle koi constant value add karvi hoy tyare '''

# imputer_mean = SimpleImputer(strategy='constant',fill_value=99)

# atlu change karvathi missing value ni jagya a 99 fill thay jase 

# -----------------------------------------------------------------------------------------------
'''categorical missing value  ma inpute karva mate '''



cat_var = x_train.select_dtypes(["O"]).columns

print(cat_var)
# Index(['MSZoning', 'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities',
#        'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2',
#        'BldgType', 'HouseStyle', 'RoofStyle', 'RoofMatl', 'Exterior1st',
#        'Exterior2nd', 'MasVnrType', 'ExterQual', 'ExterCond', 'Foundation',
#        'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
#        'Heating', 'HeatingQC', 'CentralAir', 'Electrical', 'KitchenQual',
#        'Functional', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual',
#        'GarageCond', 'PavedDrive', 'PoolQC', 'Fence', 'MiscFeature',
#        'SaleType', 'SaleCondition'],
#       dtype='object')


# most_frequent  = mins k te column ma sauvthi vadhare var avti hoy tevi value

imputer_mean = SimpleImputer(strategy='most_frequent')

imputer_mean.fit(x_train[cat_var])

x_train[cat_var] = imputer_mean.transform(x_train[cat_var])
test[cat_var] = imputer_mean.transform(test[cat_var])

print(x_train[cat_var].isnull().sum())
# badhi categorycal column nma value fill thay jase 
print(test[cat_var].isnull().sum())

print(x_train.isnull().sum().sum())
# 0
print(test.isnull().sum().sum())
# 0

# 83----------------------------------------------------------------------------

'''alag alag column nma alag alag matlab  mode,mean k constant, median value fill karvi hoy tyare '''

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

x_train = train.drop(columns = "SalePrice",axis=1)
y_train = train["SalePrice"]
x_test = test.copy()


'''missing value imputatuion'''

isnull_sum = x_train.isnull().sum()
# x tarin ma null valuno column wise sum thy ne avse 
print(isnull_sum)

num_vars = x_train.select_dtypes(["int64",'float64']).columns
num_vars_miss = [var for var in num_vars if isnull_sum[var] > 0]
print(num_vars_miss)
# ['LotFrontage', 'MasVnrArea', 'GarageYrBlt']


cat_vars = x_train.select_dtypes(["O"]).columns
cat_var_missing = [var for var in cat_vars if isnull_sum[var] > 0]
print(cat_var_missing)

# ['Alley', 'MasVnrType', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'Electrical', 'FireplaceQu',
#  'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'PoolQC',
#  'Fence', 'MiscFeature']


""" 
adddhi column ma mode ane bakini ma median ane cate gory ma addhi ma mode ane addhi ma constant value fill
karvi hoiy tyuare Simpleimuter no use na thay to ahi pipeline no use thay

"""

num_var_mean = ["LotFrontage"]
num_var_median = [ 'MasVnrArea', 'GarageYrBlt']

cat_var_mode = ['Alley', 'MasVnrType', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2']
cat_var_const = ['Electrical', 'FireplaceQu','GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'PoolQC','Fence', 'MiscFeature']


# have kaya list ne kai method apvi tena mate pipeline no use thay  

num_var_mean_imputer = Pipeline(steps=[("imputer",SimpleImputer(strategy="mean"))])
num_var_median_imputer = Pipeline(steps=[("imputer",SimpleImputer(strategy="median"))])

cat_var_mode_imputer = Pipeline(steps=[("imputer",SimpleImputer(strategy="most_frequent"))])
cat_var_const_imputer = Pipeline(steps=[("imputer",SimpleImputer(strategy="constant",fill_value = "misssing"))])

preprocessor=ColumnTransformer(transformers=[("mean_imputer",num_var_mean_imputer,num_var_mean),
                                ("median_imputer",num_var_median_imputer,num_var_median),
                                ("mode_imputer",cat_var_mode_imputer,cat_var_mode),
                                ("const_imputer",cat_var_const_imputer,cat_var_const)])

# have a processor ne x_train data ma missing va;lue ne a processor pramane fill karva mate fit no 8use thay 
preprocessor.fit(x_train)

print(preprocessor.transform)

"""kay kaya parameter ne kai kai value api che te janva mate"""

# bound method ColumnTransformer.transform of ColumnTransformer(transformers=[('mean_imputer',
#                                  Pipeline(steps=[('imputer', SimpleImputer())]),
#                                  ['LotFrontage']),
#                                 ('median_imputer',
#                                  Pipeline(steps=[('imputer',
#                                                   SimpleImputer(strategy='median'))]),
#                                  ['MasVnrArea', 'GarageYrBlt']),
#                                 ('mode_imputer',
#                                  Pipeline(steps=[('imputer',
#                                                   SimpleImputer(fill_value='misssing',
#                                                                 strategy='constant'))]),
#                                  ['Alley', 'MasVnrType', 'BsmtQual', 'BsmtCond',
#                                   'BsmtExposure', 'BsmtFinType1',
#                                   'BsmtFinType2']),
#                                 ('const_imputer',
#                                  Pipeline(steps=[('imputer',
#                                                   SimpleImputer(fill_value='misssing',
#                                                                 strategy='constant'))]),
#                                  ['Electrical', 'FireplaceQu', 'GarageType',
#                                   'GarageFinish', 'GarageQual', 'GarageCond',
#                                   'PoolQC', 'Fence', 'MiscFeature'])])>

print(preprocessor.named_transformers_["mode_imputer"].named_steps["imputer"].statistics_)
# mode_imputer vali badhi columnma kaya kaya mode ni kai kai value che te batave che 
# ['Grvl' 'None' 'TA' 'TA' 'No' 'Unf' 'Unf']  atla mode column wise batave che 

x_train_clean  = preprocessor.transform(x_train)
# a preprocessor pramane x_train ma araheli column a fill thay jas eparantui scikitlearn ma 2d arry ma convert thay have ane dataframe ma convert karva mate 

x_test_clean  = preprocessor.transform(x_test)
# a preprocessor pramane x_train ma araheli column a fill thay jas eparantui scikitlearn ma 2d arry ma convert thay have ane dataframe ma convert karva mate 


print(x_train_clean)
# ahi 2d array male have ane 3d ma convert karvo pade 
# # [[65.0 196.0 2003.0 ... 'misssing' 'misssing' 'misssing']
#  [80.0 0.0 1976.0 ... 'misssing' 'misssing' 'misssing']
#  [68.0 162.0 2001.0 ... 'misssing' 'misssing' 'misssing']
#  ...
#  [66.0 0.0 1941.0 ... 'misssing' 'GdPrv' 'Shed']
#  [68.0 0.0 1950.0 ... 'misssing' 'misssing' 'misssing']
#  [75.0 0.0 1965.0 ... 'misssing' 'misssing' 'misssing']]


print(preprocessor.transformers_)

# [('mean_imputer', Pipeline(steps=[('imputer', SimpleImputer())]), ['LotFrontage']), ('median_imputer', Pipeline(steps=[('imputer', SimpleImputer(strategy='median'))]),
# ['MasVnrArea', 'GarageYrBlt']), ('mode_imputer', Pipeline(steps=[('imputer', SimpleImputer(strategy='most_frequent'))]), ['Alley', 'MasVnrType', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 
# 'BsmtFinType1', 'BsmtFinType2']), ('const_imputer', Pipeline(steps=[('imputer',
#                  SimpleImputer(fill_value='misssing', strategy='constant'))]), ['Electrical', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'PoolQC', 'Fence',
# 'MiscFeature']), ('remainder', 'drop', [0, 1, 2, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 27, 28, 29, 34, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48,
# 49, 50, 51, 52, 53, 54, 55, 56, 61, 62, 65, 66, 67, 68, 69, 70, 71, 75, 76, 77, 78, 79])]

# ama reminder ma 1,2,3,4,5,6 vo data hoy che j columni index batve che k je column ma koui nan value nathi te automatic drop hay jay che pan apde jo ane drop na karvo hoy too
# but jo drop na krvu hoy to remider ne passthrew value apvi pade 

x_train_clean_miss_var = pd.DataFrame(x_train_clean,columns = num_var_mean+num_var_median+cat_var_mode+cat_var_const)

# kai datafrafarme ma update karvanu che te second parameterr ma column apvani pan a sequence ma apvani k pela preprocessor
# banavti vakhte j sequence ma lakheli hoy te sequence ma apvani

print(x_train_clean_miss_var.isnull().sum().sum())
# 0

# 84--------------------------------------------------------------------------------------------------------
"""
    categirical variables encoding

what is categorical var encoding?
categorical variable ne number na formate ma encode karvanu.

jyare categorical column no  data nominal formate ma hoy tyare tene ordinal formate ma cobnvart na kari shakiye  
to ana mate te categorical data ni column create kari nakhvani ane row wise check kari nakvanu k a available hoy to 1 ane na hoy to te navi banaveli column ma 0 add karvano 
a method ne one hot encoding kahevay ane dummy variable method kahevay a nominal categoriacl variable par add kari shakiye


"""


tips_df = pd.read_csv("tips.csv")
print(tips_df)

#      total_bill   tip     sex smoker   day    time  size
# 0         16.99  1.01  Female     No   Sun  Dinner     2
# 1         10.34  1.66    Male     No   Sun  Dinner     3
# 2         21.01  3.50    Male     No   Sun  Dinner     3
# 3         23.68  3.31    Male     No   Sun  Dinner     2
# 4         24.59  3.61  Female     No   Sun  Dinner     4
# ..          ...   ...     ...    ...   ...     ...   ...
# 239       29.03  5.92    Male     No   Sat  Dinner     3
# 240       27.18  2.00  Female    Yes   Sat  Dinner     2
# 241       22.67  2.00    Male    Yes   Sat  Dinner     2
# 242       17.82  1.75    Male     No   Sat  Dinner     2
# 243       18.78  3.00  Female     No  Thur  Dinner     2


# ahi  categorical variable che 
# sex , smoker,day,time

"""one hot encoding with pandas"""

dummy_df = pd.get_dummies(tips_df)
print(dummy_df)

#      total_bill   tip  size  sex_Female  sex_Male  ...  day_Sat  day_Sun  day_Thur  time_Dinner  time_Lunch
# 0         16.99  1.01     2           1         0  ...        0        1         0            1           0
# 1         10.34  1.66     3           0         1  ...        0        1         0            1           0
# 2         21.01  3.50     3           0         1  ...        0        1         0            1           0
# 3         23.68  3.31     2           0         1  ...        0        1         0            1           0
# 4         24.59  3.61     4           1         0  ...        0        1         0            1           0
# ..          ...   ...   ...         ...       ...  ...      ...      ...       ...          ...         ...
# 239       29.03  5.92     3           0         1  ...        1        0         0            1           0
# 240       27.18  2.00     2           1         0  ...        1        0         0            1           0
# 241       22.67  2.00     2           0         1  ...        1        0         0            1           0
# 242       17.82  1.75     2           0         1  ...        1        0         0            1           0
# 243       18.78  3.00     2           1         0  ...        0        0         1            1           0


"""one hot encoding with scikitlearn"""

oh_enc = OneHotEncoder(sparse=False)

# by default sparce = true hoy te matrics ape but apde numpy array joiye che to tene false rkhvu


oh_enc_array = oh_enc.fit_transform(tips_df[['sex','smoker','day','time']])

# tips_df[['sex',"smoke",'day','time']] je je column ne onehot enc karvanu hoy te matrics
# ahi oh_enc_array ma numpy array malse 
print(oh_enc_array)

# [[1. 0. 1. ... 0. 1. 0.]
#  [0. 1. 1. ... 0. 1. 0.]
#  [0. 1. 1. ... 0. 1. 0.]
#  ...
#  [0. 1. 0. ... 0. 1. 0.]
#  [0. 1. 1. ... 0. 1. 0.]
#  [1. 0. 1. ... 1. 1. 0.]]

print(dummy_df.keys())
# Index(['total_bill', 'tip', 'size', 'sex_Female', 'sex_Male', 'smoker_No',
#        'smoker_Yes', 'day_Fri', 'day_Sat', 'day_Sun', 'day_Thur',
#        'time_Dinner', 'time_Lunch'],
#       dtype='object')

oh_enc_df = pd.DataFrame(oh_enc_array,columns=['sex_Female', 'sex_Male', 'smoker_No',
       'smoker_Yes', 'day_Fri', 'day_Sat', 'day_Sun', 'day_Thur',
       'time_Dinner', 'time_Lunch'])

print(oh_enc_df)


#      sex_Female  sex_Male  smoker_No  smoker_Yes  day_Fri  day_Sat  day_Sun  day_Thur  time_Dinner  time_Lunch
# 0           1.0       0.0        1.0         0.0      0.0      0.0      1.0       0.0          1.0         0.0
# 1           0.0       1.0        1.0         0.0      0.0      0.0      1.0       0.0          1.0         0.0
# 2           0.0       1.0        1.0         0.0      0.0      0.0      1.0       0.0          1.0         0.0
# 3           0.0       1.0        1.0         0.0      0.0      0.0      1.0       0.0          1.0         0.0
# 4           1.0       0.0        1.0         0.0      0.0      0.0      1.0       0.0          1.0         0.0
# ..          ...       ...        ...         ...      ...      ...      ...       ...          ...         ...
# 239         0.0       1.0        1.0         0.0      0.0      1.0      0.0       0.0          1.0         0.0
# 240         1.0       0.0        0.0         1.0      0.0      1.0      0.0       0.0          1.0         0.0
# 241         0.0       1.0        0.0         1.0      0.0      1.0      0.0       0.0          1.0         0.0
# 242         0.0       1.0        1.0         0.0      0.0      1.0      0.0       0.0          1.0         0.0
# 243         1.0       0.0        1.0         0.0      0.0      0.0      0.0       1.0          1.0         0.0


# -------------------------------------------------------------------------------------------
"""label encoding vs ordinal encoding"""


# column ma categorical variable hoy te order formate ma hoy matlab tena uparthi koi mesure kari shakiye tene ordinal variable kahevay


"""
label encoding:
label encoding apply on ordinal and nominal variables
label encoding ma categorical variable na firs latter pramane o123 apvama ave 
    
ex =
grade  object 
a       laptop
b       car 
c       mango 
  
convert into label encoding    

grade  object 
0         1
1         0 
2         2 
    
------------------------------------------------------------------- 
ordinal encoding
aply on ordinal categorical variable
ordinal categorical variable ne ordinal 

ex = 
grade  object 
a       laptop
b       car 
c       mango 

convert into ordinal encoding 

grade  object 
3       laptop
2       car 
1       mango 

"""

# from sklearn.preprocessing import LabelEncoder

pd.set_option("display.max_rows",None)

df1 = pd.read_csv("train.csv")

print(df1)
df2= df1[["KitchenQual","BldgType"]]
print(df2)

le = LabelEncoder()

le_array = le.fit_transform(df2["BldgType"])
print(le_array)
# one dimentional array malse
# [0 0 0 ... 0 0 0]


# BldgType_l_enc namni new column banavi df2 ma 
 
df2["BldgType_l_enc"] = le_array

print(df2)

#      KitchenQual BldgType  BldgType_l_enc
# 0             Gd     1Fam               0
# 1             TA     1Fam               0
# 2             Gd     1Fam               0
# 3             Gd     1Fam               0
# 4             Gd     1Fam               0


print(df2["BldgType"].value_counts())
# BldgType column ma total ketli value che te count karinne ape 

# 1Fam      1220
# TwnhsE     114
# Duplex      52
# Twnhs       43
# 2fmCon      31
# Name: BldgType, dtype: int64


print(df2["KitchenQual"].value_counts())
# KitchenQual column ma total ketli value che te count karinne ape
 
# TA    735
# Gd    586
# Ex    100
# Fa     39
# Name: KitchenQual, dtype: int64


# full form of 
# TA    typical/average
# Gd    good
# Ex    excellent
# Fa     fair

# ex>gd>ta>fa


# KitchenQual ma rahela categorycal variable ne order form ma number apya

order_lable = {"Ex":4,"Gd":3,"TA":2,"Fa":1}

df2["KitchenQual_ord_enc"]=df2["KitchenQual"].map(order_lable)
print(df2)


#      KitchenQual BldgType  BldgType_l_enc  KitchenQual_ord_enc
# 0             Gd     1Fam               0                    3
# 1             TA     1Fam               0                    2
# 2             Gd     1Fam               0                    3
# 3             Gd     1Fam               0                    3
# 4             Gd     1Fam               0                    3
# 5             TA     1Fam               0                    2
# 6             Gd     1Fam               0                    3
# 7             TA     1Fam               0                    2
# 8             TA     1Fam               0                    2
# 9             TA   2fmCon               1                    2
# 10            TA     1Fam               0                    2
# 11            Ex     1Fam               0                    4
# 12            TA     1Fam               0                    2


#86 -------------------------------------------------------------------------------
"""
features scaling and scaling

what is feature?
koi column ma teni value hoy tene te column na features kahevay column

what is scall?
te feature ni max num mins k te column ma max num 8 hoy to teni scal 0-8 ni kehvays

what is features scaling ?
koi column ni scale ne koi perticuler range vali scale ma conert karvanu tene feature scaling kahevay.
mins k koi columni scale 0-8 che to tene -1 to 1 ni vacche ni scale apvama ave to tene feature scalng kahevay

this is last stape of data preprocessing
koi columnma 10 feature che temathi 9 feature independent che ane 1 feature dependent che to tene
feature scaling a independent 

jyare mashine learning algo ne trai n karvama ave tyare origional data ne train ane test data ma split karide 
ane tyare train data hoy teni upar feature scaling fit karvama ave ane test dataset upar apde je feature scaling karyu tene aplay karvama ave mins transform karvanma ave karyu


which ml algorythem required feature scaling?
k-nearest neighbors(KNN)
k-means
support vector machine(svm)
vector ne find kare ane ane jo feeatutr scale krelo daata na mle to ane time bov lagi jay ane ana pachi pan te 

principal discriminant analysis(pca)
linear discriminan analysis

gradiant descent based algorythem
linear regression 
logistic regression 
neural network 

tree based algorythem
ane koi feature scale  karelo data na apo to chale 
decision tree,random forest,xgboost

standerd scaller 
min max

"""

#  ------------------------------------------------------------------------------

"""
standardizaton
normalization
"""

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

df = sns.load_dataset("titanic")
print(df.head())

# survived  pclass     sex   age  sibsp  parch     fare  ...  class    who adult_male  deck  embark_town alive  alone
# 0         0       3    male  22.0      1      0   7.2500  ...  Third    man       True   NaN  Southampton    no  False
# 1         1       1  female  38.0      1      0  71.2833  ...  First  woman      False     C    Cherbourg   yes  False
# 2         1       3  female  26.0      0      0   7.9250  ...  Third  woman      False   NaN  Southampton   yes   True
# 3         1       1  female  35.0      1      0  53.1000  ...  First  woman      False     C  Southampton   yes  False
# 4         0       3    male  35.0      0      0   8.0500  ...  Third    man       True   NaN  Southampton    no   True


df2 = df[["survived","pclass","age","parch"]]

print(df2.head())
#    survived  pclass   age  parch
# 0         0       3  22.0      0
# 1         1       1  38.0      0
# 2         1       3  26.0      0
# 3         1       1  35.0      0
# 4         0       3  35.0      0


df3 = df2.fillna(df2.mean())
print(df3)

# data full fill thay gayo have a data ma koi nan value nathi 

# to have  adata ne matrics ane vector ma convert karvo pade


# independent variable ne matrics ma convert karvama ave ane dependent variable ne vector ma convert karvo pade 
# matrics ne show karva mate
# survived a dependent variable che
 
x = df3.drop("survived",axis=1)
y  = df3["survived"]

print(x.shape)
(891, 3)
print(y.shape)
(891,)

# have  a je data che tene train ane test ma split karvo pade
# machine learning algorithm ne train karva mate pela train data no use thay ane pachi te algorythem ne test karva mate test data no use thay ane pachi 


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=51)

# x,y a adata set che 
# test_size=0.2 a test data set ma total data no 20% bhag testdata ma onvert thase 

# random_state a pattern ma j badhivakhte data split thay jethi data badhi  vakhte sarkho ave tena nmate random_state no use thy
print(x_train.shape)
# (712, 3)
print(x_test.shape)
# (179, 3)
print(y_train.shape)
# (712,)
print(y_test.shape)
# (179,)


sc =  StandardScaler()

sc.fit(x_train)
# ananthi standardscaler a dataset mathi mean ane standerd value ne find kari lidhi che 


print(sc.mean_)
# [ 2.30617978 29.55409121  0.39185393]
# traney column ni mean value avse 

print(sc.scale_)
# standerddevision check karva mate 

print(x_train.describe())
# data frame ma jetla feature che tema diffrent difrent numerical features avta hyase te batavse  

#            pclass         age       parch
# count  712.000000  712.000000  712.000000
# mean     2.306180   29.554091    0.391854
# std      0.844651   13.000763    0.797035
# min      1.000000    0.420000    0.000000
# 25%      1.750000   22.000000    0.000000
# 50%      3.000000   29.699118    0.000000
# 75%      3.000000   35.000000    0.000000
# max      3.000000   71.000000    5.000000

# standardscale ne train data set upar apply karvanu 

x_train_sc = sc.transform(x_train)
x_test_sc = sc.transform(x_test)
print("{{{{{{{{{{{{")
print(x_train_sc)

# [[ 0.8220055  -0.42751304 -0.49198545]
#  [ 0.8220055   1.997125   -0.49198545]
#  [ 0.8220055  -1.42815732 -0.49198545]
#  ...
#  [ 0.8220055   1.41983023  3.27461284]
#  [ 0.8220055   0.01116307  0.76354731]
#  [ 0.8220055  -0.08113618 -0.49198545]]
print(x_test_sc)

df_train = pd.DataFrame(x_train_sc,columns=['pclass','age','parch'])
df_test = pd.DataFrame(x_test_sc,columns=['pclass','age','parch'])

print(df_train)
print(df_test)


#87 --------------------------------------------------------------------------------------------


