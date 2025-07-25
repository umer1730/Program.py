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
print(int_arr.dtype)

