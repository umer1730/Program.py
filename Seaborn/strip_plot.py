import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
var=sns.load_dataset('tips')
print(var)

# data= var must be written because without this it can not be reached day and total_bill 
sns.stripplot(x='day',y='total_bill',data=var)
plt.show()

# if we want to separatee male and female sex
sns.stripplot(x='day',y='total_bill',data=var,hue='sex')
plt.show()

# add palette para
sns.stripplot(x='day',y='total_bill',data=var,hue='sex',palette='copper')
plt.show()

# add line width for size circle
sns.stripplot(x='day',y='total_bill',data=var,hue='sex',palette='copper',linewidth=1)
plt.show()

# add edgecolor 
sns.stripplot(x='day',y='total_bill',data=var,hue='sex',palette='copper',linewidth=1,edgecolor='r')
plt.show()

# add jitter for displacement in circle
sns.stripplot(x='day',y='total_bill',data=var,hue='sex',palette='copper',linewidth=1,edgecolor='r',jitter=5)
plt.show()

# add size para for chage size
sns.stripplot(x='day',y='total_bill',data=var,hue='sex',palette='copper',linewidth=1,edgecolor='r',size=10)
plt.show()

# add marker
sns.stripplot(x='day',y='total_bill',data=var,hue='sex',palette='copper',linewidth=1,edgecolor='r',size=10,marker='<')
plt.show()

# add separate marker 
# m={'Male':'o','Female':'<'}
# sns.stripplot(x='day',y='total_bill',data=var,hue='sex',palette='copper',linewidth=1,edgecolor='r',size=10,marker='m')
# plt.show()

# add aplha para for light graph
sns.stripplot(x='day',y='total_bill',data=var,hue='sex',palette='copper',linewidth=1,edgecolor='r',size=10,alpha=0.2)
plt.show()

# if we want only one column data
sns.stripplot(x=var['total_bill'])
plt.show()

# if we want only one column data
sns.stripplot(y=var['total_bill'])
plt.show()