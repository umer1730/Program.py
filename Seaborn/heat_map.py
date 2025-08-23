# heatmap scatter plot
# heatmap dosnot work on single dimension data it work on 2 dimension array
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
var=np.linspace(1,10,20).reshape(4,5)
print(var)

# now print color data
sns.heatmap(var)
plt.show()

# now add data 
data = sns.load_dataset('anagrams')
print(data)

print()
# drop data 
x=data.drop(columns=['attnr'],axis=1)
print(x)

# heat map 
sns.heatmap(x)
plt.show()

# add var
sns.heatmap(var,vmin=0,vmax=12)
plt.show()

print()
# add head 
data = sns.load_dataset('anagrams')
x=data.drop(columns=['attnr'],axis=1).head(10)
print(x)

# add var
sns.heatmap(var,vmin=0,vmax=12,cmap='gist_heat')
plt.show()

# add annot for given number
sns.heatmap(var,vmin=0,vmax=12,cmap='gist_heat',annot=True)
plt.show()

# add ar for data
ar = np.array([['a0','a1','a2','a3','a4'],['b0','b1','b2','b3','b4']])
print(ar)
# add var
# sns.heatmap(var,vmin=0,vmax=10,cmap='PuOr',annot=ar,fmt='s')  s for string
# plt.show()
# add var
y={'fontsize':10,'color':'r'}
sns.heatmap(var,vmin=0,vmax=10,cmap='PuOr',annot=True,annot_kws=y) 
plt.show()
# add linewidth for space
y={'fontsize':10,'color':'r'}
sns.heatmap(var,vmin=0,vmax=10,cmap='PuOr',annot=True,annot_kws=y,linewidth=4) 
plt.show()
# add linecolor 
y={'fontsize':10,'color':'r'}
sns.heatmap(var,vmin=0,vmax=10,cmap='PuOr',annot=True,annot_kws=y,linewidth=4,linecolor='y') 
plt.show()
# add cbar for take bar 
y={'fontsize':10,'color':'r'}
sns.heatmap(var,vmin=0,vmax=10,cmap='PuOr',annot=True,annot_kws=y,linewidth=4,linecolor='y',cbar=False) 
plt.show()

#  remove xticks
y={'fontsize':10,'color':'r'}
sns.heatmap(var,vmin=0,vmax=10,cmap='PuOr',annot=True,annot_kws=y,linewidth=4,linecolor='y',cbar=False,xticklabels=False) 
plt.show()

#  remove y
y={'fontsize':10,'color':'r'}
sns.heatmap(var,vmin=0,vmax=10,cmap='PuOr',annot=True,annot_kws=y,linewidth=4,linecolor='y',cbar=False,xticklabels=False,yticklabels=False) 
plt.show()

#  remove y
y={'fontsize':10,'color':'r'}

v=sns.heatmap(var,vmin=0,vmax=10,cmap='PuOr',annot=True,annot_kws=y,linewidth=4,linecolor='y',cbar=False,xticklabels=False,yticklabels=False)
v.set(xlabel='python',ylabel='rate')
sns.set(font_scale=5)
plt.show()