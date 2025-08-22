import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
var=sns.load_dataset('tips')
print(var)

# make graph   sns.factorplot now update to catplot
sns.catplot(x='size',y='tip',data = var)  
plt.show()

# add hue hm chahte kis male ne kitne tip di ha kis female ne kitni  
sns.catplot(x='size',y='tip',data = var,hue='sex')  
plt.show()

# add palette para
sns.catplot(x='size',y='tip',data = var,hue='sex',palette='BuPu')  
plt.show()
# height
sns.catplot(x='size',y='tip',data = var,hue='sex',palette='BuPu',height=10)  
plt.show()

# kind para                       kind={bar,box,boxen,count,point,swarm,violin}
sns.catplot(x='size',y='tip',data = var,hue='sex',kind='bar')  
plt.show()

  
