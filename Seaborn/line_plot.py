import seaborn as sns   # in seaborn we also use matplotlib for graph and also use pandas for data
import matplotlib.pyplot as plt 
import pandas as pd
var = [1,2,3,4,5,6,7]
var_1=[2,3,4,1,5,6,7]
x_1 = pd.DataFrame({"var":var, "var_1":var_1})      # sometimes we use {matplotlib} sometimes {seaborn}
sns.lineplot(x="var",y = "var_1", data = x_1)       #plt.plot(var,var_1)
plt.show()                                          #plt.show()

print()
# for simple graph
var = [1,2,3,4,5,6,7]
var_1=[2,3,4,1,5,6,7]
sns.lineplot(x=var,y = var_1)    
plt.show() 

# for put dataset
y_1 = sns.load_dataset("penguins")
var = [1,2,3,4,5,6,7]
var_1=[2,3,4,1,5,6,7]
x_1 = pd.DataFrame({"var":var, "var_1":var_1})      # sometimes we use {matplotlib} sometimes {seaborn}
sns.lineplot(x="var",y = "var_1", data = x_1)       #plt.plot(var,var_1)
plt.show()                                          #plt.show()

print()
# when check full data then comments line 4 to plt.show
# y_1=sns.load_dataset("penguins")
# print(y_1)

sns.lineplot(x="bill_depth_mm",y = "flipper_length_mm",data=y_1)
plt.show()

# if we want to add another optionthen add {hue}
sns.lineplot(x="bill_depth_mm",y = "flipper_length_mm",data=y_1,hue="sex")
plt.show()

# if we addd size then give graph according to size
sns.lineplot(x="bill_depth_mm",y = "flipper_length_mm",data=y_1,hue="sex",size=10)
plt.show()

# change style
sns.lineplot(x="bill_depth_mm",y = "flipper_length_mm",data=y_1,hue="sex",size=10,style="sex")
plt.show()

# palette give color
sns.lineplot(x="bill_depth_mm",y = "flipper_length_mm",data=y_1,hue="sex",size=10,palette="Accent")
plt.show()

# give marker
sns.lineplot(x="bill_depth_mm",y = "flipper_length_mm",data=y_1,hue="sex",palette="Accent",markers=["o","^ "])
plt.show()
# reduce data 
y_1 = sns.load_dataset("penguins").head(20)
print(y_1)

#dashes for line and legend
sns.lineplot(x="bill_depth_mm",y = "flipper_length_mm",data=y_1,hue="sex",palette="Accent",markers=["o","^ "],dashes=False,legend="full")
plt.show()
# use grid and title
sns.lineplot(x="bill_depth_mm",y = "flipper_length_mm",data=y_1,hue="sex",palette="Accent",markers=["o","^ "],dashes=False,legend="full")
plt.grid()
plt.title("python")
plt.show()