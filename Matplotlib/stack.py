import matplotlib.pyplot as plt
x=[1,2,3,4,5]
area=[2,3,2,5,4]
plt.stackplot(x,area)
plt.show()


x=[1,2,3,4,5]
area1=[2,3,2,5,4]
area2=[2,3,4,5,3]
area3=[2,1,3,2,4]
plt.stackplot(x,area1,area2,area3)
plt.show()


x=[1,2,3,4,5]
area1=[2,3,2,5,4]
area2=[2,3,4,5,3]
area3=[2,1,3,2,4]
l=["area1","area2","area3"]
plt.stackplot(x,area1,area2,area3,labels=l)
plt.legend()
plt.show()

x=[1,2,3,4,5]
area1=[2,3,2,5,4]
area2=[2,3,4,5,3]
area3=[2,1,3,2,4]
l=["area1","area2","area3"]
plt.stackplot(x,area1,area2,area3,labels=l,colors=["r","g","y"])
plt.legend(loc=2)
plt.show()


x=[1,2,3,4,5]
area1=[2,3,2,5,4]
area2=[2,3,4,5,3]
area3=[2,1,3,2,4]
l=["area1","area2","area3"]
plt.stackplot(x,area1,area2,area3,labels=l,colors=["r","g","y"],baseline="sym")   # baseline "wiggle"
plt.title("python")
plt.legend(loc=2)
plt.show()

x=[1,2,3,4,5]
area1=[2,3,2,5,4]
area2=[2,3,4,5,3]
area3=[2,1,3,2,4]
l=["area1","area2","area3"]
plt.stackplot(x,area1,area2,area3,labels=l,colors=["r","g","y"],baseline="zero")   # baseline "wiggle"
plt.title("python")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend(loc=2)
plt.show()