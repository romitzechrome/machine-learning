# data cleaning ?
# fill the missing values in data 
'''
online file open karva mate link ma change karvano
uc?export=download& insted of open
'''
# data integration ?
# data mearge karvano alag alag jagya a thi lavi ne data ne join karvano 

# data reduction ?
# reduce the data 
# koi csv file ma 500 column che to temathi jetli joiye tetlij column lavvi baki ni ne hatavi devano ane data reduction kahevay1.

# data transformation ?
#  ak formate mathi bija fomate ma transformation karvano

# aggregasion 
# normalizations
# feature type convertion
# attribute/feature construction


# data discretization ?
# binning
# histogram analysis
# cluster analysis
# decisio tree analysis
# correlation alalysis

# data preprocessing ?

    # python librearies
         # numpy
         # pandas
         # matplotlib
         # seaborn
         # scikit learn

    # mathematics
        # statistics
        # probability
        # calculus
        # linear algebra


# data cleaning_____________________________________________________________________

# print(_______data cleaning handeling missing values )

'''
 * ignor missing value
 
 jyare total data mathi 5% data missing hoy tyare te data ne fill karidevay ane jo vadhare data hoy to tene remove karvano jethi accuracy good ave to
 jyare column no 20% thi 25% missing data hoy to te column ne delet kari shako 
 
 
 * gobal constant
 missing valure fill karvamate tya game te globaly value add kari devani but this way is not a good way
 
 * measure of central tendency
 nan value ma te column ni mean,midian k mode ne ad karvama ave but this way is not  agood way
 

 *measure of central tendency for  each class
 je te colum ma value na hoy to te row ni niji column ne dhyan ma rakhi ne te column ma mean mode k midian lagavma ave this is good way
 
 * most probable vlue tendency
 use ml algorithms,linear regg,decision tree
 mashiner learning na algorythem no use kari  ne te value ne fill karvamna ave 

 * 
 
'''
# 78---------------------------------------------------------------------------
"""data cleaning"""

import enum
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df  = pd.read_csv("train.csv")
print(df)

print(df.shape)
# (160, 13)

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

print(df.shape)
# (1460, 81)

print(df.info())
# ketli column notnull chae ane teni data type su che te baatave

print(df.isnull().sum())
# column ni nan value no sum kari ne ape 

# sns.heatmap(df.isnull())
# plt.show()

null_value = df.isnull().sum()/df.shape[0]*100

print(null_value)
# je column ma jetla %data missing hase te batavse                       

drop_column = null_value[null_value > 17].keys()
print(drop_column)

# jetli column ma 17%thi vadhare data missing che te column get karse

# Index(['LotFrontage', 'Alley', 'FireplaceQu', 'PoolQC', 'Fence',
#        'MiscFeature'],
#       dtype='object')

df2_drop_clm = df.drop(columns=drop_column)
# data frame mathi column ne drop kari didhi

print(df2_drop_clm.shape)

# have pachu check karvanu heatmap no use kari ne k ketlo data haju missing che 

# sns.heatmap(df2_drop_clm.isnull())
# plt.show()

df3_drop_rows = df2_drop_clm.dropna()
# df2 data frame mathi nan value vali badhi raw ne remove kari didhi 

# sns.heatmap(df3_drop_rows.isnull())
# plt.show()

print(df3_drop_rows.isnull().sum().sum())
# 0

df4 = df3_drop_rows.select_dtypes(include=['int64','float64']).columns
# df4 ma only int ane float dattype vali j column avse
print(df4)

# Index(['Id', 'MSSubClass', 'LotArea', 'OverallQual', 'OverallCond',
#        'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2',
#        'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF',
#        'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
#        'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces',
#        'GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF',
#        'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal',
#        'MoSold', 'YrSold', 'SalePrice'],
#       dtype='object')

# sns.displot(df['MSSubClass'])
# sns.displot(df3_drop_rows['MSSubClass'])
# plt.show()

print("PPPPPPPPPPPPPPPPPP")
print(df['MSZoning'].value_counts())

pd_nnn=pd.concat([df['MSZoning'].value_counts()/df3_drop_rows.shape[0]*100,
          df3_drop_rows['MSZoning'].value_counts()/df3_drop_rows.shape[0]*100],axis=1,keys=["mszoing org","mszoing new"])
print(pd_nnn)

# df ni mszoning column ane df3drop_row ni mszoning column a banne ne join kari je pela ketlo data hato ane have ketlo data che te check kare 

#          mszoing org  mszoing new
# RL         86.023916    79.671151
# RM         16.292975    14.275037
# FV          4.857997     4.633782
# RH          1.195815     0.822123
# C (all)     0.747384     0.597907


