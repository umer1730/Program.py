# count plot apko count krke deta ha if you wantto overall counting then count plot
# countplots plot the count the number of records by category
# bar plot apko un sbhe data ka main data deta ha
# barplots a value or metric for each cattegory(by default,barplots the mean of a variable by category)
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
var=sns.load_dataset('tips') # for all data 
print(var)

# make graph
sns.countplot(x='sex',data=var)
plt.show()

# give two var
sns.barplot(x='sex',y='size',data=var)
plt.show()   

# add hue
sns.countplot(x='sex',data=var,hue='smoker')
plt.show()
# ver
sns.countplot(y='sex',data=var,hue='smoker')
plt.show()

# add color
sns.countplot(x='sex',data=var,hue='smoker',color='g')
plt.show()
# add palette for color
sns.countplot(x='sex',data=var,hue='smoker',palette='bwr')
plt.show()
# add saturation for blur and dark color
sns.countplot(x='sex',data=var,hue='smoker',saturation=0.1)
plt.show()
