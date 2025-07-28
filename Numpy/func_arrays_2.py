# shuffle
import numpy as np
var = np.array([1,2,3,4,5])
np.random.shuffle(var)
print(var)
print()

#unique
import numpy as np
var1 = np.array([1,2,3,4,2,5,2,6,7,5,2])
x = np.unique(var1)
y = np.unique(var1,return_index=True)
z = np.unique(var1,return_index=True,return_counts=True)
print(x)
print()
print(y)
print()
print(z)
print()

# resize
import numpy as np
var1 = np.array([1,2,3,4,2,5,2,6,7,5,2])
x = np.resize(var1,(2,3))
print(x)
print()

# flatten
import numpy as np
var1 = np.array([1,2,3,4,2,5,2,6,7,5,2])
x = np.resize(var1,(2,3))
print(x)
print()
print(x.flatten())
print()
print(x.flatten(order="F")) # change order
print()  
print(np.ravel(y,order="F"))   # change order

