from email.errors import InvalidBase64CharactersDefect
from importlib.metadata import PathDistribution
from msilib.schema import LaunchCondition
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from pytest import mark 

# patterns ne find out karvaamate pandas no upyog thay 
# a process ne poreprocessing kahevay ana mate pandas libreary no use thay che 
# koi data che te exel sheet ma che tema kaik data missimg che to te data ne fillup karva mate pansdas no use thay che
# missing values handle kariske pandas 

# pandas data structure is

# series 
# data frame  ///   most important
# panel

print(pd.__version__)
# 1.4.2

list_s = [1,2,3,4,5,6.2,"data","values"]

print(pd.Series(list_s))

# 0,1,2,3 a index number che

# 0         1
# 1         2
# 2         3
# 3         4
# 4         5
# 5       6.2
# 6      data
# 7    values
# dtype: object
 
print(type(list_s))
# <class 'list'>

series_2 = pd.Series([1,2,3,4])
print(series_2)

# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64

empty_s = pd.Series([])
print("ddddddddd",empty_s)

# Series([], dtype: float64)

series_3 = pd.Series([1,2,3,4],index = ["a","b","c","d"])
# [1,2,3,4] a value che ane index ne change keri che a b,c,d ma 
# jetli valyu tetli index apvi farajiyat che 
print(series_3)

# a    1
# b    2
# c    3
# d    4
# dtype: int64


series_4 = pd.Series([1,2,3,4],index=["a","b","c","d"],dtype = float,name = "data values")
print(series_4)

# a    1.0
# b    2.0
# c    3.0
# d    4.0
# Name: data values, dtype: float64


scaler_s = pd.Series(0.5)
print(scaler_s)
# 0    0.5
# dtype: float64

scaler_s = pd.Series(0.5,index = [1,2,3,4])
# print(scaler_s)
# 1    0.5
# 2    0.5
# 3    0.5
# 4    0.5
# dtype: float64

dict_s =  pd.Series({"a":1,"b":2})
print(dict_s)
# a    1
# b    2
# dtype: int64

s4 = pd.Series([1,2,3,4,5])
print(s4)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

print(s4[0])
# 1

print(s4[3])
# 4
 
print(s4[0:4])
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64

print(max(s4))
# 5

print(s4[s4>3])
# 3    4
# 4    5
# dtype: int64


s5 = pd.Series([1,2,3,4,5])
print(s5)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

print(s4+s5)
# 0     2
# 1     4
# 2     6
# 3     8
# 4    10
# dtype: int64

s6 = pd.Series([1,2,3])
print(s6)
# 0    1
# 1    2
# 2    3
# dtype: int64

print(s5 + s6)
# pandas jya null value hoy tya bydefauly nan kari de   
# 0    2.0
# 1    4.0
# 2    6.0
# 3    NaN
# 4    NaN
# dtype: float64


# ---------------------------------data frame --------------------------------

print("______________________________data frame _________________________")


emp_df = pd.DataFrame()
print(emp_df)
# Empty DataFrame
# Columns: []
# Index: []


lst = ["a","b","c"]
df1 = pd.DataFrame(lst)
print(df1)

# pello 0 a adatra frame ni column ni kari name che il
#    0
# 0  a
# 1  b
# 2  c


ls_of_ls =  [[1,2,3],[4,5,6],[7,8,9]]
df2 = pd.DataFrame(ls_of_ls)
print(df2)
#    0  1  2
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9


dict1 = {"id":[11,12,13,14]}
df3 = pd.DataFrame(dict1)
print(df3)
#    id
# 0  11
# 1  12
# 2  13
# 3  14

dict2 = {"id":[11,12,13,14],"value":[15,16,17,18]}
df3 = pd.DataFrame(dict2)
print(df3)
#    id  value
# 0  11     15
# 1  12     16
# 2  13     17
# 3  14     18



ls_dict  = [{"a":1,"b":2},{"a":1,"b":2,"c":3}]
# jo ey vadhare hase to automatic nan value add thay jase 

df3 = pd.DataFrame(ls_dict)
print("dic",df3)
#    a  b    c
# 0  1  2  NaN
# 1  1  2  3.0
 
dict_str = {"id":pd.Series([1,2,3,4,5]),"sn":pd.Series([11,22,33,44,55])}
df6 = pd.DataFrame(dict_str)
print(df6)

#    id  sn
# 0   1  11
# 1   2  22
# 2   3  33
# 3   4  44
# 4   5  55



# csv_data = pd.read_csv("D:\\romit\\machinelearning\\numpy\\data.csv")
df = pd.read_csv("data.csv")
print(df)

#    student   class  studthours  sleeping hour
# 0      1001     10           2              9
# 1      1002     10           6              8
# 2      1003     11           3              9
# 3      1004     12           5              7
# 4      1005     11           4              8
# 5      1006     10           2              9


print(os.getcwd())
# D:\romit\machinelearning\numpy

print(pd.read_csv("data.csv"))

print(type(df))
# <class 'pandas.core.frame.DataFrame'>

print(df.columns)
# Index(['student ', 'class', 'studthours', 'sleeping hour'], dtype='object')


print(pd.read_csv("data.csv",nrows=3))
# jetli rows joiye tetli row lkhvi
#    student   class  studthours  sleeping hour
# 0      1001     10           2              9
# 1      1002     10           6              8
# 2      1003     11           3              9


print(pd.read_csv("data.csv",usecols=[0,3]))
# je column print karcvani hoy teno index num apvo
#    student   sleeping hour
# 0      1001              9
# 1      1002              8
# 2      1003              9
# 3      1004              7
# 4      1005              8
# 5      1006              9


print(pd.read_csv("data.csv",skiprows=1))
# jtlami row ne skip karvi hoy tetli row ne skip ows ma add karidevani  tethi te niklijay
# ahi student,valai row nikli gai
#    1001  10  2  9
# 0  1002  10  6  8
# 1  1003  11  3  9
# 2  1004  12  5  7
# 3  1005  11  4  8
# 4  1006  10  2  9

print(pd.read_csv("data.csv",skiprows=2))
# ahi uparthi 2 row ne skip kari didhi
#    1002  10  6  8
# 0  1003  11  3  9
# 1  1004  12  5  7
# 2  1005  11  4  8
# 3  1006  10  2  9

 
print(pd.read_csv("data.csv",skiprows=[1,2,3]))
# list ma jetli row hase te row nikalse
#    student   class  studthours  sleeping hour
# 0      1004     12           5              7
# 1      1005     11           4              8
# 2      1006     10           2              9


print(pd.read_csv("data.csv",index_col='student'))
# je column ne index tarike levani hoy tene index_col ma lakhvathi tene as a index consider karse

#          class  studthours  sleeping hour
# student
# 1001        10           2              9
# 1002        10           6              8
# 1003        11           3              9
# 1004        12           5              7
# 1005        11           4              8
# 1006        10           2              9

print(pd.read_csv("data.csv",header=2))
# header ma jetlami row ni index number hase tyatho te heading apse ane chalu karse 
#    1002  10  6  8
# 0  1003  11  3  9
# 1  1004  12  5  7
# 2  1005  11  4  8
# 3  1006  10  2  9


print(pd.read_csv("data.csv",header=None))
# heade None tyare automatic 1,2,3,4 avi index pramane name api dese
 
#          0      1           2              3
# 0  student  class  studthours  sleeping hour
# 1     1001     10           2              9
# 2     1002     10           6              8
# 3     1003     11           3              9
# 4     1004     12           5              7
# 5     1005     11           4              8
# 6     1006     10           2              9

print(pd.read_csv("data.csv",header=None,prefix="Columns"))


# prefix ma 0,1,2 ni agal je lagavvu hoy te lagavvama ave te heading ma add thay jay 
# columns ni jagyaya game te use kari sakay

# Columns0 Columns1    Columns2       Columns3
# 0  student    class  studthours  sleeping hour
# 1     1001       10           2              9
# 2     1002       10           6              8
# 3     1003       11           3              9
# 4     1004       12           5              7
# 5     1005       11           4              8
# 6     1006       10           2              9


print(pd.read_csv("data.csv",names=["a","b","c","D","e","f"]))

# perticuler column ne header apvama ave tyare 
# ane jo header vadhare hoy tyare by default nan value set kari de che 

#          a      b           c              D   e   f
# 0  student  class  studthours  sleeping hour NaN NaN
# 1     1001     10           2              9 NaN NaN
# 2     1002     10           6              8 NaN NaN
# 3     1003     11           3              9 NaN NaN
# 4     1004     12           5              7 NaN NaN
# 5     1005     11           4              8 NaN NaN
# 6     1006     10           2              9 NaN NaN

# 25--7p-------------------------------------------------------------------------------

df = pd.read_csv("data.csv")
print(df.head())

# head method first 5 record print karse
# df.head(8) pela 8 reord print karse

#    student  class  studthours  sleeping hour
# 0     1001     10           2              9
# 1     1002     10           6              8
# 2     1003     11           3              9
# 3     1004     12           5              7
# 4     1005     11           4              8


