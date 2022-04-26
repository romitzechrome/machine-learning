from importlib.metadata import PathDistribution
import numpy as np
import matplotlib.pyplot as plt

arr_1 = np.array([[1,2,3],[1,2,3]])
print(arr_1)

# for checking array dimensions
print(arr_1.ndim)
# 2
print(type(arr_1))

print(arr_1.size)
# 6
print(arr_1.shape)
# (2, 3)
print(arr_1.dtype)
# int32

mx_1s = np.ones(5)
print(mx_1s) 
# [1. 1. 1. 1. 1.]

mx_1s = np.ones((3,4))
print(mx_1s)
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

mx_2 = np.ones((3,4),dtype=int)
print(mx_2)
# [[1 1 1 1]
#  [1 1 1 1]
#  [1 1 1 1]]

mx_0 = np.zeros((3,4))
print(mx_0)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]


MX_OS = np.zeros((3,4),dtype=bool)
print(MX_OS)
# [[False False False False]
#  [False False False False]
#  [False False False False]]

mx_os = np.zeros((3,4),dtype=str)
print(mx_os)
# [['' '' '' '']
#  ['' '' '' '']
#  ['' '' '' '']]

em_mx = np.empty((3,3))
print(em_mx)
# [[6.23042070e-307 1.60217812e-306 1.78020169e-306]
        #  [8.45593934e-307 9.34605716e-307 1.60218491e-306]
#  [1.02360867e-306 1.29062229e-306 3.91792476e-317]]

 
arange_1x = np.arange(1,13)
print(arange_1x)
# [ 1  2  3  4  5  6  7  8  9 10 11 12]

even_x = np.arange(1,13,2)
print(even_x)
# [ 1  3  5  7  9 11]

lime_space = np.linspace(1,5,5)
print(lime_space)
# [1. 2. 3. 4. 5.]

lime_space = np.linspace(1,5,4)
print(lime_space)
# [1.         2.33333333 3.66666667 5.        ]
# 1 thi 5 na 4 sarkha bhag kare

arr_2d = arange_1x.reshape(2,6)
print(arr_2d)
# array ne reshape ma convert kare jetla dimentional no array banavvo hoy atla no banavi de 
# [[ 1  2  3  4  5  6]
#  [ 7  8  9 10 11 12]]

arr_2d = arange_1x.reshape(3,4)
print(arr_2d)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

ar_3d = arange_1x.reshape(2,3,2)
print(ar_3d)
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]

#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]

ar = np.arange(1,13).reshape(2,6)
print(ar)
# [[ 1  2  3  4  5  6]
#  [ 7  8  9 10 11 12]]

onr_d = ar.ravel()
print(onr_d)
# multidimentional array ne one d ma convert kari de 
# [ 1  2  3  4  5  6  7  8  9 10 11 12]

    
row_to_col =  ar.transpose()
# row_to_col = ar.T
print(row_to_col)
# row ne column ma convert kari de 
# [[ 1  7]
#  [ 2  8]
#  [ 3  9]
#  [ 4 10]
#  [ 5 11]
#  [ 6 12]]

array_1d = np.arange(1,10).reshape(3,3)
array_2d = np.arange(1,10).reshape(3,3)
print(array_1d)
print(array_2d)

sum_2 = array_1d + array_2d 
print("summmmmmmmmm",sum_2)
# [[ 2  4  6]
#  [ 8 10 12]
#  [14 16 18]]

sum_2 = np.add(array_1d, array_2d)
print("OOOOO",sum_2)
# [[ 2  4  6]
#  [ 8 10 12]
#  [14 16 18]]

sub_2 = array_1d - array_2d
print(sub_2)
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]
# sub_2 = np.substract(array_1d, array_2d)
# print("ssssssssss",sub_2)

div_2 = np.divide(array_1d, array_2d)
print("DDDDDDDDD",div_2)
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

div_2 = array_1d / array_2d
print(div_2)
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

mul_2 = array_1d  * array_2d
print(mul_2)
# [[ 1  4  9]
#  [16 25 36]
#  [49 64 81]]

dot_2 = np.dot(array_1d, array_2d)
print("DOOOT",dot_2)
# [[ 30  36  42]
#  [ 66  81  96]
#  [102 126 150]]

mul_2 = array_1d  @ array_2d
print(mul_2)
# [[ 30  36  42]
#  [ 66  81  96]
#  [102 126 150]]

print("max number in array_one",array_1d.max())
# max number in array_one 9