# --------------------------------------------------------------------------------------

dataset_path = ""
df = pd.read_csv('train.csv')

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
# file no badho data ne load karva mate matlab badhi column badhi row no data avse


print(df.shape)
print(df.isnull().sum())


missing_value__per = df.isnull().sum()/df.shape[0]*100

print(missing_value__per)
# column wise missing ketla % value missing che te batavse 
# have a % ma jetli value che te nma 20% thi vadhare missing value vali columnn ne hatavi deva mate te 20% thi vdhare missing value vali column ne ak list ma nakhi ne tene drop kari deva ma ave 

drop_column = missing_value__per[missing_value__per > 20].keys()
# 20% thi vadhu value missing hase tenu ak list taiyar thay jas e
print(drop_column)
# Index(['LotFrontage', 'Alley', 'FireplaceQu', 'PoolQC', 'Fence',
#        'MiscFeature'],
#       dtype='object')


df2_drop_columns = df.drop(columns=drop_column)
# df mathi drop_column ma raheli badhi column ne hatavi de

print(df2_drop_columns.shape)
# (1460, 75)
# 81 column mati 75 column thay 

# have vadhare null vali columnnikli gai che to have apd eonly numeric parj operation karvana hoy tethi apde olny numeric value vali column joiyr tethi tene get karisu

df3_only_numeric = df2_drop_columns.select_dtypes(['int64','float64'])
print(df3_only_numeric)
# ama only numeric dsata vali column avse 

# hit map ma dat nakhi ne jovano k data kya missing che te 

print(df3_only_numeric.isnull().sum())
# df3_only_numeric ma column wise ketli value miss che te batave 


# have nan value vali column ne ak list ma nkhva mate 
missing_value_num = [var for var in df3_only_numeric if df3_only_numeric[var].isnull().sum() > 0]

# df3_only_numeric vali datframe ma jetli column ma nan value hase tetli colun missing_value_num ma vai jase 
print("onlu nan valu column ")
print(missing_value_num)
# ['LotFrontage', 'MasVnrArea', 'GarageYrBlt']


# have a column ma missing value che tya mean k median ne add karvano
# jyare dataset ma missing value randomly hoy tyare mean k median no use thay 


# sns.set()
# for i , var in enumerate(missing_value_num):
#     plt.subplot(2,2,i+1)
#     sns.distplot(df3_only_numeric[var],bins=20,kde_kws={'linewidth':5,'color':"b"})
# plt.show()


df4_num_mean=df3_only_numeric.fillna(df3_only_numeric.mean())
print(df4_num_mean.isnull().sum().sum())
# 0

# print(df4)
# 

# mean ane median banne thi null value fillkari ne tene graph ma jovani k kai value add karvathi original sathe su fer che te 

# sns.set()
# for i ,var in enumerate(missing_value_num):
#     plt.subplot(2,2,i+1)
#     sns.distplot(df3_only_numeric[var],bins=20,hist=False,kde_kws={'linewidth':8,'color':"b"},label = "original")
#     sns.displot(df4_num_mean[var],bins=20,kde_kws={'linewidth':5,'color':"green"},label = "mean")
#     plt.legend()
# plt.show()

df5_num_median = df3_only_numeric.fillna(df3_only_numeric.median())
print(df5_num_median.isnull().sum().sum())
# 0
# print(df5_num_median)
# sns.set()
# for i ,var in enumerate(missing_value_num):
#     plt.subplot(2,2,i+1)
#     sns.distplot(df3_only_numeric[var],bins=20,hist=False,kde_kws={'linewidth':8,'color':"b"},label = "original")
#     sns.displot(df4_num_mean[var],bins=20,kde_kws={'linewidth':5,'color':"green"},label = "mean")
#     sns.displot(df5_num_median[var],bins=20,kde_kws={'linewidth':5,'color':"r"},label = "median")
#     plt.legend()
# plt.show()

# for i,var in enumerate(missing_value_num):
#     plt.figure(figsize=(10,10))
#     plt.subplot(3,1,1)
#     sns.boxenplot(df[var])
#     plt.subplot(3,1,2)
#     sns.boxenplot(df4_num_mean[var])
#     plt.subplot(3,1,3)
#     sns.boxenplot(df5_num_median[var])

# plt.show()

df_concate  = pd.concat([df3_only_numeric[missing_value_num],df4_num_mean[missing_value_num],df5_num_median[missing_value_num]],axis=1)


diffrence_all3 = df_concate[df_concate.isnull().any(axis=1)]
# df_concate data frame ma je jagya upar nulll value hase to te alhi row ne show karse  

