import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
var = sns.load_dataset('penguins')
print(var)

print()
# if we want to print x and y
sns.barplot(x=var.island,y =var.bill_length_mm)
plt.show()

# same print but method diff
sns.barplot(x="island",y ="bill_length_mm",data=var)
plt.show()
# In Seaborn, the hue parameter is used to introduce a third dimension to a plot by coloring elements based on the values of a specified categorical or numerical variable. It allows for the visual representation of relationships and distinctions within different subgroups of data.
sns.barplot(x="island",y ="bill_length_mm",data=var,hue="sex")
plt.show()
# order parameter is used for changing orgers
order_1=["Dream","Torgersen","Biscoe"]
sns.barplot(x="island",y ="bill_length_mm",data=var,hue='sex',order=order_1)
plt.show()

# if we change male and female
order_1=["Dream","Torgersen","Biscoe"]
sns.barplot(x="island",y ="bill_length_mm",data=var,hue='sex',order=order_1,hue_order=["Female","Male"])
plt.show()

#now add parameter for changing interval size b/w 0 to 100
order_1=["Dream","Torgersen","Biscoe"]
sns.barplot(x="island",y ="bill_length_mm",data=var,hue='sex',order=order_1,hue_order=["Female","Male"],ci= 20)
plt.show()

# n_boot is also change size but show only half line
order_1=["Dream","Torgersen","Biscoe"]
sns.barplot(x="island",y ="bill_length_mm",data=var,hue='sex',order=order_1,hue_order=["Female","Male"],ci= 20,n_boot=2)
plt.show()

# now add para to show graph ver and hor
order_1=["Dream","Torgersen","Biscoe"]
sns.barplot(x="island",y ="bill_length_mm",data=var,hue='sex',order=order_1,hue_order=["Female","Male"],ci= 20,n_boot=2,orient="v")
plt.show()
# change variables and find graph ver and hor
order_1=["Dream","Torgersen","Biscoe"]
sns.barplot(x="bill_depth_mm",y ="bill_length_mm",data=var,orient="v")
plt.show()
# now hor
order_1=["Dream","Torgersen","Biscoe"]
sns.barplot(x="bill_depth_mm",y ="bill_length_mm",data=var,orient="h")
plt.show()
# add and change color
order_1=["Dream","Torgersen","Biscoe"]
sns.barplot(x="bill_depth_mm",y ="bill_length_mm",data=var,color="g")
plt.show()
# add palette for changing color
order_1=["Dream","Torgersen","Biscoe"]
sns.barplot(x="bill_depth_mm",y ="bill_length_mm",data=var,palette="icefire")
plt.show()
# and
order_1=["Dream","Torgersen","Biscoe"]
sns.barplot(x="island",y ="bill_length_mm",data=var,hue='sex',order=order_1,hue_order=["Female","Male"],ci= 20,n_boot=2,orient="v",palette="icefire")
plt.show()

# add saturation para for blur color
order_1=["Dream","Torgersen","Biscoe"]
sns.barplot(x="island",y ="bill_length_mm",data=var,hue='sex',order=order_1,hue_order=["Female","Male"],orient="v",saturation=10)
plt.show()

# add errcolor and errwidth
order_1=["Dream","Torgersen","Biscoe"]
sns.barplot(x="island",y ="bill_length_mm",data=var,hue='sex',order=order_1,hue_order=["Female","Male"],orient="v",saturation=10,errcolor='y',errwidth=10)
plt.show()

# add capsize 
order_1=["Dream","Torgersen","Biscoe"]
sns.barplot(x="island",y ="bill_length_mm",data=var,hue='sex',order=order_1,hue_order=["Female","Male"],orient="v",saturation=10,errcolor='b',capsize=1)
plt.show()

# add dodge method for show only one bar
order_1=["Dream","Torgersen","Biscoe"]
sns.barplot(x="island",y ="bill_length_mm",data=var,hue='sex',order=order_1,hue_order=["Female","Male"],orient="v",saturation=10,errcolor='b',dodge=False) # we can't add true becauae it is already present
plt.show()

# add alpha for light color
order_1=["Dream","Torgersen","Biscoe"]
sns.barplot(x="island",y ="bill_length_mm",data=var,hue='sex',order=order_1,hue_order=["Female","Male"],orient="v",saturation=10,errcolor='b',alpha=0.5) 
plt.show()

# if we do not want to matplotlib grid then use seaborn grid
sns.set(style='darkgrid')
order_1=["Dream","Torgersen","Biscoe"]
sns.barplot(x="island",y ="bill_length_mm",data=var,hue='sex',order=order_1,hue_order=["Female","Male"],orient="v",saturation=10,errcolor='b') 
plt.show()