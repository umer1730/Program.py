#plt.bar(x,height,color="color name",width=value,label="label name")
# bar chart ko use krna ha for categories, continuously agr data a raha ha tb use ni krna 
import matplotlib.pyplot as plt
product=["A","B","C","D","E"]
sales=[1000,2000,4000,3000,5000]
# we can also make bar chart horizontally by putting plt.barh
plt.bar(product,sales,color="orange",label="Sales 2025")
plt.xlabel("product")
plt.ylabel("sales")
plt.title("Product sales comparison")
plt.legend()
plt.show()


# bar plot
import matplotlib.pyplot as plt
x=["python","c++","java","c"]
y=[85,70,67,78]
plt.xlabel("language",fontsize=15)
plt.ylabel("NO",fontsize=15)
plt.title("Total",fontsize=15)
c=["y","b","g","m"]
plt.bar(x,y,width=0.4,color=c,align="edge",edgecolor="r",linewidth=5,linestyle=":",alpha=0.5) # align is use dfo changing space check difference
plt.show()  


x=["python","c++","java","c"]
y=[85,70,67,78]
plt.xlabel("language",fontsize=15)
plt.ylabel("NO",fontsize=15)
plt.title("Total",fontsize=15)
c=["y","b","g","m"]
plt.bar(x,y,width=0.4,color=c,align="edge",edgecolor="r",linewidth=5,linestyle=":",alpha=0.5) # align is use dfo changing space check difference
plt.text(2,5,"java",fontsize=15,style="italic",bbox={"facecolor":"red"})
plt.show() 


x=["python","c++","java","c"]
y=[85,70,67,78]
plt.xlabel("language",fontsize=15)
plt.ylabel("NO",fontsize=15)
plt.title("Total",fontsize=15)
c=["y","b","g","m"]
plt.bar(x,y,width=0.4,color=c,align="edge",edgecolor="r",linewidth=5,linestyle=":") # align is use dfo changing space check difference
plt.text(2,5,"java",fontsize=15,style="italic",bbox={"facecolor":"red"})