# plt.hist(data, bins=number_of_bins, color="colorname", edgecolor="black")
import matplotlib.pyplot as plt
scores=[45,34,55,76,89,68,68,90,26,78]
plt.hist(scores,bins=5,color="purple", edgecolor="black",label="Data")       # continuous data
plt.xlabel("Score Range")
plt.ylabel("Number of students")
plt.title("Score distribution of students")
plt.legend()
plt.show()



import matplotlib.pyplot as plt
import numpy as np
x=np.random.randint(10,60,(50))
print(x)
no = [22, 39, 58, 41, 30, 33, 54, 13, 59, 38, 14, 37, 11, 39, 19, 40, 34, 53, 51, 58, 15, 10, 12, 22,
27, 24, 34, 44, 39, 42, 59, 21, 29, 49, 19, 29, 19, 52, 55, 33, 59, 28, 39, 33, 31, 56, 31, 53,
39, 31]
l=[10,20,30,40,50,60]
# plt.hist(no) you can also print this only
plt.hist(no,color="r",edgecolor="b")  
plt.title("Number data")
plt.xlabel("No")
plt.ylabel("data")
plt.show()


plt.hist(no,color="r",cumulative=-1)  # cumulative reverse the plot
plt.title("Number data")
plt.xlabel("No")
plt.ylabel("data")
plt.show()

plt.hist(no,color="r",label="data",bottom=10)  # bottom 10 mean it will start from 10 instead 0
plt.title("Number data")
plt.legend()
plt.xlabel("No")
plt.ylabel("data")
plt.show()

plt.hist(no,color="r",histtype="step")  # in histtype it will remove the inner part and stepfilled fill the inner part and also write barstacked
plt.title("Number data")
plt.xlabel("No")
plt.ylabel("data")
plt.show()

plt.hist(no,color="r",orientation="horizontal")  # and vertical
plt.title("Number data")
plt.xlabel("No")
plt.ylabel("data")
plt.show()


plt.hist(no,color="b",edgecolor="yellow",label="data")  
plt.title("Number data")
plt.xlabel("No")
plt.ylabel("data")
plt.axvline(45,color="r",label="line")   # create a line and label display the line
plt.legend()
plt.show()