print(df.tail())
# tail method last 5 record apse
# df.tail(6) last 6 record apse
#    student  class  studthours  sleeping hour
# 4     1005     11           4              8
# 5     1006     10           2              9
# 6     1007     12           5              9
# 7     1008     12           6              8
# 8     1009     10           6              8


# df = pd.read_csv("data.csv",dtype={"class":'float64'})
# print(df)

# class vali column ni data type change kari multiple column ne pan change keari skay

#    student  class  studthours  sleeping hour
# 0     1001   10.0           2              9
# 1     1002   10.0           6              8
# 2     1003   11.0           3              9
# 3     1004   12.0           5              7
# 4     1005   11.0           4              8
# 5     1006   10.0           2              9
# 6     1007   12.0           5              9
# 7     1008   12.0           6              8
# 8     1009   10.0           6              8


df = pd.read_csv("data.csv",true_values=['Yes'])
# jya Yes hase tya True kari dese 

print(df)
#    student  class  studthours  sleeping hour  date
# 0     1001     10           2              9  True
# 1     1002     10           6              8  True
# 2     1003     11           3              9  True
# 3     1004     12           5              7  True
# 4     1005     11           4              8  True
# 5     1006     10           2              9  True
# 6     1007     12           5              9  True
# 7     1008     12           6              8  True
# 8     1009     10           6              8  True


df = pd.read_csv("data.csv",true_values=['Yes'],false_values=['No'])
print(df)
# jya yes tya true ane No tya false 
#    student  class  studthours  sleeping hour   date
# 0     1001     10           2              9   True
# 1     1002     10           6              8   True
# 2     1003     11           3              9   True
# 3     1004     12           5              7  False
# 4     1005     11           4              8   True
# 5     1006     10           2              9  False
# 6     1007     12           5              9   True
# 7     1008     12           6              8   True
# 8     1009     10           6              8  False

# 26----p8--------------------------------------------------------------------

print("______________________________handeling missing values in pandas ")
print()
df = pd.read_csv("data.csv")
print(df)

'''( N/A,N/A,#NA,-1.#Ind,-1.#QNAN
-Nan,-nan,N/A,NA,NILL
 null,n/a,nan,1.#IND,,1.#QNAN ) ''' 
#  a badhi string value ne bydefault pandas NAN consider kare che 
# pandas libreary a none value ne bydefault  Nan kari de 

#    student  class  studthours  sleeping hour date
# 0     1001   10.0         2.0            9.0  Yes
# 1     1002   10.0         6.0            8.0  NaN
# 2     1003   11.0         NaN            9.0  Yes
# 3     1004   12.0         5.0            7.0   No
# 4     1005    NaN         4.0            8.0  Yes
# 5     1006    NaN         2.0            9.0   No
# 6     1007   12.0         5.0            NaN  Yes
# 7     1008   12.0         6.0            8.0  Yes
# 8     1009   10.0         6.0            8.0   No


df = pd.read_csv("data.csv",na_values=["notavailable","novalues"])
print(df)

# jya jya not available ane novalues  hase tene Nan consider karse

#    student  class  studthours  sleeping hour date
# 0     1001   10.0         2.0            9.0  Yes
# 1     1002   10.0         6.0            8.0  NaN
# 2     1003   11.0         NaN            9.0  Yes
# 3     1004   12.0         5.0            7.0   No
# 4     1005    NaN         4.0            8.0  Yes
# 5     1006    NaN         2.0            9.0   No
# 6     1007   12.0         5.0            NaN  Yes
# 7     1008   12.0         6.0            8.0  Yes
# 8     1009   10.0         6.0            8.0   No


df = pd.read_csv("data.csv",na_values={"class":"notavailable","date":"none"})
print(df)

# class svali column ma jya not available hase tya Nan consider karse ane date vali column ma jya none hase tya Nan consider karse 

# filedata:
# student	class	studthours	sleeping hour	date
# 1001	10	2	9	Yes
# 1002	10	6	8	null
# 1003	11		9	Yes
# 1004	12	5	7	No
# 1005	notavailable	4	8	notavailable
# 1006	null	2	9	No
# 1007	12	5		Yes
# 1008	12	6	8	Yes
# 1009	10	6	8	No


#    student  class  studthours  sleeping hour          date
# 0     1001   10.0         2.0            9.0           Yes
# 1     1002   10.0         6.0            8.0           NaN
# 2     1003   11.0         NaN            9.0           Yes
# 3     1004   12.0         5.0            7.0            No
# 4     1005    NaN         4.0            8.0  notavailable
# 5     1006    NaN         2.0            9.0            No
# 6     1007   12.0         5.0            NaN           Yes
# 7     1008   12.0         6.0            8.0           Yes
# 8     1009   10.0         6.0            8.0            No


df = pd.read_csv("data.csv",keep_default_na=False)
print(df)
#  bydefault jetla ne NAN value consider kare che tene  na kre tena mate keepdefaultna ne False karvama aave 

#    student         class studthours sleeping hour          date
# 0     1001            10          2             9           Yes
# 1     1002            10          6             8          null
# 2     1003            11                        9           Yes
# 3     1004            12          5             7            No
# 4     1005  notavailable          4             8  notavailable
# 5     1006          null          2             9            No
# 6     1007            12          5                         Yes
# 7     1008            12          6             8           Yes
# 8     1009            10          6             8            No

df = pd.read_csv("data.csv",na_filter=False)
print(df)

#    student  class  studthours  sleeping hour date
# 0     1001     10           2              9  Yes
# 1     1002     10           6              8  Yes
# 2     1003     11           5              9  Yes
# 3     1004     12           5              7   No
# 4     1005     11           4              8  yes
# 5     1006     11           2              9  YES
# 6     1007     12           5              8  Yes
# 7     1008     12           6              8  Yes
# 8     1009     10           6              8   No

# jo koi column ma none value hase to tya Nan consider nai thay

#    student  class  studthours  sleeping hour date
# 0     1001     10           2              9  Yes
# 1     1002     10           6              8  Yes
# 2     1003     11           5              9  Yes
# 3     1004     12           5              7   No
# 4     1005     11           4              8  yes
# 5     1006     11           2              9  YES
# 6     1007     12           5              8  Yes
# 7     1008     12           6              8
# 8     1009     10           6              8   No


df = pd.read_csv("data.csv")
print(df.isnull())

# jya null value hase tya true avse ane jta null value  nai hoy tya  tya false  cosider karse 

#    student  class  studthours  sleeping hour   date
# 0    False  False       False          False  False
# 1    False  False       False          False  False
# 2    False  False       False          False  False
# 3    False   True       False          False  False
# 4    False   True       False          False  False
# 5    False   True       False          False  False
# 6    False  False       False          False  False
# 7    False  False       False          False   True
# 8    False  False       False          False  False

print(df.isnull().sum())
# jetli coluumn ma jetli null value hase teno sum apsse 
# student          0
# class            3
# studthours       0
# sleeping hour    0
# date             1
# dtype: int64

print(df.isnull().sum().sum())
# akhi data frame ma ketli null value che te no sum apse 
# output = 4


print(df.notnull())
# jta value none  k nyull hase tene false apse ane jya null k none nai hoy tya true consider karse
# baku sum ne a badhu isnull ni jemj

#    student  class  studthours  sleeping hour   date
# 0     True   True        True           True   True
# 1     True   True        True           True   True
# 2     True   True        True           True   True
# 3     True  False        True           True   True
# 4     True  False        True           True   True
# 5     True  False        True           True   True
# 6     True   True        True           True   True
# 7     True   True        True           True  False
# 8     True   True        True           True   True


sr = pd.Series([1,2,3,np.nan,4,np.nan])
print(sr)
# 0    1.0
# 1    2.0
# 2    3.0
# 3    NaN
# 4    4.0
# 5    NaN
# dtype: float64

print(sr.isnull())
# 0    False
# 1    False
# 2    False
# 3     True
# 4    False
# 5     True
# dtype: bool

print(sr.isnull().sum())
# output = 2

df = pd.read_csv("data.csv")

print(df)

#    student  class  studthours  sleeping hour date
# 0     1001   10.0           2              9  Yes
# 1     1002   10.0           6              8  Yes
# 2     1003   11.0           5              9  Yes
# 3     1004    NaN           5              7   No
# 4     1005    NaN           4              8  yes
# 5     1006    NaN           2              9  YES
# 6     1007   12.0           5              8  Yes
# 7     1008   12.0           6              8  NaN
# 8     1009   10.0           6              8   No

print(df.dropna())
# jetli jetli row ma nan value hase te badhi drop kari dese 

#    student  class  studthours  sleeping hour date
# 0     1001   10.0           2              9  Yes
# 1     1002   10.0           6              8  Yes
# 2     1003   11.0           5              9  Yes
# 6     1007   12.0           5              8  Yes
# 8     1009   10.0           6              8   No

print(df.dropna(axis = 1) )
# je je column ma none value hase te badhi column ne drop kari dese 