print("max number index number in  array_one",array_1d.argmax())
# max number ni index number apse array_one 8

print(array_1d.max(axis=0))
# axix=0 ahi 0 a column ne represent karse
# column vise check karse k a colum ni max value kai che te print karse 
# [7 8 9]

print(array_1d.max(axis=1))
# axix=1 ahi 0 a row ne represent karse
# row vise check karse k a roww ni max valyu kai che te apse 
# [3 6 9]

print(array_1d.min())
# 1

print(array_1d.min(axis = 1))
# [1 4 7]

print(np.sum(array_1d))
# 45

        
print(np.sum(array_1d,axis = 1))
# sum kare badhi row wise
# [ 6 15 24]


print(np.sum(array_1d,axis =0))   
# sum kare column wise
# array_1d = [[1 2 3]
#             [4 5 6]
#             [7 8 9]]

# [12 15 18]


print(np.mean(array_1d))
# arrayn abadh element no sum karse ane divide by len of array
# 5.0


print(np.sqrt(array_1d))
# find the squareroot of array's all elements of
# [[1.         1.41421356 1.73205081]
#  [2.         2.23606798 2.44948974]
#  [2.64575131 2.82842712 3.        ]]

 
print(np.std(array_1d))
# find the standerddevision 
# 2.581988897471611


print(np.exp(array_1d))
# find the exponent for array_1d all elements
# [[2.71828183e+00 7.38905610e+00 2.00855369e+01]
#  [5.45981500e+01 1.48413159e+02 4.03428793e+02]
#  [1.09663316e+03 2.98095799e+03 8.10308393e+03]]


print(np.log(array_1d)) 
# find the naturallog 
# [[0.         0.69314718 1.09861229]
#  [1.38629436 1.60943791 1.79175947]
#  [1.94591015 2.07944154 2.19722458]]


print(np.log10(array_1d))
# find the logbaseten 
# [[0.         0.30103    0.47712125]
#  [0.60205999 0.69897    0.77815125]
#  [0.84509804 0.90308999 0.95424251]]


# python aray slicing 

arr1 = np.arange(1,101).reshape((10,10))
print("SSSSSSSSSSSSS",arr1)
# [[  1   2   3   4   5   6   7   8   9  10]
#  [ 11  12  13  14  15  16  17  18  19  20]
#  [ 21  22  23  24  25  26  27  28  29  30]
#  [ 31  32  33  34  35  36  37  38  39  40]
#  [ 41  42  43  44  45  46  47  48  49  50]
#  [ 51  52  53  54  55  56  57  58  59  60]
#  [ 61  62  63  64  65  66  67  68  69  70]
#  [ 71  72  73  74  75  76  77  78  79  80]
#  [ 81  82  83  84  85  86  87  88  89  90]
#  [ 91  92  93  94  95  96  97  98  99 100]]

print(arr1[0,0])
# 1
# 1 ne access karva mate pelo 0 a coloumn number ane bijo zero a row number 


print(arr1[0])
# [ 1  2  3  4  5  6  7  8  9 10]
# jetlami row joti hoy teno index number 


print(arr1[:,0])
# badhi row mate : ane jetlami colun joti hot teno index number 
# but a ak onedimention array avse 
# [ 1 11 21 31 41 51 61 71 81 91]


print("qqqq",arr1[:,0:1])
# [[ 1]
#  [11]
#  [21]
#  [31]
#  [41]
#  [51]
#  [61]
#  [71]
#  [81]
#  [91]]
# twodimntion ma avse 


print(arr1[1:4,1:4])
# [[12 13 14]
#  [22 23 24]
#  [32 33 34]]

print(arr1[:,1:4])
# 1,2,3 number ni column ni all row
# [[ 2  3  4]
#  [12 13 14]
#  [22 23 24]
#  [32 33 34]
#  [42 43 44]
#  [52 53 54]
#  [62 63 64]
#  [72 73 74]
#  [82 83 84]
#  [92 93 94]]

# arr1[:]
# arr[::]
# arr[:,:]
# all metrics


print(arr1.itemsize)
# 4

print(arr1.dtype)
# int32

# ----------------------------------------------------------------------
ar1 = np.arange(1,17).reshape(4,4)
print(ar1)

# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]


ar2 = np.arange(17,33).reshape(4,4)
print(ar2)
# [[17 18 19 20]
#  [21 22 23 24]
#  [25 26 27 28]
#  [29 30 31 32]]