print(diffrence_all3)

#-------------------------------------------------------------s
# measure of central tendency for each class

df = pd.read_csv('train.csv')

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


missing_value_per = df.isnull().sum()/df.shape[0]*100

drop_column = missing_value__per[missing_value__per > 20].keys()

df2_drop_columns = df.drop(columns = drop_column)

print(df2_drop_columns.shape)
# (1460, 76)

df3_num = df2_drop_columns.select_dtypes(["int64","float64"])

print(df3_num.isnull().sum())

num_var_missing = [var for var in df3_num if df3_num[var].isnull().sum() > 0]

print(num_var_missing)
# ['LotFrontage', 'MasVnrArea', 'GarageYrBlt']

print(df3_num[num_var_missing][df3_num[num_var_missing].isnull().any(axis=1)])
# num_var_missing ma raheli badhi column ne row wise check karse jo koi ak ma pan data nan hase to te column ne returnkarse 

# have a 3 column ne tena class wise mean k median add karva mate tene class wise alag karva pade 

# have tene class wise alag karva mate tene te data frame mathi tena related alag padto calss gotvo pade ane te clas a string ma hoo joiye
#   note ahi apnnne "LotConfig" column  male che je  LotFrontage ne laag pade che 
 
print(df['LotConfig'].unique())
# lotconfig vali column no unic data batavse 
# ['Inside' 'FR2' 'Corner' 'CulDSac' 'FR3']
 
 
print(df[df.loc[:,'LotConfig'] == "Inside"]["LotFrontage"])
# only lotcofig column ma je row ma inside has te j row malse ane te pan lotfrontage column ma j 

# 0        65.0
# 2        68.0
# 5        85.0
# 6        75.0
# 8        51.0
# 10       70.0
# 11       85.0
# 12        NaN
# 13       91.0
# 17       72.0
# 18       66.0
# 19       70.0
# 21       57.0
# 22       75.0

# print(df[df.loc[:,'LotConfig'] == "Inside"]["LotFrontage"].replace(np.nan,df[df.loc[:,'LotConfig'] == "Inside"]["LotFrontage"].mean()))


df_copy = df.copy()
for var_class  in df['LotConfig'].unique():
    df[df.loc[:,'LotConfig'] == var_class]["LotFrontage"].replace(np.nan,df[df.loc[:,'LotConfig'] == var_class]["LotFrontage"].mean())


# for dynamic update alle colums with his perticuler matches class 
# k kai column ma nan value che te num_var_missing  ma che 
num_vars_missing = ['LotFrontage', 'MasVnrArea', 'GarageYrBlt']

# kai column ne kai column sathe class wise te relation dharave che te cat_var_missing ma use thay che 
cat_var_missing = ['LotConfig','MasVnrType','GarageType']


df_copy = df.copy()
for cat_var,num_var in zip(cat_var_missing,num_var_missing):
    for var_class  in df[cat_var].unique():
        df_copy.update(df[df.loc[:,cat_var] == var_class][num_var].replace(np.nan,df[df.loc[:,cat_var] == var_class][num_var].mean()))


print(df_copy[num_var_missing].isnull().sum())
# LotFrontage     0
# MasVnrArea      8
# GarageYrBlt    81
# dtype: int64

# ahi badhi column no sum 0 avvo joiye pan amuk ma 8a ane amuk ma 81 ave che because categorycal variable j ahi none che tethi te numerical variable ma update na kari shake 

# Note : categorycal variable ma none value na hovi joiye jo ama nine value hase to numerical variable ne update nai kari shake  


num_vars_missing = ['LotFrontage', 'MasVnrArea', 'GarageYrBlt']

cat_var_missing = ['LotConfig','Exterior2nd','KitchenQual']

df_copy = df.copy()
for cat_var,num_var in zip(cat_var_missing,num_var_missing):
    for var_class  in df[cat_var].unique():
        df_copy.update(df[df.loc[:,cat_var] == var_class][num_var].replace(np.nan,df[df.loc[:,cat_var] == var_class][num_var].mean()))


print(df_copy[num_var_missing].isnull().sum())
# LotFrontage    0
# MasVnrArea     0
# GarageYrBlt    0
# dtype: int64

# plt.figure(figsize=(10,10)  )
# sns.set()
# for i ,var in enumerate(num_var_missing):
#     plt.subplot(2,2,i+1)
#     sns.distplot(df[var],bins=20,hist=False,kde_kws={'linewidth':8,'color':"b"},label = "original")
#     sns.displot(df_copy[var],bins=20,kde_kws={'linewidth':5,'color':"green"},label = "mean")
#     plt.legend()
# plt.show()