#    student  studthours  sleeping hour
# 0     1001           2              9
# 1     1002           6              8
# 2     1003           5              9
# 3     1004           5              7
# 4     1005           4              8
# 5     1006           2              9
# 6     1007           5              8
# 7     1008           6              8
# 8     1009           6              8


print(df.dropna(axis = 0))
# je je row ma nan value hase te akhi row nw remove kari dese 

#    student  class  studthours  sleeping hour date
# 0     1001   10.0           2              9  Yes
# 1     1002   10.0           6              8  Yes
# 2     1003   11.0           5              9  Yes
# 6     1007   12.0           5              8  Yes
# 8     1009   10.0           6              8   No


print(df.dropna(how='any'))
#  similer to dropna
# jetli row ma none value hase te badhi ne drop kari dese

#    student  class  studthours  sleeping hour date
# 0     1001   10.0           2              9  Yes
# 1     1002   10.0           6              8  Yes
# 2     1003   11.0           5              9  Yes
# 6     1007   12.0           5              8  Yes
# 8     1009   10.0           6              8   No


print(df.dropna(how='all'))
#  koi record ne drop nai kare badhi row badhi column batavse 
#  but jo koi column k row no badhi value none k null hse to te ne drop kari dese 

#    student  class  studthours  sleeping hour date
# 0     1001   10.0           2              9  Yes
# 1     1002   10.0           6              8  Yes
# 2     1003   11.0           5              9  Yes
# 3     1004    NaN           5              7   No
# 4     1005    NaN           4              8  yes
# 5     1006    NaN           2              9  YES
# 6     1007   12.0           5              8  Yes
# 7     1008   12.0           6              8  NaN
# 8     1009   10.0           6              8   No


print(df.dropna(thresh= 1))
#  jetli row ma minimum ak notnull value hoy te print karse jo badhi value null k none hase to tenre drop kari dese 

#    student  class  studthours  sleeping hour date
# 0     1001   10.0           2              9  Yes
# 1     1002   10.0           6              8  Yes
# 2     1003   11.0           5              9  Yes
# 3     1004    NaN           5              7   No
# 4     1005    NaN           4              8  yes
# 5     1006    NaN           2              9  YES
# 6     1007   12.0           5              8  Yes
# 7     1008   12.0           6              8  NaN
# 8     1009   10.0           6              8   No

print(df.dropna(thresh= 2))
# minimum 2 value to notnull hovi jnjoiye jo ak value notnull hoy to tene drop kari dese 
#    student  class  studthours  sleeping hour date
# 0     1001   10.0           2              9  Yes
# 1     1002   10.0           6              8  Yes
# 2     1003   11.0           5              9  Yes
# 3     1004    NaN           5              7   No
# 4     1005    NaN           4              8  yes
# 5     1006    NaN           2              9  YES
# 6     1007   12.0           5              8  Yes
# 7     1008   12.0           6              8  NaN
# 8     1009   10.0           6              8   No


print(df.dropna(subset=["class"]))
# class vali column ma jetli nan value hase te akho row nw drop kari dese. 
#    student  class  studthours  sleeping hour date
# 0     1001   10.0           2              9  Yes
# 1     1002   10.0           6              8  Yes
# 2     1003   11.0           5              9  Yes
# 6     1007   12.0           5              8  Yes
# 7     1008   12.0           6              8  NaN
# 8     1009   10.0           6              8   No


print(df.dropna(inplace=True))
print(df)
# inplace a juni data frame ma j jetli row ma none k null values hase teb badhi ne drop kari dese 
# junu data frame j updatekaridese

#    student  class  studthours  sleeping hour date
# 0     1001   10.0           2              9  Yes
# 1     1002   10.0           6              8  Yes
# 2     1003   11.0           5              9  Yes
# 6     1007   12.0           5              8  Yes
# 8     1009   10.0           6              8   No

# 29---p11----------------------------------------------------------------

print("__________________________________pandas fillna")

df = pd.read_csv("data.csv")

# NAN value ne fillup kare

print(df.fillna(0))

# fillna na parameter ma je hoy te nan ni jagya a print thay

#    student  class  studthours  sleeping hour date
# 0     1001   10.0           2              9  Yes
# 1     1002   10.0           6              8  Yes
# 2     1003   11.0           5              9  Yes
# 3     1004    0.0           5              7   No
# 4     1005    0.0           4              8  yes
# 5     1006    0.0           2              9  YES
# 6     1007   12.0           5              8  Yes
# 7     1008   12.0           6              8    0
# 8     1009   10.0           6              8   No

print("PPPPPPPPPPPPPP")
print(df.fillna({"student":"none","class":0,"studthours":0,"sleeping hour":0}))
# ama raheli column ma perticuler value set thay jay none ni jagya par 

#    student  class  studthours  sleeping hour date
# 0     1001   10.0           2              9  Yes
# 1     1002   10.0           6              8  Yes
# 2     1003   11.0           5              9  Yes
# 3     1004    0.0           5              7   No
# 4     1005    0.0           4              8  yes
# 5     1006    0.0           2              9  YES
# 6     1007   12.0           5              8  Yes
# 7     1008   12.0           6              8  NaN
# 8     1009   10.0           6              8   No

print(df.fillna(method='ffill'))
# print(df.fillna('pad'))
# padd == ffill
# method  fffill ma ana pelani value automatic fill thay jay  

#    student  class  studthours  sleeping hour date
# 0     1001   10.0           2              9  Yes
# 1     1002   10.0           6              8  Yes
# 2     1003   11.0           5              9  Yes
# 3     1004   11.0           5              7   No
# 4     1005   11.0           4              8  yes
# 5     1006   11.0           2              9  YES
# 6     1007   12.0           5              8  Yes
# 7     1008   12.0           6              8  Yes
# 8     1009   10.0           6              8   No

print(df.fillna(method='bfill'))
# bfill ma none valyu pachi ni next j value hoy te fill thay jay 

#    student  class  studthours  sleeping hour date
# 0     1001   10.0           2              9  Yes
# 1     1002   10.0           6              8  Yes
# 2     1003   11.0           5              9  Yes
# 3     1004   12.0           5              7   No
# 4     1005   12.0           4              8  yes
# 5     1006   12.0           2              9  YES
# 6     1007   12.0           5              8  Yes
# 7     1008   12.0           6              8   No
# 8     1009   10.0           6              8   No

print(df.fillna(method='ffill',axis =0))

# ana agalni row ni value set thay jay axix 0 matlab row par 

#    student  class  studthours  sleeping hour date
# 0     1001   10.0           2              9  Yes
# 1     1002   10.0           6              8  Yes
# 2     1003   11.0           5              9  Yes
# 3     1004   11.0           5              7   No
# 4     1005   11.0           4              8  yes
# 5     1006   11.0           2              9  YES
# 6     1007   12.0           5              8  Yes
# 7     1008   12.0           6              8  Yes
# 8     1009   10.0           6              8   No

print(df.fillna(method='ffill',axis =1))

# axis = 1 mins column ni value set thay ane axis =0 matlab row ni value set thay 
# axis0 matlab tena pela ni j column hoy teni value set thay jase 

#   student class studthours sleeping hour date
# 0    1001  10.0          2             9  Yes
# 1    1002  10.0          6             8  Yes
# 2    1003  11.0          5             9  Yes
# 3    1004  1004          5             7   No
# 4    1005  1005          4             8  yes
# 5    1006  1006          2             9  YES
# 6    1007  12.0          5             8  Yes
# 7  1008.0  12.0        6.0           8.0  8.0
# 8    1009  10.0          6             8   No

print(df.fillna(0,limit = 1))
# limit sathe value athva to method ne specify karvi pade matlab k nan ni badle su print karvu che te 
# limit hamnesha >1 hovu joiye 
# limit 1 matlab ak column ma ak j nan value ni badle 0 fill thase bakini ma nai thay se\
# jo limit 2 hoy to ak column ma 2 nan value ne change karse third nan valyu ne nan j reva dese     
    
#    student  class  studthours  sleeping hour date
# 0     1001   10.0           2              9  Yes
# 1     1002   10.0           6              8  Yes
# 2     1003   11.0           5              9  Yes
# 3     1004    0.0           5              7   No
# 4     1005    NaN           4              8  yes
# 5     1006    NaN           2              9  YES
# 6     1007   12.0           5              8  Yes
# 7     1008   12.0           6              8    0
# 8     1009   10.0           6              8   No

print(df.fillna(5,inplace=True))
print(df)
# inplace a pan nan ni jagya par ahi 5 ne set karse pan inplace method che atle teni tej data frame ne update karse 

#    student  class  studthours  sleeping hour date
# 0     1001   10.0           2              9  Yes
# 1     1002   10.0           6              8  Yes
# 2     1003   11.0           5              9  Yes
# 3     1004    5.0           5              7   No
# 4     1005    5.0           4              8  yes
# 5     1006    5.0           2              9  YES
# 6     1007   12.0           5              8  Yes
# 7     1008   12.0           6              8    5
# 8     1009   10.0           6              8   No


df = pd.read_csv("data.csv")
print(df.replace(to_replace="Yes",value="finance"))

#  jya jay Yes hase tya finance kari de 
 
