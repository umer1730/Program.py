#subplot functions
import matplotlib.pyplot as plt
# fig,ax = plt.subplots(nrow,ncol,figsize=(width,height))
fig,ax = plt.subplots(1,2,figsize=(10,5))

x=[1,2,3,4]
y=[10,20,15,25]
 # now you can add color
ax[0].plot(x,y,color="blue")
ax[0].set_title("line Plot")

ax[1].bar(x,y,color="green")
ax[1].set_title("Bar chart")

fig.suptitle("Comparison of line and bar charts")
#plt.tight_layout()
plt.tight_layout()

plt.show()