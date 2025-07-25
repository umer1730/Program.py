# shape
import numpy as np       
arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)
print("-------------")

#size
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr.size)
print("-------------")

# ndim
import numpy as np
arr_1d = np.array([1,2,3,4,5,6])
arr_2d = np.array([[1,2,3],[4,5,6]])
arr_3d = np.array([[[1,2],[3,4],[5,6]]])
print(arr_1d)
print(arr_2d)
print(arr_3d)
print("----*****-----")
# elements
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)
print("----*****-----")

# if 10dim
arr = np.array([1,2,3,4],ndmin=10)
print(arr)               
print(arr.ndim)
