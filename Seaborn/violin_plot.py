# violin plot
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
var=sns.load_dataset('tips')
print(var)

# check konse day pr kitne logo ne bill diya
sns.violinplot(x='day',y='total_bill',data=var)
plt.show()

# add hue
sns.violinplot(x='day',y='total_bill',data=var,hue='time')
plt.show()

# line width
sns.violinplot(x='day',y='total_bill',data=var,linewidth=2)
plt.show()

# palette
sns.violinplot(x='day',y='total_bill',data=var,linewidth=2,palette='Dark2')
plt.show()

# order
sns.violinplot(x='time',y='total_bill',data=var,order=['Dinner','Lunch'])
plt.show()

# saturation
sns.violinplot(x='day',y='total_bill',data=var,linewidth=2,palette='Dark2',saturation=0.2)
plt.show()

# color
sns.violinplot(x='day',y='total_bill',data=var,linewidth=2,color='r')
plt.show()

# use split para for separate male and female
sns.violinplot(x='day',y='total_bill',data=var,hue='sex',split=True)
plt.show()

# use split para for separate male and female and add scale para {count,width,area} 
sns.violinplot(x='day',y='total_bill',data=var,hue='sex',split=True,scale='width')
plt.show()

# ver
sns.violinplot(x='total_bill',y='day',data=var,hue='sex')
plt.show()

# use inner {quartile,box,point,stick,None}
sns.violinplot(x='time',y='total_bill',data=var,order=['Dinner','Lunch'],inner='quart')
plt.show()

# make complete 
sns.violinplot(x=var['total_bill'])
plt.show()
# ver make complete 
sns.violinplot(y=var['total_bill'])
plt.show()