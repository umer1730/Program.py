import matplotlib.pyplot as plt
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
degrees = [30,34,35,40,37,41,38]
plt.plot(days,degrees, color="blue", linestyle="--",linewidth=2,marker="o",label="Second week")
plt.title("July second week data")
plt.xlabel("Days")
plt.ylabel("Degrees")
plt.legend(loc="upper left",fontsize=12) #plt.legend()
plt.grid(color="gray",linestyle=":",linewidth=2)

#plt.lim optional
# plt.xticks optional
plt.show()