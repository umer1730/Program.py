#savefig("filenme.extension",dpi=value,bbox_inches="tight")
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,15,30]
plt.plot(x,y,color="blue",marker="o")
plt.title("simple line plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# you can also save by write folder name plt.savefig("folder_name/line_plot.png...")  otherwise automatically save
plt.savefig("line_plot.png",dpi=300,facecolor="g",bbox_inches="tight") #dpi for screen resolution
plt.show()


x=[1,2,3,4]
y=[10,20,15,30]
plt.plot(x,y,color="blue",marker="o")
plt.title("simple line plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# you can also save by write folder name plt.savefig("folder_name/line_plot.png...")  otherwise automatically save
plt.savefig("line_plot.png",dpi=300,facecolor="g",transparent=True,bbox_inches="tight") #dpi for screen resolution
plt.show()