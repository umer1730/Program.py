#with default values
#np.zeros(shape) (3) fir id,(3,3) 2d
import numpy as np
zeroes_array = np.zeros(3)
zeroes_array1 = np.zeros((3,4))
print(zeroes_array)
print(zeroes_array1)
print("-------**-------")

#ones(shape)
import numpy as np
ones_array = np.ones((2,3))
print(ones_array)
print("-------**-------")

# empty array
import numpy as np
emp_array = np.empty((2,3))      # previous data entered in empty array
print(emp_array)
print("-------**-------")

#Full (shape, value)
import numpy as np
filled_array = np.full((2,2),7)
print(filled_array)
print("-------**-------")

#creating sequences of numbers in numpy
#arange
#arange(start,stop,step)
import numpy as np
arr = np.arange(1,10,2)
print(arr)
print("-------**-------")

#creating identity matrices
#eye(size)
import numpy as np
identity_matrix = np.eye(4)
print(identity_matrix)
print("-------**-------")

# linspace
import numpy as np
lin_space = np.linspace(1,10,num=5)
print(lin_space)
print("-------**-------")