print(np.concatenate((ar1,ar2)))
# ar1 ane ar2 ne concatinate karva mate 
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]
#  [17 18 19 20]
#  [21 22 23 24]
#  [25 26 27 28]
#  [29 30 31 32]]

print(np.concatenate((ar1,ar2),axis=1))
# bydefault axis = 0 hoy atle column wise thay but axis 1 karvama ave tyare raw wise thay 
# raw wise concatinate thay
# [[ 1  2  3  4 17 18 19 20]
#  [ 5  6  7  8 21 22 23 24]
#  [ 9 10 11 12 25 26 27 28]
#  [13 14 15 16 29 30 31 32]]

print(np.vstack((ar1,ar2)))
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]
#  [17 18 19 20]
#  [21 22 23 24]
#  [25 26 27 28]
#  [29 30 31 32]]

print(np.hstack((ar1,ar2)))
# [[ 1  2  3  4 17 18 19 20]
#  [ 5  6  7  8 21 22 23 24]
#  [ 9 10 11 12 25 26 27 28]
#  [13 14 15 16 29 30 31 32]]

print(np.split(ar1,2))
# ar1 ne split karvano split karvano
# 2 mins ar1 na be bhag ma split karvano

# [array([[1, 2, 3, 4],
#        [5, 6, 7, 8]]), array([[ 9, 10, 11, 12],
#        [13, 14, 15, 16]])]

list1 = np.split(ar1,2)
print(type(list1))
# <class 'list'>
print(list1[0])
# [[1 2 3 4]
#  [5 6 7 8]]

print(np.split(ar1,2,axis=1))
# column wise splite karva mate 
# [array([[ 1,  2],
#        [ 5,  6],
#        [ 9, 10],
#        [13, 14]]), array([[ 3,  4],
#        [ 7,  8],
#        [11, 12],
#        [15, 16]])]


# =-------------------------------------------------------------------
print("Trignomatry functions -------------------------------------------")
print(np.sin(180))
# -0.8011526357338304

print(np.sin(90))
# 0.8939966636005579

print(np.cos(180))
# -0.5984600690578581

print(np.tan(180))
# 1.3386902103511544

x_sin = np.arange(0,3*np.pi,0.1)
# np.pi = 3.14 thay
print(x_sin)
# [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7
#  1.8 1.9 2.  2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 3.  3.1 3.2 3.3 3.4 3.5
#  3.6 3.7 3.8 3.9 4.  4.1 4.2 4.3 4.4 4.5 4.6 4.7 4.8 4.9 5.  5.1 5.2 5.3
#  5.4 5.5 5.6 5.7 5.8 5.9 6.  6.1 6.2 6.3 6.4 6.5 6.6 6.7 6.8 6.9 7.  7.1
#  7.2 7.3 7.4 7.5 7.6 7.7 7.8 7.9 8.  8.1 8.2 8.3 8.4 8.5 8.6 8.7 8.8 8.9
#  9.  9.1 9.2 9.3 9.4]

y_sin = np.sin(x_sin)
print(y_sin)
# [ 0.          0.09983342  0.19866933  0.29552021  0.38941834  0.47942554
#   0.56464247  0.64421769  0.71735609  0.78332691  0.84147098  0.89120736
#   0.93203909  0.96355819  0.98544973  0.99749499  0.9995736   0.99166481
#   0.97384763  0.94630009  0.90929743  0.86320937  0.8084964   0.74570521
#   0.67546318  0.59847214  0.51550137  0.42737988  0.33498815  0.23924933
#   0.14112001  0.04158066 -0.05837414 -0.15774569 -0.2555411  -0.35078323
#  -0.44252044 -0.52983614 -0.61185789 -0.68776616 -0.7568025  -0.81827711
#  -0.87157577 -0.91616594 -0.95160207 -0.97753012 -0.993691   -0.99992326
#  -0.99616461 -0.98245261 -0.95892427 -0.92581468 -0.88345466 -0.83226744
#  -0.77276449 -0.70554033 -0.63126664 -0.55068554 -0.46460218 -0.37387666
#  -0.2794155  -0.1821625  -0.0830894   0.0168139   0.1165492   0.21511999
#   0.31154136  0.40484992  0.49411335  0.57843976  0.6569866   0.72896904
#   0.79366786  0.85043662  0.8987081   0.93799998  0.96791967  0.98816823
#   0.99854335  0.99894134  0.98935825  0.96988981  0.94073056  0.90217183
#   0.85459891  0.79848711  0.7343971   0.66296923  0.58491719  0.50102086
#   0.41211849  0.31909836  0.22288991  0.12445442  0.02477543]

