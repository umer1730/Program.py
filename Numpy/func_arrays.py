# search
import numpy as np
arr = np.array([1,2,3,4,2,5,2,6,2,7])
x = np.where(arr == 2)   # give acc to index
print(x)
print()

import numpy as np
arr = np.array([4,2,3,4,2,5,2,6,2,7])
x = np.where((arr/2) == 0)  # give acc to index
print()   
x_1 = np.where((arr%2) == 0)   # give acc to index
print(x)
print(x_1)
print()

# search sorted
import numpy as np
var = np.array([1,2,3,4,6,7,8])
#index          0 1 2 3 4 5 6
x_1 = np.searchsorted(var,5)
print(x_1)
print()

import numpy as np
var = np.array([1,2,3,4,8,9,10])
#index          0 1 2 3 4 5 6
x_1 = np.searchsorted(var,[5,6,7],side= "right")
print(x_1)
print()

# sort-array
import numpy as np
arr = np.array([1,2,33,4,2,52,2,61,72,7])
alpha = np.array(["s","a","d","n"])
print(np.sort(arr))
print(np.sort(alpha))
print()

# 2d
import numpy as np
arr = np.array([[1,2,33,4],[22,61,72,7]])
print(np.sort(arr))
print()

# filter array
import numpy as np
alpha = np.array(["s","a","d","n"])
f = [True,False,False,True]
new_alpha = alpha[f] 
print(new_alpha)