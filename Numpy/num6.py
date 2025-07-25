# aggregate functions
import numpy as np
arr = np.array([10,20,30,40,50])
print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr))
print(np.var(arr))
print("-------------")

# indexing
import numpy as np
arr = np.array([10,20,30,40,50])
print(arr[0])
print(arr[2])
print(arr[3])
print("-------------")

# slicing
import numpy as np
arr = np.array([10,20,30,40,50,60])
print(arr[1:4])
print(arr[:3])
print(arr[::2])
print(arr[::-1])
print("-------------")