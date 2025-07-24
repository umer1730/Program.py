mark1= 10
mark2= 12
mark3= 13
mark4= 14
mark5= 15
print(mark1)
print(mark2)
print(mark3)
print(mark4)
print(mark5)
print("--------------")                    # only to see easy
# it is too large so instead of this i use numpy
# one dimensonal array
import numpy as np
marks_1d = np.array([10,12,13,14,15])
print(marks_1d)
print("--------------")

# two dimensional array
import numpy as np
marks_2d = np.array([[1,2,3],
                    [4,5,6]])
print(marks_2d)
print("--------------")


#multi dimensional array
import numpy as np
matrix = np.array([[[2,46,6],
                   [8,10,11],
                   [7,8,9]]])
print(matrix)