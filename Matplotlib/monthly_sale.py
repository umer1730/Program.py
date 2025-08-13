#  {these are all matplotlib plottting functions part}
# plt.plot  funct 1 part 
# plt.plot(x,y, color="color name",linestyle="line_style",linewidth=value,marker="marker symbol",label="label name")
import matplotlib.pyplot as plt
months = [1,2,3,4]
sales = [1000,1500,1200,1800]
plt.plot(months,sales, color="blue",linestyle="--",linewidth=2,marker="o",label="2025 sales data")
# plt.xlabel("text")  we can write
plt.xlabel("Months")
# similarly y label
plt.ylabel("sales per month")

plt.title("Monthly sales data report")  # plt.title

# plt.legend() you can also writ only this
plt.legend(loc="upper left",fontsize=12)    # ye chart me small box create kre ga jo btaega for each line marker aur color kia represent kr rahe ha
# lower right

#plt.grid() we can also only pass
plt.grid(color="gray",linestyle=":",linewidth=1)
# grid make like a chart

# plt.xlim(start,end)
plt.xlim(1,4) # hm sirf 1 se 4 tk hi chahte ha
plt.ylim(0,2000) #you can also comments lim to see the graph

plt.xticks([1,2,3,4],["M1","M2","M3","M4"])    # inko ap meaningful name de skte ho

plt.show()

 