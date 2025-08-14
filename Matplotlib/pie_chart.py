 # pie chart represent data as part of a slices of a circle 
import matplotlib.pyplot as plt
regions=["North","South","East","West"]
revenue=[3000,2000,1500,1000]
plt.pie(revenue,labels=regions,autopct="%1.1f%%",colors=["gold","skyblue","lightgreen","coral"])
plt.title("Revenue contribution by region")
plt.show()

import matplotlib.pyplot as plt
x=[10,20,30,40]
y=["c","c++","python","java"]
ex=[0.4,0.0,0.0,0.0]
plt.pie(x,labels=y,explode=ex)
plt.show()

x=[10,20,30,40]
y=["c","c++","python","java"]
ex=[0.4,0.0,0.3,0.0]
c=["r","b","g","y"]
plt.pie(x,labels=y,explode=ex,colors=c)
plt.show()

x=[10,20,30,40]
y=["c","c++","python","java"]
ex=[0.4,0.0,0.3,0.0]
c=["r","b","g","y"]
plt.pie(x,labels=y,explode=ex,colors=c,autopct="%1.1f%%",shadow=True,radius=1.5,labeldistance=1) # labeldistance is close and far the label through diagram
plt.show()

x=[10,20,30,40]
y=["c","c++","python","java"]
ex=[0.4,0.0,0.3,0.0]
c=["r","b","g","y"]
plt.pie(x,labels=y,explode=ex,colors=c,autopct="%1.1f%%",shadow=True,radius=1.5,labeldistance=1,startangle=180,textprops={"fontsize":15},counterclock=False ) # labeldistance is close and far the label through diagram
plt.show()

x=[10,20,30,40]
y=["c","c++","python","java"]
ex=[0.4,0.0,0.3,0.0]
c=["r","b","g","y"]
plt.pie(x,labels=y,explode=ex,colors=c,autopct="%1.1f%%",shadow=True,radius=1.5,labeldistance=1,startangle=180,textprops={"fontsize":15},counterclock=False,wedgeprops={"linewidth":4,"edgecolor":"m"}) 
plt.show()


x=[10,20,30,40]
y=["c","c++","python","java"]
ex=[0.4,0.0,0.3,0.0]
c=["r","b","g","y"]
plt.pie(x,labels=y,explode=ex,colors=c,rotatelabels=False)
plt.legend(loc=2)
plt.show()


x=[10,20,30,40]
x1=[40,30,20,10]
y=["c","c++","python","java"]
plt.pie(x,labels=y,radius=1)
plt.pie(x1,radius=0.5)
plt.show()

# ring
x=[10,20,30,40]
x1=[40,30,20,10]
y=["c","c++","python","java"]
plt.pie(x,labels=y,radius=1.5)
plt.pie([1],colors="w")
plt.show()
