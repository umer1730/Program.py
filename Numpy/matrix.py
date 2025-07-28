#array
import numpy as np
var  = np.array([[1,2,3],[4,5,6]])
print(var)
print(type(var))

# matrix 
import numpy as np
var  = np.matrix([[1,2,3],[4,5,6]])
print(var)
print(type(var))
print()

# addition
var1  = np.matrix([[1,2,3],[4,5,6]])
var2  = np.matrix([[1,2,3],[4,5,6]])
print(var1+var2)
print(var1-var2)
print()  

# matrix mul mean  dot mult
var1  = np.matrix([[1,2],[4,5]])  # in matrix 1*1+2*4=9  
var2  = np.matrix([[1,2],[4,5]])
print(var1.dot(var2))