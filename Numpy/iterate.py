import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print()
for i in arr:
    print(i) 
print("-----------")
print()

# 2D
arr_2 = np.array([[1,2,3],[4,5,6]])
print(arr_2)
print()
for j in arr_2:
    print(j)
print()

# if you want in a row
arr_2 = np.array([[1,2,3],[4,5,6]])
print(arr_2)
print()
for j in arr_2:
    print(j)
print()
for k in arr_2:
    for l in k:
        print(l)
print("--------")
print()

# 3D
arr_3 = np.array([[[1,2],[3,4],[5,6]]])
print(arr_3)
print(arr_3.ndim)
print()
for i in arr_3:
    for j in i:
        for k in j:
            print(k)
print("---------")
print()

arr_3 = np.array([[[1,2],[3,4],[5,6]]])
print(arr_3)
print(arr_3.ndim)
print()
for i in np.nditer(arr_3,flags=["buffered"],op_dtypes="S"):
    print(i)
print()

arr_3 = np.array([[[1,2],[3,4],[5,6]]])
print(arr_3)
for i,d in np.ndenumerate(arr_3):
    print(i,d)