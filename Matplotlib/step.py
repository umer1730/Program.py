import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[1,2,3,5,4]
plt.step(x,y)
plt.show()


x=[1,2,3,4,5]
y=[1,2,3,5,4]
plt.step(x,y)
plt.title("python")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid()
plt.show()


x=[1,2,3,4,5]
y=[1,2,3,5,4]
plt.step(x,y,marker="o",ms=10)
plt.title("python")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid()
plt.show()

x=[1,2,3,4,5]
y=[1,2,3,5,4]
plt.step(x,y,marker="o",ms=10,mfc="g",label="python") # marker face color
plt.legend(loc=2) # loc for left side
plt.title("python")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid()
plt.show()