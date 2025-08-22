# Box plots, also known as box-and-whisker plots, are a type of data visualization used to display the distribution of quantitative data, particularly useful for comparing distributions across different categories
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
var = sns.load_dataset('tips')
print(var)

# make box plot style={whitegrid,white,ticks,dark,darkgrid}
sns.set(style='whitegrid') 
sns.boxplot(x='day',y='total_bill',data=var)
plt.show()

# make box plot style={whitegrid,white,ticks,dark,darkgrid}
sns.set(style='whitegrid') 
sns.boxplot(x='day',y='total_bill',data=var,hue='sex')
plt.show()

# add color para for chnage color
sns.set(style='whitegrid') 
sns.boxplot(x='day',y='total_bill',data=var,hue='sex',color="g")
plt.show()

# add order para if you want which day is first and second
sns.set(style='whitegrid') 
sns.boxplot(x='day',y='total_bill',data=var,hue='sex',color="g",order=["Fri",'Sun','Thu','Sat'])
plt.show()

# if you want to mean then add para
sns.set(style='whitegrid') 
sns.boxplot(x='day',y='total_bill',data=var,hue='sex',color="g",order=["Fri",'Sun','Thu','Sat'],showmeans=True)
plt.show()

#  change mean color and shape
sns.set(style='whitegrid') 
sns.boxplot(x='day',y='total_bill',data=var,hue='sex',color="g",order=["Fri",'Sun','Thu','Sat'],showmeans=True,meanprops={'marker':'o','markeredgecolor':'b'})
plt.show()

# add line width
sns.set(style='whitegrid') 
sns.boxplot(x='day',y='total_bill',data=var,hue='sex',color="g",order=["Fri",'Sun','Thu','Sat'],showmeans=True,meanprops={'marker':'o','markeredgecolor':'b'},linewidth=4)
plt.show()

# change line width color
sns.set(style='whitegrid') 
sns.boxplot(x='day',y='total_bill',data=var,hue='sex',color="g",order=["Fri",'Sun','Thu','Sat'],showmeans=True,meanprops={'marker':'o','markeredgecolor':'b'},linewidth=4,linecolor='r')
plt.show()

# palette para 
sns.set(style='whitegrid') 
sns.boxplot(x='day',y='total_bill',data=var,hue='sex',color="g",order=["Fri",'Sun','Thu','Sat'],showmeans=True,meanprops={'marker':'o','markeredgecolor':'b'},linewidth=4,palette='plasma')
plt.show()

# orient para ke through hm inko  hor aur ver bna skte ha
sns.set(style='whitegrid') 
sns.boxplot(x='day',y='total_bill',data=var,hue='sex',color="g",order=["Fri",'Sun','Thu','Sat'],showmeans=True,meanprops={'marker':'o','markeredgecolor':'b'},linewidth=4,palette='plasma',orient='v')
plt.show()  # hor me hm tb hi kr skte ha jb hmare pass x axis me string type ka data hona chahiye aur y axis me numeric data  

# like is tarah
# now this  show hor
sns.set(style='whitegrid') 
sns.boxplot(x='total_bill',y='day',data=var,hue='sex',color="g",order=["Fri",'Sun','Thu','Sat'],showmeans=True,meanprops={'marker':'o','markeredgecolor':'b'},linewidth=4,palette='plasma')
plt.show()  # hor me hm tb hi kr skte ha jb hmare pass x axis me string type ka data hona chahiye aur y axis me numeric data  

# this can show graph hor 
sns.set(style='whitegrid') 
sns.boxplot(data=var,showmeans=True,meanprops={'marker':'o','markeredgecolor':'b'},linewidth=4,palette='plasma',orient='h')
plt.show()  
# this show hor
sns.set(style='whitegrid') 
sns.boxplot(x=var['total_bill'])
plt.show()  

# this show hor
sns.set(style='whitegrid') 
sns.boxplot(y=var['total_bill'])
plt.show()  