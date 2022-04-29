from importlib.metadata import PathDistribution
from tkinter import font
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

import matplotlib.image as mpimg

'''
types of charts:-
    histogram,
    bar charts,
    scatterplots,
    area plot,
    pie plot,
    error charts,
    power spectra
'''

# print("________________________1_      line plot")

# days = [1,2,3,4,5,6,7,8,9,10,11,12]
# temp= [32,36,36,23,26,25,36,35,34,36,40,42]

# style.use("ggplot")
# plt.plot(days,temp,color='r',marker='^',linestyle='--',label = "temp line")
# plt.axis([0,max(days),0,max(temp)])
# plt.title("surat temperature")
# plt.xlabel("days")
# plt.ylabel("Temperature")
# plt.legend(loc = 2)
# plt.grid(color='r',linestyle='-',linewidth=2)
# plt.show()

# --------------------------------------------------------------------------------------

# days = [1,2,3,4,5,6,7,8,9,10,11,12]
# surat_temp= [32,36,36,23,26,25,36,35,34,36,40,42]
# mumbai_temp = [32.5,36.8,36.2,33,36,35,36,25,44,26,30,32]

# style.use("ggplot")
# plt.plot(days,surat_temp,color='r',marker='^',linestyle='--',label = "sutrat temp line")

# plt.plot(days,mumbai_temp,color='b',marker='^',linestyle='--',label = "mumbai temp line")

# plt.axis([0,max(days),0,max(mumbai_temp)])

# plt.title("surat & mumbai temperature")
# plt.xlabel("days")
# plt.ylabel("Temperature")
# plt.legend(loc = 2)
# plt.grid(color='r',linestyle='-',linewidth=2)
# plt.show()

# ---------------------------------------------------------------------------------------------
# histogram graph

ml_student = np.random.randint(18,45,(100))
py_student = np.random.randint(15,40,(100))

print(ml_student)
# [23 29 31 43 24 27 24 41 31 44 22 18 21 31 26 44 39 21 19 44 31 18 25 18
#  37 23 27 19 34 35 31 41 30 32 34 37 33 33 29 30 44 40 37 38 41 36 42 40
#  20 39 40 32 38 32 20 38 38 18 23 35 36 43 27 21 36 32 37 31 24 32 20 28
#  32 28 29 24 40 21 29 27 23 22 18 33 36 23 23 41 27 26 35 34 34 34 42 40
#  28 30 21 22]
print(py_student)
# [20 22 34 28 32 24 25 24 22 20 26 20 34 25 23 38 16 29 26 33 21 38 18 16
#  22 17 30 15 38 37 27 28 27 31 32 17 25 37 26 28 31 35 16 17 18 22 39 29
#  24 18 33 29 34 39 29 32 16 22 34 29 39 29 16 39 37 35 18 38 19 19 28 22
#  34 24 23 19 18 33 28 29 25 35 37 36 15 27 21 16 21 22 33 15 35 37 29 39
#  18 34 23 15]


# plt.hist(ml_student,rwidth=0.8,histtype="bar",orientation='horizontal',color='y',label='ml_ Student',)
# plt.title('ml_student')
# plt.xlabel('Student age category')
# plt.ylabel('no of Student age ')
# plt.legend()
# plt.show()

# -----------------------

# plt.figure(figsize=(16,9))
# ## size ne change karva mate figure no use thay

# plt.hist([ml_student,py_student],rwidth=0.8,histtype="bar",orientation='vertical',color=['y','m'],label=['ml_ Student','py_student'])


# ## plt.hist(ml_student,rwidth=0.8,histtype="bar",orientation='horizontal',color='y',label='ml_ Student',)
# ## plt.hist(py_student,rwidth=0.8,histtype="bar",orientation='vertical',color='b',label='py_ Student',)

# plt.title('ml & py student')
# plt.xlabel('Student age category')
# plt.ylabel('no of Student age ')
# plt.legend()
# plt.show()

# -----------------------------------------------------------------------------------------
# bar chart 

classes = ['python','ai','ml','r','ds']
class1_stu = [30,10,20,25,10]
class2_stu = [40,5,20,20,10]
class3_stu = [35,5,30,15,15]

# plt.bar(classes,class1_stu,width=0.2,align='edge',color='y',edgecolor='m',linewidth=3,alpha=0.50,linestyle='--',label="class_1_students")

# # plt.barh(classes,class1_stu)
# # barh kari ne karvathi graph ne hoeizontaly printkari shakiye\ 
# plt.show()

# ------------------------------


# plt.bar(classes,class1_stu,width=0.2,align='edge',color='y',edgecolor='m',linewidth=3,alpha=0.50,linestyle='--',label="class_1_students")

# # plt.barh(classes,class1_stu)
# # barh kari ne karvathi graph ne hoeizontaly printkari shakiye\ \

# plt.title("bar chart of class",fontsize=15)    
# plt.xlabel("classes",fontsize=15)
# plt.ylabel("no of student",fontsize=15)
# plt.legend()
# plt.show()

