import matplotlib.pyplot as plt
x=[10,20,30,40,50,60,70]    # 40 is median
plt.boxplot(x)
plt.show()


x=[10,20,30,40,50,60,70]    # 40 is median
plt.boxplot(x,notch=True) # give v shape box
plt.show()


x=[10,20,30,40,50,60,70]    # 40 is median
plt.boxplot(x,vert=False)
plt.show()

x=[10,20,30,40,50,60,70]    # 40 is median
plt.boxplot(x,widths=0.5)
plt.show()



x=[10,20,30,40,50,60,70]    # 40 is median
plt.boxplot(x,labels=["python"])
plt.show()

x=[10,20,30,40,50,60,70]    # 40 is median
plt.boxplot(x,patch_artist=True)    #give color
plt.show()

x=[10,20,30,40,50,60,70]    # 40 is median
plt.boxplot(x,patch_artist=True,showmeans=True) # give means a dot
plt.show()


x=[10,20,30,40,50,60,70,120]    # outlier 120
plt.boxplot(x)
plt.show()

x=[10,20,30,40,50,60,70,120]    # 40 is median
plt.boxplot(x,whis=2) #join with outlier
plt.show()

x=[10,20,30,40,50,60,70,120]    # 40 is median
plt.boxplot(x,labels=["python"],sym="g+")
plt.show()

x=[10,20,30,40,50,60,70]    # 40 is median
plt.boxplot(x,sym="g+",boxprops=dict(color="r"),capprops=dict(color="g"))
plt.show()


x=[10,20,30,40,50,60,70]    # 40 is median
plt.boxplot(x,boxprops=dict(color="r"),capprops=dict(color="g"),whiskerprops=dict(color="b"))
plt.show()


x=[10,20,30,40,50,60,70]    # 40 is median
plt.boxplot(x,boxprops=dict(color="r"),capprops=dict(color="g"),whiskerprops=dict(color="b"),flierprops=dict(markeredgecolor="y"))
plt.show()

x=[10,20,30,40,50,60,70]   # 40 is median
x1=[10,20,40,50,30,60,90]
plt.boxplot(x,boxprops=dict(color="r"),capprops=dict(color="g"),whiskerprops=dict(color="b"),flierprops=dict(markeredgecolor="y"))
plt.boxplot(x1,boxprops=dict(color="r"),capprops=dict(color="g"),whiskerprops=dict(color="b"),flierprops=dict(markeredgecolor="y")) 
plt.show()


x=[10,20,30,40,50,60,70]   # 40 is median
x1=[10,20,40,50,30,60,90]
y=[x,x1]
plt.boxplot(y,boxprops=dict(color="r"),capprops=dict(color="g"),whiskerprops=dict(color="b"),flierprops=dict(markeredgecolor="y"))
 
plt.show()