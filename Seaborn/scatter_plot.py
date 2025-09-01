import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
var=sns.load_dataset('penguins') #.head(20) add this after ()
print(var)

# add columns
sns.scatterplot(x='bill_length_mm',y='bill_depth_mm',data=var)
plt.show()

# add hue method
sns.scatterplot(x='bill_length_mm',y='bill_depth_mm',data=var,hue='sex')
plt.show()

# add style para for change sex
sns.scatterplot(x='bill_length_mm',y='bill_depth_mm',data=var,hue='sex',style='sex')
plt.show()

# add size para for change 
sns.scatterplot(x='bill_length_mm',y='bill_depth_mm',data=var,hue='sex',style='sex',size='sex')
plt.show()

# add sizes para for change size with own self 
sns.scatterplot(x='bill_length_mm',y='bill_depth_mm',data=var,hue='sex',style='sex',size='sex',sizes=(100,40))
plt.show()

# add palette for canges color {agr ap koi bhi aik random digit likh dete hn to ap ko error me colors ki list show ho jae gi phir uske according bna le} 
sns.scatterplot(x='bill_length_mm',y='bill_depth_mm',data=var,hue='sex',style='sex',size='sex',sizes=(100,40),palette='gist_ncar')
plt.show()

# now give alpha para
sns.scatterplot(x='bill_length_mm',y='bill_depth_mm',data=var,hue='sex',style='sex',size='sex',sizes=(100,40),palette='gist_ncar',alpha=0.7)
plt.show()

# now add marker
m={'Male':'*','Female':'o'}
sns.scatterplot(x='bill_length_mm',y='bill_depth_mm',data=var,hue='sex',style='sex',size='sex',sizes=(100,40),palette='gist_ncar',alpha=0.7,markers=m)
plt.show()