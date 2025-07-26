# 1d to 2d
import numpy as np
matrix = np.array([[1,2,3],[4,5,6]])
vector = np.array([1,2,3])
result = matrix + vector
print(result)
print("-------------")

# vectorization
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
result = arr1 + arr2
print(result)
print("-------------")

# isnan
import numpy as np
arr = np.array([1,2,np.nan,4,np.nan,6])
print(np.isnan(arr)) 