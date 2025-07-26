# aggregate functions
import numpy as np
arr = np.array([10,20,30,40,50])
print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr),np.argmin(arr))   # argmin find index
print(np.max(arr),np.argmax(arr))
print(np.std(arr))
print(np.var(arr))
print(np.sqrt(arr))
print(np.sin(arr))
print(np.cos(arr))
print(np.cumsum(arr))    # e-g [1,2,3] = 1 as it then 1+2=3 then 3+3=6
print()
arr = np.array([[10,20],[40,50]])
print(np.min(arr,axis=1))  # axis =0, col
print("-------------")
print()
# indexing
import numpy as np
arr = np.array([10,20,30,40,50])
            #    0  1  2  3  4
            #   -5 -4 -3 -2 -1
print(arr[0])
print(arr[2])
print(arr[3])   #  0 1  2 3
print(arr[-5])  # -4 -3 -2 -1
print("-------------")
print()
# slicing
import numpy as np
arr = np.array([10,20,30,40,50,60])
print(arr[1:4])
print(arr[:3])
print(arr[::2])  # jump 2
print(arr[::-1])
print("-------------")
print()

# index in 2d
import numpy as np
arr = np.array([[1,2],[4,5]])
print(arr[0,1])
print()
# 3D
import numpy as np
arr = np.array([[[1,2],[4,5]]])
print(arr[0,1,1])