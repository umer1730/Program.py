# transpose
import numpy as np
var = np.matrix([[1,2,3],[4,5,6]])
print(var)
print()
print(np.transpose(var))
print()
print(var.T) # short method
print()

#swapaxes
print(np.swapaxes(var,0,1))
print()
var2=np.matrix([[1,2],[3,4]])
print(var2)
print()
print(np.swapaxes(var2,0,1))
print()

#inverse
var3 = np.matrix([[1,2],[3,4]])
print(var3)
print()
print(np.linalg.inv(var3))
print()

#power
var4 = np.matrix([[1,2],[3,4]])
print(var4)
print()
print(np.linalg.matrix_power(var4,2))
print()

# determine
var5 = np.matrix([[1,2],[3,4]])
print(var5)
print()
print(np.linalg.det(var5))
print()

var5 = np.matrix([[1,2,3],[3,4,5],[6,7,8]])
print(var5)
print()
print(np.linalg.det(var5))
print()