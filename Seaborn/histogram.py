import matplotlib.pyplot as plt
import seaborn as sns
import pandas  as pd
var= sns.load_dataset('penguins')
print(var)

# var 
sns.displot(var['bill_length_mm'])
plt.show()

# add bins for changing data with yourself
sns.displot(var['flipper_length_mm'],bins=[170,180,190,200,210,220,230,240])
plt.show()

# we did'nt arrange data we write simple
sns.displot(var['flipper_length_mm'])
plt.show()

# now add kde (kernel density eliminator) para
sns.displot(var['flipper_length_mm'],kde=True)
plt.show()

# add rug parameter for adding lines in under
sns.displot(var['flipper_length_mm'],kde=True,rug=True)
plt.show()
# add color para for change color
sns.displot(var['flipper_length_mm'],kde=True,rug=True,color='g')
plt.show()

# add log scale isme ap ka sara data log scale me convert ho gya ha
sns.displot(var['flipper_length_mm'],kde=True,rug=True,color='g',log_scale=True)
plt.show()
# add grid and also for many same func if you want to add
sns.displot(var['flipper_length_mm'],kde=True,rug=True,color='g',log_scale=True)
plt.grid()
plt.show()