#    student  class  studthours  sleeping hour     date
# 0     1001   10.0           2              9  finance
# 1     1002   10.0           6              8  finance
# 2     1003   11.0           5              9  finance
# 3     1004    NaN           5              7       No
# 4     1005    NaN           4              8      yes
# 5     1006    NaN           2              9      YES
# 6     1007   12.0           5              8  finance
# 7     1008   12.0           6              8      NaN
# 8     1009   10.0           6              8       No


print(df.replace(10,50))
#  10 ne 50 ma convert kari de 

#    student  class  studthours  sleeping hour date
# 0     1001   50.0           2              9  Yes
# 1     1002   50.0           6              8  Yes
# 2     1003   11.0           5              9  Yes
# 3     1004    NaN           5              7   No
# 4     1005    NaN           4              8  yes
# 5     1006    NaN           2              9  YES
# 6     1007   12.0           5              8  Yes
# 7     1008   12.0           6              8  NaN
# 8     1009   50.0           6              8   No

print(df.replace([1,2,3,4,5,6,7,8,9],0))

#  jay jya 1 ,2,3,4,5,6,7,8,9 hase tya 0 thay jase 

#    student  class  studthours  sleeping hour date
# 0     1001   10.0           0              0  Yes
# 1     1002   10.0           0              0  Yes
# 2     1003   11.0           0              0  Yes
# 3     1004    NaN           0              0   No
# 4     1005    NaN           0              0  yes
# 5     1006    NaN           0              0  YES
# 6     1007   12.0           0              0  Yes
# 7     1008   12.0           0              0  NaN
# 8     1009   10.0           0              0   No

print(df.replace([1,2,3,4,5,6,7,8,9],[11,12,13,14,15,16,17,18,19]))

# list ni same list ni jem j replace thy jase replaceex: 1 ni jagya a 11 thay jase 

#    student  class  studthours  sleeping hour date
# 0     1001   10.0          12             19  Yes
# 1     1002   10.0          16             18  Yes
# 2     1003   11.0          15             19  Yes
# 3     1004    NaN          15             17   No
# 4     1005    NaN          14             18  yes
# 5     1006    NaN          12             19  YES
# 6     1007   12.0          15             18  Yes
# 7     1008   12.0          16             18  NaN
# 8     1009   10.0          16             18   No


print(df.replace({"studthours":6},"hhhhhhhh"))

# studenthour namni column ma jya jya 6 hase ty hhhh replace thay jas e 
 
#    student  class studthours  sleeping hour date
# 0     1001   10.0          2              9  Yes
# 1     1002   10.0   hhhhhhhh              8  Yes
# 2     1003   11.0          5              9  Yes
# 3     1004    NaN          5              7   No
# 4     1005    NaN          4              8  yes
# 5     1006    NaN          2              9  YES
# 6     1007   12.0          5              8  Yes
# 7     1008   12.0   hhhhhhhh              8  NaN
# 8     1009   10.0   hhhhhhhh              8   No


print(df.replace('[A-za-z]',123654456,regex=True))
# jetli string value hase a 1235654456 ma convert thay jase

#    student  class  studthours  sleeping hour         date
# 0     1001   10.0           2              9  123654456.0
# 1     1002   10.0           6              8  123654456.0
# 2     1003   11.0           5              9  123654456.0
# 3     1004    NaN           5              7  123654456.0
# 4     1005    NaN           4              8  123654456.0
# 5     1006    NaN           2              9  123654456.0
# 6     1007   12.0           5              8  123654456.0
# 7     1008   12.0           6              8          NaN
# 8     1009   10.0           6              8  123654456.0

print(df.replace({"date":'[A-za-z]'},0,regex=True))
# date  column ma jya a-z noi use thayo hase te sting ne 0 ma convert kari dese  

#    student  class  studthours  sleeping hour  date
# 0     1001   10.0           2              9   0.0
# 1     1002   10.0           6              8   0.0
# 2     1003   11.0           5              9   0.0
# 3     1004    NaN           5              7   0.0
# 4     1005    NaN           4              8   0.0
# 5     1006    NaN           2              9   0.0
# 6     1007   12.0           5              8   0.0
# 7     1008   12.0           6              8   NaN
# 8     1009   10.0           6              8   0.0


print(df.replace("yes",method='pad'))

# jya jya yes hase tya teni upar ni row ni valyu print thaijase 

#    student  class  studthours  sleeping hour date
# 0     1001   10.0           2              9  Yes
# 1     1002   10.0           6              8  Yes
# 2     1003   11.0           5              9  Yes
# 3     1004    NaN           5              7   No
# 4     1005    NaN           4              8   No
# 5     1006    NaN           2              9  YES
# 6     1007   12.0           5              8  Yes
# 7     1008   12.0           6              8  NaN `   `
# 8     1009   10.0           6              8   No

print(df.replace(0,method='bfill',limit = 1))

# jya jya o hase tya teni row ni pachi ji row ni value consider thase 
# ane limit 2 hoy to ak column ma 2 varj thase 

#    student  class  studthours  sleeping hour date
# 0     1001     10           2              9  Yes
# 1     1002     10           6              8  Yes
# 2     1003     11           5              9  Yes
# 3     1004      0           5              7   No
# 4     1005      0           4              8  yes
# 5     1006     12           2              9  YES
# 6     1007     12           5              8  Yes
# 7     1008     12           6              8  NaN
# 8     1009     10           6              8   No

df.replace(0,100,inplace=True)
print(df)

# jya jya 0 hase tya 100 kari dese but ama inplace che atle te data frame ne mdi fy j kari dese  

#    student  class  studthours  sleeping hour date
# 0     1001     10           2              9  Yes
# 1     1002     10           6              8  Yes
# 2     1003     11           5              9  Yes
# 3     1004    100           5              7   No
# 4     1005    100           4              8  yes
# 5     1006    100           2              9  YES
# 6     1007     12           5              8  Yes
# 7     1008     12           6              8  NaN
# 8     1009     10           6              8   No


# 31-----p13-------------------------------------------------------------------------------------
print()
print("__________________pandas interpolate")
print()


df =  pd.read_csv("student.csv")
print(df)

#      id name  rollnum  marks
# 0   1.0  aaa     11.0   98.0
# 1   2.0  bbb     12.0   56.0
# 2   3.0  ccc     13.0   96.0
# 3   4.0  ddd     14.0   98.0
# 4   NaN  eee      NaN    NaN
# 5   NaN  fff     16.0    NaN
# 6   NaN  NaN     17.0    NaN
# 7   8.0  hhh      NaN   86.0
# 8   9.0  iii     19.0   75.0
# 9  10.0  jjj     20.0   76.0


print(df.interpolate())
# interpolate function a numeric va;lue ne auto matic fillup kare te nan box ni agal pachal ni valyu parthi automatic tene fillup kare 
# string valueue ma te Nan j revadese 
# by default linear pramane te update kare matlab k teni agal pachal ni value ne dhyan ma rakhi ne te ni vacceh ni value print karse 
#      id name  rollnum  marks
# 0   1.0  aaa     11.0   98.0
# 1   2.0  bbb     12.0   56.0
# 2   3.0  ccc     13.0   96.0
# 3   4.0  ddd     14.0   98.0
# 4   5.0  eee     15.0   95.0
# 5   6.0  fff     16.0   92.0
# 6   7.0  NaN     17.0   89.0
# 7   8.0  hhh     18.0   86.0
# 8   9.0  iii     19.0   75.0
# 9  10.0  jjj     20.0   76.0



# print(df.interpolate(method='time'))
# method='time' a only datetime formate ne j automatic update kare but ahi ap[di pase date column a str ma che to tene date time ma convert karvi pade ] 
# te index number pramane autoimatic update kare
# date ne index ma lavvi pade 

print(type(df.date[0]))
# <class 'str'>

df =  pd.read_csv("student.csv",parse_dates=['date'])
print(df)
#      id name  rollnum  marks       date
# 0   1.0  aaa     11.0   98.0   2021-02-01
# 1   2.0  bbb     12.0   56.0   2021-03-01
# 2   3.0  ccc     13.0   96.0   2021-01-01
# 3   4.0  ddd     14.0   98.0   2021-01-01
# 4   NaN  eee      NaN    NaN   2021-05-01
# 5   NaN  fff     16.0    NaN        NaT
# 6   NaN  NaN     17.0    NaN   2021-08-01
# 7   8.0  hhh      NaN   86.0        NaT
# 8   9.0  iii     19.0   75.0   2021-09-01
# 9  10.0  jjj     20.0   76.0   2021-10-01


print(type(df.date[0]))
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>

df =  pd.read_csv("student.csv",parse_dates=['date'],index_col=['date'])
# parse date parameter a je te column ne datetimme formate ma conver klari de  
print(df)