plt.plot(x_sin,y_sin)
# plt.show()


y_cos= np.cos(x_sin)
print(y_cos)
# [ 1.          0.99500417  0.98006658  0.95533649  0.92106099  0.87758256
#   0.82533561  0.76484219  0.69670671  0.62160997  0.54030231  0.45359612
#   0.36235775  0.26749883  0.16996714  0.0707372  -0.02919952 -0.12884449
#  -0.22720209 -0.32328957 -0.41614684 -0.5048461  -0.58850112 -0.66627602
#  -0.73739372 -0.80114362 -0.85688875 -0.90407214 -0.94222234 -0.97095817
#  -0.9899925  -0.99913515 -0.99829478 -0.98747977 -0.96679819 -0.93645669
#  -0.89675842 -0.84810003 -0.79096771 -0.7259323  -0.65364362 -0.57482395
#  -0.49026082 -0.40079917 -0.30733287 -0.2107958  -0.11215253 -0.01238866
#   0.08749898  0.18651237  0.28366219  0.37797774  0.46851667  0.55437434
#   0.63469288  0.70866977  0.77556588  0.83471278  0.88551952  0.92747843
#   0.96017029  0.98326844  0.9965421   0.99985864  0.99318492  0.97658763
#   0.95023259  0.91438315  0.86939749  0.8157251   0.75390225  0.68454667
#   0.60835131  0.52607752  0.43854733  0.34663532  0.25125984  0.15337386
#   0.05395542 -0.04600213 -0.14550003 -0.24354415 -0.33915486 -0.43137684
#  -0.51928865 -0.6020119  -0.67872005 -0.74864665 -0.81109301 -0.86543521
#  -0.91113026 -0.9477216  -0.97484362 -0.99222533 -0.99969304]
plt.plot(x_sin,y_cos)
# plt.show()

y_tan = np.tan(x_sin)
print(y_tan)
# [ 0.00000000e+00  1.00334672e-01  2.02710036e-01  3.09336250e-01
#   4.22793219e-01  5.46302490e-01  6.84136808e-01  8.42288380e-01
#   1.02963856e+00  1.26015822e+00  1.55740772e+00  1.96475966e+00
#   2.57215162e+00  3.60210245e+00  5.79788372e+00  1.41014199e+01
#  -3.42325327e+01 -7.69660214e+00 -4.28626167e+00 -2.92709751e+00
#  -2.18503986e+00 -1.70984654e+00 -1.37382306e+00 -1.11921364e+00
#  -9.16014290e-01 -7.47022297e-01 -6.01596613e-01 -4.72727629e-01
#  -3.55529832e-01 -2.46405394e-01 -1.42546543e-01 -4.16166546e-02
#   5.84738545e-02  1.59745748e-01  2.64316901e-01  3.74585640e-01
#   4.93466730e-01  6.24733075e-01  7.73556091e-01  9.47424650e-01
#   1.15782128e+00  1.42352648e+00  1.77777977e+00  2.28584788e+00
#   3.09632378e+00  4.63733205e+00  8.86017490e+00  8.07127630e+01
#  -1.13848707e+01 -5.26749307e+00 -3.38051501e+00 -2.44938942e+00
#  -1.88564188e+00 -1.50127340e+00 -1.21754082e+00 -9.95584052e-01
#  -8.13943284e-01 -6.59730572e-01 -5.24666222e-01 -4.03110900e-01
#  -2.91006191e-01 -1.85262231e-01 -8.33777149e-02  1.68162777e-02
#   1.17348947e-01  2.20277200e-01  3.27858007e-01  4.42757417e-01
#   5.68339979e-01  7.09111151e-01  8.71447983e-01  1.06489313e+00
#   1.30462094e+00  1.61656142e+00  2.04928417e+00  2.70601387e+00
#   3.85226569e+00  6.44287247e+00  1.85068216e+01 -2.17151127e+01
#  -6.79971146e+00 -3.98239825e+00 -2.77374930e+00 -2.09137751e+00
#  -1.64571073e+00 -1.32636433e+00 -1.08203242e+00 -8.85556937e-01
#  -7.21146876e-01 -5.78923588e-01 -4.52315659e-01 -3.36700526e-01
#  -2.28641712e-01 -1.25429598e-01 -2.47830328e-02]
plt.plot(x_sin,y_tan)
# plt.show()

