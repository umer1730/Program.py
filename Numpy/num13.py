import numpy as np
l = []
for i in range(1,5):
    int_1 = int(input("Enter:"))
    l.append(int_1)
print(np.array(l))
print("--------*--------")

# arithmeric operations in numpy arrays
import numpy as np
arr = np.array([1,2,3,4])
arr_add = arr + 3            # arr_add = np.add(arr,3)
print(arr_add)
print("-----*******---------")

# double array
arr1 = np.array([1,2,3,4])
arr2 = np.array([1,2,3,4])
arr_add = np.add(arr1,arr2)          # aese bhi likh skte ha! arr_add = arr1 + arr2 
print(arr_add)
print("-----*******---------")

# sub
arr1 = np.array([1,2,3,4])
arr2 = np.array([1,2,3,4])
arr_sub = arr1 - arr2         # arr_sub = np.sub(arr1,arr2)
print(arr_sub)                 #print(arr_sub)
print("-----*******---------")

# mul
arr1 = np.array([1,2,3,4])
arr2 = np.array([1,2,3,4])
arr_mul = arr1 * arr2           #arr_mul = np.mul(arr1,arr2)
print(arr_mul)                  #print(arr_mul)
print("-----*******---------")

# pow
arr1 = np.array([1,2,3,4])
arr2 = np.array([1,2,3,4])
arr_pow = arr1 ** arr2            #arr_pow=np.pow(arr1,arr2)
print(arr_pow)
print("-----*******---------")

#  mul 
arr1 = np.array([1,2,3,4])
arr2 = np.array([1,2,3,4])
arr_mul = arr1 * 3          #  arr_mul = np.mul(arr,3)       
print(arr_mul)
print("-----*******---------")

# pow 
arr1 = np.array([1,2,3,4])
arr_pow = arr1 ** 3                         #arr_pow = np.pow(arr,3)
print(arr_pow)
print("-----*******---------")

#mod
arr1 = np.array([1,2,3,4])
arr_mod = arr1 % 3              # arr_mod = np.mod(arr,3)
print(arr_mod)
print("-----*******---------")

# 2d array
arr1 = np.array([[1,2,3,4],[4,5,6,8]])
arr_mod = arr1 + 3
print(arr_mod)
print("-----*******---------")