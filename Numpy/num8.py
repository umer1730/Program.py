import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr.ravel())         
print(arr.flatten())
print("-------------")

import numpy as np 
arr = np.array([10,20,30,40])
print(arr)
new_arr = np.insert(arr,2,100)
print(new_arr)
print("-------------")

# 2d
import numpy as np
arr_2d = np.array([[1,2],[3,4]])
print(arr_2d)
new_arr_2d = np.insert(arr_2d,1,[5,6],axis = None) # if axis = 1 then in 2d
print(new_arr_2d)
print()
# append
import numpy as np
arr_2d = np.array([[1,2],[3,4]])
print(arr_2d)
new_arr_2d = np.append(arr_2d,[5,6],axis = None) # if axis = 1 then in 2d
print(new_arr_2d)