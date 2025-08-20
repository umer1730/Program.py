# it is used for signal systems
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[2,3,5,6,9,4]
plt.stem(x,y)   # linefmt="-"
plt.show()

x=[1,2,3,4,5,6]
y=[2,3,5,6,9,4]
plt.stem(x,y,linefmt="-",markerfmt="r+") #solid line
plt.show()

x=[1,2,3,4,5,6]
y=[2,3,5,6,9,4]
plt.stem(x,y,linefmt="--",markerfmt="r o")  #dashed line
plt.show()

x=[1,2,3,4,5,6]
y=[2,3,5,6,9,4]
plt.stem(x,y,linefmt="-.")  #dashed dotted line
plt.show()

x=[1,2,3,4,5,6]
y=[2,3,5,6,9,4]
plt.stem(x,y,linefmt=":",orientation="horizontal")   #colon
plt.show()

x=[1,2,3,4,5,6]
y=[2,3,5,6,9,4]
plt.stem(x,y,linefmt="-",markerfmt="ro",bottom=2)   #colon
plt.show()

x=[1,2,3,4,5,6]
y=[2,3,5,6,9,4]
plt.stem(x,y,linefmt="-",markerfmt="ro",bottom=9,basefmt="g",label="python")   # basefmt is bottom line
plt.legend()
plt.show()