# -----------------------------

# plt.bar(classes,class1_stu,width=0.2,color='y',label="class_1_students")
# plt.bar(classes,class2_stu,width=0.2,color='b',label="class_2_students")
# plt.bar(classes,class3_stu,width=0.2,color='m',label="class_3_students")


# # plt.barh(classes,class1_stu)
# # barh kari ne karvathi graph ne hoeizontaly printkari shakiye\ \

# plt.title("bar chart of class",fontsize=15)    
# plt.xlabel("classes",fontsize=15)
# plt.ylabel("no of student",fontsize=15)
# plt.legend()
# plt.show()

# ------------------------------------

# width = 0.2
# classes_index = np.arange(len(classes))

# plt.bar(classes_index,class1_stu,width,color='y',label="class_1_students")
# plt.bar(classes_index+width,class2_stu,width,color='b',label="class_2_students")
# plt.bar(classes_index+width+width,class3_stu,width,color='m',label="class_3_students")

# # plt.barh(classes,class1_stu)
# # barh kari ne karvathi graph ne hoeizontaly printkari shakiye

# plt.xticks(classes_index + width,classes)
# # xtics no use xaxis par te xaxis na name lakh=v amte thay 

# plt.title("bar chart of class",fontsize=15)    
# plt.xlabel("classes",fontsize=15)
# plt.ylabel("no of student",fontsize=15)
# plt.legend()
# plt.show()

# ---------------------------------------------

# scatter plot_____________________________________________________________
print("____________________scatter plot")

# df = pd.read_csv("data.csv")

# print(df)

# x = df["class"]
# y = df["sleeping hour"]

# # plt.figure(figsize=(16,9))
# plt.scatter(x,y,color="black",marker="*")
# plt.xlabel("class")
# plt.ylabel("sleeping hour")
# plt.show()

# ---------------------------------------

# df = pd.read_csv("data.csv")

# print(df)

# x = df["class"]
# y = df["sleeping hour"]

# # plt.figure(figsize=(16,9))
# plt.scatter(x,y,color="black",marker="*",label="sleeping hour")
# plt.scatter(x,df["studthours"],color="y",marker=">",label="studthours")
# plt.xlabel("class")
# plt.ylabel("sleeping hour & studthours")
# plt.legend(loc="upper left")
# plt.show()

# -----------------------------------------------------------------
# pie chart

classes = ['python','ai','ml','r','ds']
class1_stu = [30,10,20,25,10]


# plt.pie(class1_stu,labels=classes)
# plt.show()

# -----------------
# explode=[0,0,0.1,0,0]
# # expload ma je te number ni index no data hoy tetlo bhag circle thi thodo dur thya ne slice thay jay
# colors =["c","b","r","y","g"]
# # je te arry wise colour reakhv mate colour no use thay
# textprops = {"fontsize":15}
# # pie chart ni andar rahela text ni property change karva mate 


# plt.pie(class1_stu,labels=classes,explode=explode,colors=colors,autopct="%0.1f%%",shadow = True,radius=1.4,textprops=textprops)

# # autopct="%0.1f%%" ana athi percentage show thay
# # SHADOW THI pie chart ma shadow avi jay
# # radius thi pie chart ni size bADLI SHAKAY

# plt.show()


# subplot----------------------------------------------------------------------------
# print("Subplot_______________________________________________________")


# plt.subplot(2,2,1)
# plt.pie([1])

# plt.subplot(2,2,2)
# plt.pie([1,2])

# plt.subplot(2,2,3)
# plt.pie([1,2,3])

# plt.subplot(2,2,4)
# plt.pie([1,2,3,4])

# plt.show()

# ------------------------------------
# # savefig function



# plt.pie([40,30,20])
# plt.savefig("pie_chart",dpi = 100,quality = '99',facecolor = 'g')

# # dpi a resoplution mae use thay
# # quality = graph ni quality kevi joiye che te 
# # faxecolor =  background ma kevoi colour joiy te 


# plt.show()


# dpi a resoplution mae use thay
# quality = graph ni quality kevi joiye che te 
# faxecolor =  background ma kevoi colour joiy te 

# -----------------------------------------------

# imshow
print("_________________________imshow")

# koi inage ne read karva mate 

# img = mpimg.imread("pie_chart.png")

# # img a 3d ma read karse


# print(img)

# print(type(img))
# # <class 'numpy.ndarray'>

# print(img.shape)
# # (4800, 6400, 4)

# print(img.ndim)
# # 3d aray che 
# # 3

# plt.figure(figsize=(16,9))
# plt.axis("off")
# plt.imshow(img,cmap="BuPu_r")
# plt.colorbar()
# plt.show()

# ------------------------------------------


# img = mpimg.imread("car.jpeg")

# single_channel2_img =img[::1]
# plt.imshow(single_channel2_img,cmap="hot")
# plt.colorbar()
# plt.show()




















