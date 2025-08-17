#plt.subplot(nrows, ncol,index) yaha indexing 1 se start ho gi
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,15,25]
plt.subplot(1,2,1) # 1 row, 2col, 1 subplot
plt.plot(x,y)
plt.title("Line chart")

plt.subplot(1,2,2) #1row, 2col,2supbplot
plt.bar(x,y)
plt.title("Bar chart")

  #plt.tight_layout()
plt.show()



