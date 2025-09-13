import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
var=sns.load_dataset('tips')
print(var)

#  make graph
fg = sns.FacetGrid(var)
fg.map(plt.scatter,'total_bill','tip')
plt.show()

# make mul plot
fg = sns.FacetGrid(var,col='sex')
fg.map(plt.scatter,'total_bill','tip')
plt.show()

# now we want to separate days
fg = sns.FacetGrid(var,col='sex',hue='day')
fg.map(plt.scatter,'total_bill','tip')
plt.show()


# now we add legend to see which days
fg = sns.FacetGrid(var,col='sex',hue='day')
fg.map(plt.scatter,'total_bill','tip').add_legend()
plt.show()

# now me days wise ke according separate graph chahte ha 
fg = sns.FacetGrid(var,col='day',hue='sex')
fg.map(plt.scatter,'total_bill','tip').add_legend()
plt.show()

# bar graph with separate days
fg = sns.FacetGrid(var,col='day',hue='sex')
fg.map(plt.bar,'total_bill','tip').add_legend()
plt.show()

# bar graph
fg = sns.FacetGrid(var,col='sex',hue='day')
fg.map(plt.bar,'total_bill','tip').add_legend()
plt.show()

# palette
fg = sns.FacetGrid(var,col='sex',hue='day',palette='summer')
fg.map(plt.bar,'total_bill','tip').add_legend()
plt.show()

# edgecolor
fg = sns.FacetGrid(var,col='sex',hue='day',palette='summer')
fg.map(plt.bar,'total_bill','tip',edgecolor='g').add_legend()
plt.show()