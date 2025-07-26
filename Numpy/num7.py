# fancing
import numpy as np
arr = np.array([10,20,30,40,50,60])
print(arr[[0,2,4]])
print("-------------")

# filtering (boolean)
import numpy as np
arr =  np.array([10,20,30,40,50,60])
print(arr[arr>25])
print("-------------")

# shape
import numpy as np       
arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)
print("-------------")
print()
# reshaping and manipulaing
import numpy as np
arr = np.array([1,2,3,4,5,6])
reshaped_Arr = arr.reshape(2,3)
print(reshaped_Arr)
print(reshaped_Arr.ndim)