#               id name  rollnum  marks
# date
# 2021-02-01   1.0  aaa     11.0   98.0
# 2021-03-03   2.0  bbb     12.0   56.0
# 2021-01-01   3.0  ccc     13.0   96.0
# 2021-01-02   4.0  ddd     14.0   98.0
# 2021-05-01   NaN  eee      NaN    NaN
# 2021-08-02   NaN  fff     16.0    NaN
# 2021-08-08   NaN  NaN     17.0    NaN
# 2021-08-15   8.0  hhh      NaN   86.0
# 2021-09-01   9.0  iii     19.0   75.0
# 2021-10-01  10.0  jjj     20.0   76.0


print(df.interpolate(method='time'))
# te teni najik ni date pramne te nan value ne fillup karse 


#                    id name    rollnum      marks
# date
# 2021-02-01   1.000000  aaa  11.000000  98.000000
# 2021-03-03   2.000000  bbb  12.000000  56.000000
# 2021-01-01   3.000000  ccc  13.000000  96.000000
# 2021-01-02   4.000000  ddd  14.000000  98.000000
# 2021-05-01   4.145455  eee  13.552632  66.727273
# 2021-08-02   7.527273  fff  16.000000  83.636364
# 2021-08-08   7.745455  NaN  17.000000  84.727273
# 2021-08-15   8.000000  hhh  17.583333  86.000000
# 2021-09-01   9.000000  iii  19.000000  75.000000
# 2021-10-01  10.000000  jjj  20.000000  76.000000



df =  pd.read_csv("student.csv",parse_dates=['date'],index_col=['id'])
print(df)

#      name  rollnum  marks       date
# id
# 1.0   aaa     11.0   98.0 2021-02-01
# 2.0   bbb     12.0   56.0 2021-03-03
# 3.0   ccc     13.0   96.0 2021-01-01
# 4.0   ddd     14.0   98.0 2021-01-02
# NaN   eee      NaN    NaN 2021-05-01
# NaN   fff     16.0    NaN 2021-08-02
# NaN   NaN     17.0    NaN 2021-08-08
# 8.0   hhh      NaN   86.0 2021-08-15
# 9.0   iii     19.0   75.0 2021-09-01
# 10.0  jjj     20.0   76.0 2021-10-01


df =  pd.read_csv("student.csv")
print(df)

#    id name  rollnum  marks      date
# 0   1  aaa     11.0   98.0  02-01-21
# 1   2  bbb     12.0   56.0  03-03-21
# 2   3  ccc     13.0   96.0  01-01-21
# 3   4  ddd     14.0   98.0  01-02-21
# 4   5  eee      NaN    NaN  05-01-21
# 5   6  fff     16.0    NaN  08-02-21
# 6   7  NaN     17.0    NaN  08-08-21
# 7   8  hhh      NaN   86.0  15-08-21
# 8   9  iii     19.0   75.0  09-01-21
# 9  10  jjj     20.0   76.0  10-01-21


print(df.interpolate(limit=1))

# limit = 1 mins k ak  column ma  (ak sathe) 1 varj value fill karse ane biji but ghani badhi value update kare limit change karo te pramane change thay 

#    id name  rollnum  marks      date
# 0   1  aaa     11.0   98.0  02-01-21
# 1   2  bbb     12.0   56.0  03-03-21
# 2   3  ccc     13.0   96.0  01-01-21
# 3   4  ddd     14.0   98.0  01-02-21
# 4   5  eee     15.0   95.0  05-01-21
# 5   6  fff     16.0    NaN  08-02-21
# 6   7  NaN     17.0    NaN  08-08-21
# 7   8  hhh     18.0   86.0  15-08-21
# 8   9  iii     19.0   75.0  09-01-21
# 9  10  jjj     20.0   76.0  10-01-21

print(df.interpolate(limit = 1,limit_direction='backward'))
# backword mins value column ni last mathi update kare ane limit apvi jaruri che 

#    id name  rollnum  marks      date
# 0   1  aaa     11.0   98.0  02-01-21
# 1   2  bbb     12.0   56.0  03-03-21
# 2   3  ccc     13.0   96.0  01-01-21
# 3   4  ddd     14.0   98.0  01-02-21
# 4   5  eee     15.0    NaN  05-01-21
# 5   6  fff     16.0    NaN  08-02-21
# 6   7  NaN     17.0   89.0  08-08-21
# 7   8  hhh     18.0   86.0  15-08-21
# 8   9  iii     19.0   75.0  09-01-21
# 9  10  jjj     20.0   76.0  10-01-21


print(df.interpolate(limit = 1,limit_direction='both'))

# uparthio ane nichethi banne side thi  null value ne filup karse 

#    id name  rollnum  marks      date
# 0   1  aaa     11.0   98.0  02-01-21
# 1   2  bbb     12.0   56.0  03-03-21
# 2   3  ccc     13.0   96.0  01-01-21
# 3   4  ddd     14.0   98.0  01-02-21
# 4   5  eee     15.0   95.0  05-01-21
# 5   6  fff     16.0    NaN  08-02-21
# 6   7  NaN     17.0   89.0  08-08-21
# 7   8  hhh     18.0   86.0  15-08-21
# 8   9  iii     19.0   75.0  09-01-21
# 9  10  jjj     20.0   76.0  10-01-21


print(df.interpolate(limit_area='inside'))
# badhi nan value ne fill kari dese 

#    id name  rollnum  marks      date
# 0   1  aaa     11.0   98.0  02-01-21
# 1   2  bbb     12.0   56.0  03-03-21
# 2   3  ccc     13.0   96.0  01-01-21
# 3   4  ddd     14.0   98.0  01-02-21
# 4   5  eee     15.0   95.0  05-01-21
# 5   6  fff     16.0   92.0  08-02-21
# 6   7  NaN     17.0   89.0  08-08-21
# 7   8  hhh     18.0   86.0  15-08-21
# 8   9  iii     19.0   75.0  09-01-21
# 9  10  jjj     20.0   76.0  10-01-21


print(df.interpolate(limit_area='outside'))
#  koi pan missing value ne fill nai kare 
#    id name  rollnum  marks      date
# 0   1  aaa     11.0   98.0  02-01-21
# 1   2  bbb     12.0   56.0  03-03-21
# 2   3  ccc     13.0   96.0  01-01-21
# 3   4  ddd     14.0   98.0  01-02-21
# 4   5  eee      NaN    NaN  05-01-21
# 5   6  fff     16.0    NaN  08-02-21
# 6   7  NaN     17.0    NaN  08-08-21
# 7   8  hhh      NaN   86.0  15-08-21
# 8   9  iii     19.0   75.0  09-01-21
# 9  10  jjj     20.0   76.0  10-01-21


#33 =====p15====================================================================

print("___________________________loc&iloc in pandas")
df =  pd.read_csv("student.csv")
print(df)
#    id name  rollnum  marks      date
# 0   1  aaa     11.0   98.0  02-01-21
# 1   2  bbb     12.0   56.0  03-03-21
# 2   3  ccc     13.0   96.0  01-01-21
# 3   4  ddd     14.0   98.0  01-02-21
# 4   5  eee      NaN    NaN  05-01-21
# 5   6  fff     16.0    NaN  08-02-21
# 6   7  NaN     17.0    NaN  08-08-21
# 7   8  hhh      NaN   86.0  15-08-21
# 8   9  iii     19.0   75.0  09-01-21
# 9  10  jjj     20.0   76.0  10-01-21


print(df.loc[0])
# first index ni value return karse
# id                1
# name            aaa
# rollnum        11.0
# marks          98.0
# date       02-01-21
# Name: 0, dtype: object

print(df.loc[[0]])

#    id name  rollnum  marks      date
# 0   1  aaa     11.0   98.0  02-01-21

print(df.loc[[0,1,2]])

# 0,1,2 a tran index number ni valyue apse 
#   id name  rollnum  marks      date
# 0   1  aaa     11.0   98.0  02-01-21
# 1   2  bbb     12.0   56.0  03-03-21
# 2   3  ccc     13.0   96.0  01-01-21


print(df.loc[1,'marks'])
# marks column ni 1 index par raheli val ne print karse 
56.0

print(df.loc[1:9,'marks'])
#  index number 1 thi 9 sudhi ni marks column ma raheli badhi value print thay

# 1    56.0
# 2    96.0
# 3    98.0
# 4     NaN
# 5     NaN
# 6     NaN
# 7    86.0
# 8    75.0
# 9    76.0
# Name: marks, dtype: float64

print(df.loc[[False,False,True,False,False,True,False,False,True,True]])
# index number pramane jetlami index upar true ave tene print karse 
# note : jetla true false atli index hovi jaruri che 

#    id name  rollnum  marks      date
# 2   3  ccc       13     96  01-01-21
# 5   6  fff       16     65  08-02-21
# 8   9  iii       19     75  09-01-21
# 9  10  jjj       20     76  10-01-21

print(df.loc[df['rollnum'] < 15])

# roll num ma lesthen 15 vala hase tetlani j value apse

#    id name  rollnum  marks      date
# 0   1  aaa       11     98  02-01-21
# 1   2  bbb       12     56  03-03-21
# 2   3  ccc       13     96  01-01-21
# 3   4  ddd       14     98  01-02-21

print(df.loc[df['rollnum'] < 15,['marks','name']])

