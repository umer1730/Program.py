# jb bhi apko koi particular reason dekhana ha ke iske andr ye km ho raha ha to fill between ko use krte ha
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[1,2,3,5,4]
plt.plot(x,y,color="r")
plt.fill_between(x,y)
plt.title("Python")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()


x=[1,2,3,4,5]
y=[1,2,3,4,5]
plt.plot(x,y,color="r")
plt.fill_between(x=[2,4],y1=2,y2=4)
plt.title("Python")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show() 

import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([1,2,3,4,5])
plt.plot(x,y,color="r")
plt.fill_between(x,y,color="g",where=(x>=2) & (x<=4),alapha=0.5)    #alpha is optional
plt.title("Python")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()