# -------------------------------------------------------------

print("random sampling with numpy________________________________________________________________________________________")

print(np.random.random(1))
# random.random a a0 thi 1 vachhe ni value apse
# [0.86505405]

print(np.random.random((3,3)))
# [[0.19928357 0.44268586 0.53204323]
#  [0.69912545 0.85290663 0.95460652]
#  [0.28841353 0.86928363 0.04704651]]

print(np.random.randint(1,4))
# 1 thi 4 ni koi pan value apse 

print(np.random.randint(1,4,(4,4)))
# (4,4) a 4*4 no matrics banavse a 1 thi 4 ni vachhe ni koi pan random valyu no 
# [[2 1 1 2]
#  [1 3 2 3]
#  [1 2 2 3]
#  [3 1 1 3]]

print(np.random.randint(1,4,(2,4,4)))
# 3d array banse 2d array be var repet thay ne 3d array banavse. 
# [[[3 2 2 3]
#   [1 1 2 1]
#   [2 1 3 2]
#   [1 2 3 2]]
#  [[2 1 3 1]
#   [2 1 1 3]
#   [1 2 3 1]
#   [1 1 1 1]]]

np.random.seed(10)
print("seed",np.random.randint(1,4,(2,4,4)))
#  [[[2 2 1 1]
#   [2 1 2 2]
#   [1 2 2 3]
#   [1 2 1 3]]

#  [[1 3 1 1]
#   [1 3 1 3]
#   [3 2 1 1]
#   [3 2 3 2]]]

# seed function use karvathi dar vakhte same j value avse random valu same ave 

np.random.seed(10)
print(np.random.randint(1,4,(2,4,4)))
#  [[[2 2 1 1]
#   [2 1 2 2]
#   [1 2 2 3]
#   [1 2 1 3]]

#  [[1 3 1 1]
#   [1 3 1 3]
#   [3 2 1 1]
#   [3 2 3 2]]]


print(np.random.rand(3))
# 3 a ketli value joiye che te 
# [0.13145815 0.41366737 0.77872881]

print(np.random.rand(3,3))
# (3,3) a three by three no matrix banavi ne aperandomly
# [[0.58390137 0.18263144 0.82608225]
#  [0.10540183 0.28357668 0.06556327]
#  [0.05644419 0.76545582 0.01178803]]

print(np.random.randn(3,3))
# minus ma pan value apse 
# [[-1.58494101  1.05535316 -1.92657911]
#  [ 0.69858388 -0.74620143 -0.15662666]

#  [-0.19363594  1.13912535  0.36221796]]

x = [6,9,8,3]

print(np.random.choice(x))
# choic efunction ma rahela list ni value ape game te select kari ne ape
# 6
# 5

print(np.random.permutation(x))
# [8 9 3 6]

# ----------------------------------------------------------------------

# print("string op[eration,comparision,information___________________________________________")

ch_name = "indian ai production"

str_1 = "learning numpy"

print(np.char.add(ch_name,str_1))
# string ne array ma convert karididhi 
# array('indian_ai_productionlearning numpy',dtype='U41')

print(np.char.upper(ch_name))
# INDIAN_AI_PRODUCTION

print(np.char.lower(ch_name))
# indian_ai_production

print(np.char.center(ch_name,60,fillchar='*'))
# ********************indian_ai_production********************
# 60 charaector ni string ma ch_name ne center ma lagavani ane bakina ma * avvojoie 

print(np.char.split(ch_name))
# numpy array ma splite thase 
# ['indian', 'ai', 'production']

print(np.char.splitlines("hello\nindian"))
# "\n thi split karvanu hoy tyare splitlines no use karvama ave "
# ['hello', 'indian']

str2 = "dmy"
str3= "dmy"

print(np.char.join([":","/"],[str2,str3]))
# :peli string na badha charachet 
['d:m:y' 'd/m/y']

print(np.char.replace(ch_name,"ai","artificial inteligence"))
# ai ni jagya a artificial inteligence karvu hoy matlab string badalvi hoy tyare
# indian artificial inteligence production

print(np.char.equal(str2,str3))
# str2 = "dmy"
# str3= "dmy"
# True

print(np.char.count(str_1,"a"))
# str_1 = "learning numpy"
# 1

print(np.char.find(str_1,"nu"))
# je number ni index upar nu che te batave
# 9

