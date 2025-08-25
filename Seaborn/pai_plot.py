import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
var = sns.load_dataset('tips')
print(var)

# make pairplot
sns.pairplot(var)
plt.show()

# make pairplot by add hue
sns.pairplot(var,hue='sex')
plt.show()

# agr ap kuch hi cheso ka pair plot chahte ha to pairplot ka use kre
sns.pairplot(var,vars=['total_bill','tip'],hue='sex')
plt.show()

# apni marzi ka order set krskte ha
sns.pairplot(var,vars=['total_bill','tip'],hue='sex',hue_order=['Female','Male'])
plt.show()

# now add palette for changing color
sns.pairplot(var,vars=['total_bill','tip'],hue='sex',hue_order=['Female','Male'],palette='BuGn')
plt.show()

# ap inke variables ko change krna chahte hn ke x axis ke andr konsa ho ga y ke andr konsa
sns.pairplot(var,hue='sex',hue_order=['Female','Male'],x_vars=['total_bill','tip'])
plt.show()

# ap inke variables ko change krna chahte hn ke x axis ke andr konsa ho ga y ke andr konsa
sns.pairplot(var,hue='sex',hue_order=['Female','Male'],y_vars=['total_bill','tip'])
plt.show()

# graph ko change bhi krskte ha kind={hist,kde,reg,scatter}
sns.pairplot(var,hue='sex',hue_order=['Female','Male'],y_vars=['total_bill','tip'],kind='kde')
plt.show()

# add diag kind 
sns.pairplot(var,hue='sex',hue_order=['Female','Male'],y_vars=['total_bill','tip'],kind='kde',diag_kind='hist')
plt.show()

# ab kind order ko khatam krdo 
sns.pairplot(var,hue='sex',hue_order=['Female','Male'])
plt.show()

# use marker 
sns.pairplot(var,hue='sex',hue_order=['Female','Male'],markers=['*','<'] )
plt.show()

