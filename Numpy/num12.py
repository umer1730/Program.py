import numpy as np
arr = np.array([1,2,np.nan,4,np.nan,6])
cleaned_arr = np.nan_to_num(arr,nan=100)
print(cleaned_arr) 
print("---------------")

# isinf
import numpy as np
arr = np.array([1,2,np.inf,4,-np.inf,6])
print(np.isinf(arr)) 
print("----------------")

# convert into finite
import numpy as np
arr = np.array([1,2,np.inf,4,-np.inf,6])
print(np.isinf(arr))
cleaned_arr = np.nan_to_num(arr,posinf=1000,neginf=-1000)
print(cleaned_arr) 
print("----------------")