# roll num 15 thi ocha hoy ane only koi perticuler column noj data joto hoy tyare

#    marks name
# 0     98  aaa
# 1     56  bbb
# 2     96  ccc
# 3     98  ddd

print(df.iloc[[0]])

#    id name  rollnum  marks      date
# 0   1  aaa       11     98  02-01-21

print()
print(df.iloc[:,0])

# badhi row 0 number ni index vali colum ni badhi row ne print karva mate 
# 0     1
# 1     2
# 2     3
# 3     4
# 4     5
# 5     6
# 6     7
# 7     8
# 8     9
# 9    10
# Name: id, dtype: int64


print(df.iloc[[0,1]])

#  0 ane 1 number ni index no data
 
#  id name  rollnum  marks      date
# 0   1  aaa       11     98  02-01-21
# 1   2  bbb       12     56  03-03-21


print(df.iloc[[False,False,True,False,False,True,False,False,True,True]])

#    id name  rollnum  marks      date
# 2   3  ccc       13     96  01-01-21
# 5   6  fff       16     65  08-02-21
# 8   9  iii       19     75  09-01-21
# 9  10  jjj       20     76  10-01-21


# 36---------p16----------------------------------------------------------------------------------------

print("___________________groupby__________")


gr1 = df.groupby(by='marks')
# data frame ne group by ma karvama ave tyare te object return kare
print(gr1)
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000002056699BA90>

print(gr1.groups)

#  marks wise group kari dese k a marks vala data aa insdex number ma che m 

# {56: [1], 65: [5], 75: [8], 76: [9], 85: [6], 86: [4, 7], 96: [2], 98: [0, 3]}

print()
print(df.groupby(by=['marks','date']).groups)

# marks ane date wise groppup kari dese k a marks vala data aa insd

# {(56, '03-03-21'): [1], (65, '08-02-21'): [5], (75, '09-01-21'): [8], (76, '10-01-21'): [9], (85, '08-08-21'): [6], (86, '05-01-21'): [4], (86, '15-08-21'): [7], (96, '01-01-21'): [2], (98, '02-01-21'): [0, 3]}

for marks,df_1 in gr1:
    print(marks)
    print(df_1)

# 56
#    id name  rollnum  marks      date
# 1   2  bbb       12     56  03-03-21
# 65
#    id name  rollnum  marks      date
# 5   6  fff       16     65  08-02-21
# 75
#    id name  rollnum  marks      date
# 8   9  iii       19     75  09-01-21
# 76
#    id name  rollnum  marks      date
# 9  10  jjj       20     76  10-01-21
# 85
#    id name  rollnum  marks      date
# 6   7  ggg       17     85  08-08-21
# 86
#    id name  rollnum  marks      date
# 4   5  eee       15     86  05-01-21
# 7   8  hhh       18     86  15-08-21
# 96
#    id name  rollnum  marks      date
# 2   3  ccc       13     96  01-01-21
# 98
#    id name  rollnum  marks      date
# 0   1  aaa       11     98  02-01-21
# 3   4  ddd       14     98  02-01-21


gl1 = list(gr1)
print("LLLLLLLLLLLLLLLLLLLLLLL")

print(list(gr1))

#  list ma convert thay jay 
# [(56,    id name  rollnum  marks      date
# 1   2  bbb       12     56  03-03-21), (65,    id name  rollnum  marks      date
# 5   6  fff       16     65  08-02-21), (75,    id name  rollnum  marks      date
# 8   9  iii       19     75  09-01-21), (76,    id name  rollnum  marks      date
# 9  10  jjj       20     76  10-01-21), (85,    id name  rollnum  marks      date
# 6   7  ggg       17     85  08-08-21), (86,    id name  rollnum  marks      date
# 4   5  eee       15     86  05-01-21
# 7   8  hhh       18     86  15-08-21), (96,    id name  rollnum  marks      date
# 2   3  ccc       13     96  01-01-21), (98,    id name  rollnum  marks      date
# 0   1  aaa       11     98  02-01-21
# 3   4  ddd       14     98  02-01-21)]

print(dict(list(gr1)))

# {56:    id name  rollnum  marks      date
# 1   2  bbb       12     56  03-03-21, 65:    id name  rollnum  marks      date
# 5   6  fff       16     65  08-02-21, 75:    id name  rollnum  marks      date
# 8   9  iii       19     75  09-01-21, 76:    id name  rollnum  marks      date
# 9  10  jjj       20     76  10-01-21, 85:    id name  rollnum  marks      date
# 6   7  ggg       17     85  08-08-21, 86:    id name  rollnum  marks      date
# 4   5  eee       15     86  05-01-21
# 7   8  hhh       18     86  15-08-21, 96:    id name  rollnum  marks      date
# 2   3  ccc       13     96  01-01-21, 98:    id name  rollnum  marks      date
# 0   1  aaa       11     98  02-01-21
# 3   4  ddd       14     98  02-01-21}


g3 = df.groupby('marks').get_group(86)
print(g3)
# marks vali column ma jena 86 hase tenu group banavi ne ape

print(g3.sum())

# g3 ma je group hase teno sum kari de 
# id                       13
# name                 eeehhh
# rollnum                  33
# marks                   172
# date       05-01-2115-08-21
# dtype: object

print(g3.describe())

#  jetli int value hase tena par thata aerithmatic function batavse in

#             id   rollnum  marks
# count  2.00000   2.00000    2.0
# mean   6.50000  16.50000   86.0
# std    2.12132   2.12132    0.0
# min    5.00000  15.00000   86.0
# 25%    5.75000  15.75000   86.0
# 50%    6.50000  16.50000   86.0
# 75%    7.25000  17.25000   86.0
# max    8.00000  18.00000   86.0

print(gr1.agg(['sum','max','mean']))

# badhi column upar a badha uperation perform karva hpoy tyare 

#       sum max  mean     sum max  mean
# marks
# 56      2   2   2.0      12  12  12.0
# 65      6   6   6.0      16  16  16.0
# 75      9   9   9.0      19  19  19.0
# 76     10  10  10.0      20  20  20.0
# 85      7   7   7.0      17  17  17.0
# 86     13   8   6.5      33  18  16.5
# 96      3   3   3.0      13  13  13.0
# 98      5   4   2.5      25  14  12.5


# 35------p17------------------------------------------------------------------

print("__________________________merge function in pandas ")

df1 = pd.DataFrame({"id":[1,2,3,4],"class":[9,10,11,12]})

print(df1)
#    id  class
# 0   1      9
# 1   2     10
# 2   3     11
# 3   4     12

df2 = pd.DataFrame({"id":[1,2,3,4],"name":['a','b','c','d']})
print(df2)

#    id name
# 0   1    a
# 1   2    b
# 2   3    c
# 3   4    d

print(pd.merge(df1,df2,on='id'))
# on =  'id ' thi merge karvama ave che jetlani id sarkhi hase tetli rows j batavase jo id match nai thay teni row nai btave
# id na base upar banne data frame combin hy jase 

#    id  class name
# 0   1      9    a
# 1   2     10    b
# 2   3     11    c
# 3   4     12    d

print(pd.merge(df2,df1,on='id'))
# je dta frame nu name pela rakhvama abve teni series pela ave 

# on =  'id ' thi merge karvama ave che jetlani id sarkhi hase tetli rows j batavase jo id match nai thay teni row nai btave

#    id name  class
# 0   1    a      9
# 1   2    b     10
# 2   3    c     11
# 3   4    d     12


print(pd.merge(df2,df1,on='id',how = 'inner'))
# how = inner matlab banne ma sarkhi id hase e j avse [intersection]
 
#    id name  class
# 0   1    a      9
# 1   2    b     10
# 2   3    c     11
# 3   4    d     12

# ---------------------------------------------------
df1 = pd.DataFrame({"id":[1,2,3,4],"class":[9,10,11,12]})

df2 = pd.DataFrame({"id":[1,2,3,5],"name":['a','b','c','d']})


print(pd.merge(df1,df2,on='id',how = 'left'))
# left ma je detaframe hase te full avse ane rightvali ma nan va;lue avse [left joining type]
#    id  class name
# 0   1      9    a
# 1   2     10    b
# 2   3     11    c
# 3   4     12  NaN

print(pd.merge(df1,df2,on='id',how = 'right'))
# [right join type ]right ma je data frame hase te full fillup avse ane left vali ma unmatch ma nan avse 
#   id  class name
# 0   1    9.0    a
# 1   2   10.0    b
# 2   3   11.0    c
# 3   5    NaN    d

print(pd.merge(df1,df2,on='id',how = 'outer'))

# outer ma badha data tahs ematch val apn thse ane unmatch vala pan thase 

#    id  class name
# 0   1    9.0    a
# 1   2   10.0    b
# 2   3   11.0    c
# 3   4   12.0  NaN
# 4   5    NaN    d

print(pd.merge(df1,df2,on='id',how = 'outer',indicator = True))
# indecator = True mins te mearging kai rite thayu che jo banne match thay ne thau hoy ri both ave ,lleft row no data avyo hoy to left_only ave ane right no avyo hoy to right onlly ave ave

