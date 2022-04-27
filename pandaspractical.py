from importlib.metadata import PathDistribution
from msilib.schema import LaunchCondition
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os 

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


s5= pd.Series([1,2,3,4,5])
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
#  bydefault jetla ne NAN value consider na kre tena mate keepdefaultna ne False karvama aave 

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
# class vali column ma jetli nan value hase te akho row nw drop kari dese 
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






























