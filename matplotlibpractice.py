import matplotlib.pyplot as plt

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

print("________________________1_      line plot")

days = [1,2,3,4,5,6,7,8,9,10,11,12]
temp= [32,36,36,23,26,25,36,35,34,36,40,42]

plt.plot(days,temp,color='r',marker='^',linestyle='--')
plt.axis([0,max(days),0,max(temp)])
plt.title("surat temperature")
plt.xlabel("days")
plt.ylabel("Temperature")

plt.show()

 






