#    id  class name      _merge
# 0   1    9.0    a        both
# 1   2   10.0    b        both
# 2   3   11.0    c        both
# 3   4   12.0  NaN   left_only
# 4   5    NaN    d  right_only



df1 = pd.DataFrame({"id":[1,2,3,4],"class":[9,10,11,12]})

df2 = pd.DataFrame({"id":[5,6,7,8],"name":['a','b','c','d']})

print(pd.merge(df1,df2,left_index=True,right_index=True))

# bydefault id_x ane id_y banavi dese ane banne data frame ni value avse 

#    id_x  class  id_y  name
# 0     1      9     5    a
# 1     2     10     6    b
# 2     3     11     7    c
# 3     4     12     8    d


df1 = pd.DataFrame({"id":[1,2,3,4],"class":[9,10,11,12]})

df2 = pd.DataFrame({"id":[1,2,3,4],"class":[9,10,11,12]})

print(pd.merge(df1,df2,on = 'id'))
# jyare id sarkhi hoy tyare 
# bt default class_x ane class_y am banne ne print karidese 

#    id  class_x  class_y
# 0   1        9        9
# 1   2       10       10
# 2   3       11       11
# 3   4       12       12

print(pd.merge(df1,df2,on = 'id',suffixes=["df1_data","df2_data"]))

# by default avti column na name change karva hoy btyare 

#    id  classdf1_data  classdf2_data
# 0   1              9              9
# 1   2             10             10
# 2   3             11             11
# 3   4             12             12


# 36---------p18--------------------------------------concate function

s1 = pd.Series([0,1,2,3])
print(s1)

s2 = pd.Series([4,5,6,7,8])
print(s2)

print(pd.concat([s1,s2]))

# 0    0
# 1    1
# 2    2
# 3    3
# 0    4
# 1    5
# 2    6
# 3    7
# 4    8
# dtype: int64

df1 = pd.DataFrame({"id":[1,2,3,4],"name":['a','b','c','d'],"class":[5,6,7,8]})
print(df1)
#    id name  class
# 0   1    a      5
# 1   2    b      6
# 2   3    c      7
# 3   4    d      8

df2 = pd.DataFrame({"id":[5,6,7,8],"name":['e','f','g','h'],"class":[9,10,11,12]})
print(df2)
#    id name  class
# 0   5    e      9
# 1   6    f     10
# 2   7    g     11
# 3   8    h     12

print(pd.concat([df1,df2]))
# concate ma peli data frame ni niche thii j biji data frame start thay jay ane index number pan te juni data frame no hoiy tej re 
#    id name  class
# 0   1    a      5
# 1   2    b      6
# 2   3    c      7
# 3   4    d      8
# 0   5    e      9
# 1   6    f     10
# 2   7    g     11
# 3   8    h     12

print(pd.concat([df1,df2],axis = 1))

#  axix = 1 hoy tyare column wise data frame nu concatination thay
#  mins ak dara frame ni column puri thay pachi biji data frame ni column start tyhay jay 
#    id name  class  id name  class
# 0   1    a      5   5    e      9
# 1   2    b      6   6    f     10
# 2   3    c      7   7    g     11
# 3   4    d      8   8    h     12

print(pd.concat([df1,df2],ignore_index=True))

# ignore index  = True karvathi index number line ma chalto hoy tem j chale 

#    id name  class
# 0   1    a      5
# 1   2    b      6
# 2   3    c      7
# 3   4    d      8
# 4   5    e      9
# 5   6    f     10
# 6   7    g     11
# 7   8    h     12

df1 = pd.DataFrame({"id":[1,2,3,4],"name":['a','b','c','d'],"class":[5,6,7,8]})
print(df1)

df2= pd.DataFrame({"id":[3,4],"name":['c','d'],"class":[7,8]})
print(df2)

print(pd.concat([df1,df2],ignore_index=True))
#  jaruri nathi k banne data frame ni lenth sarkhi hovi joiye
#    id name  class
# 0   1    a      5
# 1   2    b      6
# 2   3    c      7
# 3   4    d      8
# 4   3    c      7
# 5   4    d      8


print(pd.concat([df1,df2],axis = 1))

# banne dat frame ni lengh sarkhi na hoy ane column vise tene  concatinate karvama ave tyare je data frame ma valye ghatti hoy tya by default nan consider kari de 

#    id name  class   id name  class
# 0   1    a      5  3.0    c    7.0
# 1   2    b      6  4.0    d    8.0
# 2   3    c      7  NaN  NaN    NaN
# 3   4    d      8  NaN  NaN    NaN

print(pd.concat([df1,df2],axis = 1,join = "inner"))

# join = inner karvma ave tyare teni banne ma jo te index value hoy toj concatinate thay 

#    id name  class  id name  class
# 0   1    a      5   3    c      7
# 1   2    b      6   4    d      8


df1 = pd.DataFrame({"id":[1,2,3,4],"name":['a','b','c','d'],"class":[5,6,7,8]})
print(df1)

df2 = pd.DataFrame({"id":[5,6,7,8],"name":['e','f','g','h'],"class":[9,10,11,12]})
print(df2)

print(pd.concat([df1,df2],keys=['first_df','seconf_df']))


#  keys no use dataframe ne key apva mate thay che 
 
#              id name  class
# first_df  0   1    a      5
#           1   2    b      6
#           2   3    c      7
#           3   4    d      8
# seconf_df 0   5    e      9
#           1   6    f     10
#           2   7    g     11
#           3   8    h     12


print(pd.concat([df1,df2],axis = 1,keys=['first_df','seconf_df']))

#  first_df            seconf_df
#         id name class        id name class
# 0        1    a     5         5    e     9
# 1        2    b     6         6    f    10
# 2        3    c     7         7    g    11
# 3        4    d     8         8    h    12

# 38----p20---------------join()--------------------------------------------------------------

print("________________________join in pandas")

df1 = pd.DataFrame({"a":[1,2,3],"b":[10,20,30]})

df2 = pd.DataFrame({"c":[4,5,6],"d":[10,20,30]})

print(df1.join(df2))

#    a   b  c   d
# 0  1  10  4  10
# 1  2  20  5  20
# 2  3  30  6  30


print(df2.join(df1))

#    c   d  a   b
# 0  4  10  1  10
# 1  5  20  2  20
# 2  6  30  3  30

df1 = pd.DataFrame({"a":[1,2,3],"b":[10,20,30]},index=['a','b','c'])
print(df1)
#    a   b
# a  1  10
# b  2  20
# c  3  30

df2 = pd.DataFrame({"c":[4,5],"d":[10,20]},index=['a','b'])
print(df2)
#    c   d
# a  4  10
# b  5  20

print(df1.join(df2))
# index alag alag hase to nan vlyu apse 
# jetlma index match thase ane join karse

#    a   b    c     d
# a  1  10  4.0  10.0
# b  2  20  5.0  20.0
# c  3  30  NaN   NaN

print(df1.join(df2,how='right'))

#  right data farme pramane output ape 

#    a   b  c   d
# a  1  10  4  10
# b  2  20  5  20

print(df1.join(df2,how='outer'))

#    a   b    c     d
# a  1  10  4.0  10.0
# b  2  20  5.0  20.0
# c  3  30  NaN   NaN

df1 = pd.DataFrame({"a":[1,2,3],"b":[10,20,30]},index=['a','b','c'])

df2 = pd.DataFrame({"a":[4,5],"d":[10,20]},index=['a','b'])

print("PPPPPPPPPPPPPPPPPPPPPPPPPPPP")
# print(df1.join(df2))
# be data farme ma jo column na name same hoy tyare erroe ave 

print(df1.join(df2,lsuffix="_1"))
# lsuffix ma jo banne data frame ni je colum sarkhi hase tyare left vali data farem ni column nu name change kari de 

#    a_1   b    a     d
# a    1  10  4.0  10.0
# b    2  20  5.0  20.0
# c    3  30  NaN   NaN

print(df1.join(df2,rsuffix="_1"))

#  column na name srkha hoy tyare ane join karvama ave tyare eror ave but lsuffix k r suffix no use karvathi left left valu change thay ane rsudffix to right vali data farme ni columnname change thay

#    a   b  a_1     d
# a  1  10  4.0  10.0
# b  2  20  5.0  20.0
# c  3  30  NaN   NaN

# 39--p21-----------------------------------append in pandas 

#  ak data frame ma biji data frame na rows k column ne append karva mate k add karva mate thay che 
# apend  function no use karvathi te navo data frame object return kare 

df1 = pd.DataFrame({"a":[1,2,3],"b":[10,20,30]})
print(df1)
#    a   b
# 0  1  10
# 1  2  20
# 2  3  30

df2 = pd.DataFrame({"a":[4,5,6],"b":[40,50,60]})
print(df2)
#    a   b
# 0  4  40
# 1  5  50
# 2  6  60


print(df1.append(df2,ignore_index=True))
#    a   b
# 0  1  10
# 1  2  20
# 2  3  30
# 3  4  40
# 4  5  50
# 5  6  60

