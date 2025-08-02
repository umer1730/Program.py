import numpy as np
var = np.array([1,2,3,4,5])
co = var.copy() 
print("var: ",var)
print("copy: ",co)
print()

# make copy with the help of view
x = np.array([3,4,5,6])
vi = x.view()
print("x:",x)
print("view:",vi)
print()

#1 copy owns the data.                      |vs|    the views does not the data.
#2 copy of an array is a new array.         |vs|    a view of the original array.
#3 the changes made in the original         |vs|    any changes made to the view will affect the original array, and any changes 
#array does't reflect in the original array.|vs|  made to the original view will affect the view.

# put value and see diff
import numpy as np
var = np.array([1,2,3,4,5])
co = var.copy() 
var[1] = 40         # put 40 in first index
print("var: ",var)  #var data changes
print("copy: ",co)  #copy does not
print()

x = np.array([3,4,5,6])
vi = x.view()
x[1] = 40
print("x:",x)
print("view:",vi)
print() 