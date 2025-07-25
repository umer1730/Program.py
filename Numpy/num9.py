# append
import numpy as np
arr = np.array([10,20,30,40])
print(arr)
new_arr = np.append(arr,[50,60,70])
print(new_arr)
print("-------------")

# concatenate
import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
new_arr = np.concatenate((arr1,arr2))
print(new_arr)
print("-------------")

# flatten array
import numpy as np
arr = np.array([10,20,30,40])
print(arr)
new_arr = np.delete(arr,1)
print(new_arr)

# 2d
import numpy as np
arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d)
new_arr_2d = np.delete(arr_2d,0,axis = 0)
print(new_arr_2d)