df1 = pd.DataFrame({"a":[1,2,3],"b":[10,20,30]})
df2 = pd.DataFrame({"c":[4,5,6],"b":[40,50,60]})

print(df1.append(df2,ignore_index=True,sort = False))

# ignor_index = True mins k index number chalto hoy tej chale ane sort= false mins k 

#     a   b    c
# 0  1.0  10  NaN
# 1  2.0  20  NaN
# 2  3.0  30  NaN
# 3  NaN  40  4.0
# 4  NaN  50  5.0
# 5  NaN  60  6.0


# 40----p22-------------------------------------pivot table in pandas-----------------------------------------------------
print()
print("_______________________pivot table")
print()


df = pd.read_csv("movie.csv")
print(df)

#        genre  year  budget  ratings%
# 0     action  2008      28        48
# 1     action  2007     200        57
# 2     action  2009      32        82
# 3     action  2008      10        56
# 4  adventure  2010      18        75
# 5  adventure  2009      20        46
# 6  adventure  2008      15        65
# 7     comedy  2007      66        55
# 8     comedy  2008      56        81
# 9     comedy  2009      52        71

print(df.pivot_table(index='genre'))

# pivot_table ma je column ne index apvama ave te category wise thay jay ane bakini column ni valyu ni average set thay jay 
 
#               budget  ratings%  year
# genre
# action     67.500000     60.75  2008
# adventure  17.666667     62.00  2009
# comedy     58.000000     69.00  2008


print(df.pivot_table(index='genre',columns='year'))

# column ma je columnname hase tena pramane te dataframe ni information set thay jase 
# ane badhi column ni value ne average wise batavse

#           budget                   ratings%
# year        2007  2008  2009  2010     2007  2008  2009  2010
# genre
# action     200.0  19.0  32.0   NaN     57.0  52.0  82.0   NaN
# adventure    NaN  15.0  20.0  18.0      NaN  65.0  46.0  75.0
# comedy      66.0  56.0  52.0   NaN     55.0  81.0  71.0   NaN


print(df.pivot_table(index='genre',columns='year',aggfunc='count'))

# count kari ne appse agfunc ma mostof aggregrate function batavse

#          budget                ratings%
# year        2007 2008 2009 2010     2007 2008 2009 2010
# genre
# action       1.0  2.0  1.0  NaN      1.0  2.0  1.0  NaN
# adventure    NaN  1.0  1.0  1.0      NaN  1.0  1.0  1.0
# comedy       1.0  1.0  1.0  NaN      1.0  1.0  1.0  NaN

print(df.pivot_table(index='genre',columns='year',aggfunc='sum'))

#           budget                   ratings%
# year        2007  2008  2009  2010     2007   2008  2009  2010
# genre
# action     200.0  38.0  32.0   NaN     57.0  104.0  82.0   NaN
# adventure    NaN  15.0  20.0  18.0      NaN   65.0  46.0  75.0
# comedy      66.0  56.0  52.0   NaN     55.0   81.0  71.0   NaN

print(df.pivot_table(index='genre',columns='year',fill_value='none'))

# jema value nai hoy tene bydefault none rakse none ni jagya par biju game te lakh shakiye
# note:-  jo avi koi column hoy k jema badhi value none hoy to te column ne by default remove kari dese
#           budget                   ratings%
# year        2007  2008  2009  2010     2007  2008  2009  2010
# genre
# action     200.0  19.0  32.0  none     57.0  52.0  82.0  none
# adventure   none  15.0  20.0  18.0     none  65.0  46.0  75.0
# comedy      66.0  56.0  52.0  none     55.0  81.0  71.0  none


print(df.pivot_table(index='genre',columns='year',fill_value='none',dropna=False))
#  jo koi column ma badhi value nan hoy to te column ne show karvi hoy to dropna=False karvathi te co;lumn pan shoew thase 

print(df.pivot_table(index='genre',columns='year',fill_value='none',dropna=False,margins=True))

# margin = True mins te badhi column no automatic mean kadhi ne all vali column auto matic update kari dese

#           budget                                    ratings%
# year        2007   2008       2009  2010        All     2007  2008       2009  2010    All
# genre
# action     200.0   19.0       32.0  none       67.5     57.0  52.0       82.0  none  60.75
# adventure   none   15.0       20.0  18.0  17.666667     none  65.0       46.0  75.0   62.0
# comedy      66.0   56.0       52.0  none       58.0     55.0  81.0       71.0  none   69.0
# All        133.0  27.25  34.666667  18.0       49.7     56.0  62.5  66.333333  75.0   63.6\
    
print(df.pivot_table(index='genre',columns='year',fill_value='none',dropna=False,margins=True,aggfunc='sum'))

# agg_func hoy to all ma te column ni ane row ni value no sum thay ne ave 
#               budget                        ratings%
# year        2007  2008  2009  2010  All     2007   2008  2009  2010  All
# genre
# action     200.0  38.0  32.0  none  270     57.0  104.0  82.0  none  243
# adventure   none  15.0  20.0  18.0   53     none   65.0  46.0  75.0  186
# comedy      66.0  56.0  52.0  none  174     55.0   81.0  71.0  none  207
# All          266   109   104    18  497      112    250   199    75  636
    
# 41-------p23------------------------------------pandas melt ----------

# data ne transform k reshap karva mate rthat che 

    
df  = pd.read_csv('movie.csv')
print(df)
    
print(pd.melt(df))    
    
#      variable      value
# 0      genre     action
# 1      genre     action
# 2      genre     action
# 3      genre     action
# 4      genre  adventure
# 5      genre  adventure
# 6      genre  adventure
# 7      genre     comedy
# 8      genre     comedy
# 9      genre     comedy
# 10      year       2008
# 11      year       2007
# 12      year       2009
# 13      year       2008
# 14      year       2010
# 15      year       2009
# 16      year       2008
# 17      year       2007
# 18      year       2008
# 19      year       2009
# 20    budget         28
# 21    budget        200
# 22    budget         32
# 23    budget         10
# 24    budget         18
# 25    budget         20
# 26    budget         15
# 27    budget         66
# 28    budget         56
# 29    budget         52
# 30  ratings%         48
# 31  ratings%         57
# 32  ratings%         82
# 33  ratings%         56
# 34  ratings%         75
# 35  ratings%         46
# 36  ratings%         65
# 37  ratings%         55
# 38  ratings%         81
# 39  ratings%         71   
    
print(pd.melt(df,id_vars=['genre']))     
    
# id_vars ni andar raheli column ne according data set kari ne apse
    
#          genre  variable  value
# 0      action      year   2008
# 1      action      year   2007
# 2      action      year   2009
# 3      action      year   2008
# 4   adventure      year   2010
# 5   adventure      year   2009
# 6   adventure      year   2008
# 7      comedy      year   2007
# 8      comedy      year   2008
# 9      comedy      year   2009
# 10     action    budget     28
# 11     action    budget    200
# 12     action    budget     32
# 13     action    budget     10
# 14  adventure    budget     18
# 15  adventure    budget     20
# 16  adventure    budget     15
# 17     comedy    budget     66
# 18     comedy    budget     56
# 19     comedy    budget     52
# 20     action  ratings%     48
# 21     action  ratings%     57
# 22     action  ratings%     82
# 23     action  ratings%     56
# 24  adventure  ratings%     75
# 25  adventure  ratings%     46
# 26  adventure  ratings%     65
# 27     comedy  ratings%     55
# 28     comedy  ratings%     81
# 29     comedy  ratings%     71

print(pd.melt(df,id_vars=['year'],value_vars=['genre']))     
    
# ahi year na according gener ne variable dhyan ma rakjhi ne badho data apvama ave che 

#    year variable      value
# 0  2008    genre     action
# 1  2007    genre     action
# 2  2009    genre     action
# 3  2008    genre     action
# 4  2010    genre  adventure
# 5  2009    genre  adventure
# 6  2008    genre  adventure
# 7  2007    genre     comedy
# 8  2008    genre     comedy
# 9  2009    genre     comedy
    
print(pd.melt(df,id_vars=['year'],value_vars=['ratings%']))
    
#    year  variable  value
# 0  2008  ratings%     48
# 1  2007  ratings%     57
# 2  2009  ratings%     82
# 3  2008  ratings%     56
# 4  2010  ratings%     75
# 5  2009  ratings%     46
# 6  2008  ratings%     65
# 7  2007  ratings%     55
# 8  2008  ratings%     81
# 9  2009  ratings%     71
    
print(pd.melt(df,id_vars=['year'],value_vars=['ratings%'],var_name='category',value_name='data'))  

# var_name thi variable name ne name api shakay ane value name ne te varuable ni value ne name apoi shakay

#     year  category  data
# 0  2008  ratings%    48
# 1  2007  ratings%    57
# 2  2009  ratings%    82
# 3  2008  ratings%    56
# 4  2010  ratings%    75
# 5  2009  ratings%    46
# 6  2008  ratings%    65
# 7  2007  ratings%    55
# 8  2008  ratings%    81
# 9  2009  ratings%    71
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    