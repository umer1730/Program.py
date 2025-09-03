import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
var = sns.load_dataset('tips')
print(var)

# 1- Seaborn figure sizes
# make box plot
sns.boxplot(y = var['total_bill'].head(10))
plt.show()

# bar plot
sns.set_style('darkgrid')   #white,whitegrid,dark,darkgrid,ticks
sns.barplot(x='day',y='total_bill',data =var)
# plt.grid()
plt.show()

# 2-  Removing axes spines

sns.set_style('white')   
sns.barplot(x='day',y='total_bill',data =var)
sns.despine() # remove line in graph
plt.show()

# 3- Figure size
sns.set_style('white')   
plt.figure(figsize=(12,6))  # change graph size
sns.barplot(x='day',y='total_bill',data =var)
sns.despine() # remove line in graph
plt.show()

# 4- change fontsize
sns.set_style('white')   
plt.figure(figsize=(12,6)) 
sns.set_context('poster',font_scale=2) # we can write paper instead of poster
sns.barplot(x='day',y='total_bill',data =var,color="r")
plt.show()
# palette para give many colors list
sns.set_style('white')   
plt.figure(figsize=(12,6)) 
sns.barplot(x='day',y='total_bill',data =var,palette='viridis')
plt.grid() # add grid
plt.show()
