# dtype
import numpy as np
arr = np.array([1,2,3.4,2.5,5])
print(arr.dtype)
print("-------------")

# astype
import numpy as np
arr = np.array([1.2,2.4,3.8])
print(arr.dtype)
int_arr = arr.astype(int)
print(int_arr)
print("Converting into",int_arr.dtype)
print("-------------")

# new
import numpy as np
x = np.array([1,2,3,4],dtype=np.int8)
print("Data type:",x.dtype)
print(x)
print("-------------")

# converting into float
import numpy as np
x1 = np.array([1,2,3,4],dtype="f") # converting into float
print("Data type:",x1.dtype)
print(x1)