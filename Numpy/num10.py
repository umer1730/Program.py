# stack
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))
print("-------------")

# splitting
import numpy as np
arr = np.array([10,20,30,40,50,60])
print(np.split(arr,2))
print("-------------")

# broadcasting                                           # prices = [10,20,30]
import numpy as np                                       #  discount = 10  
prices = np.array([10,20,30])                            # final_prices = []
discount = 10                                            # for price in prices:
final_prices = prices - (prices*discount/100)            #  final_price = price-(price*discount/100)
print(final_prices)                                      # final_prices.append(final_price)
print("-------------")                                   # print(final_prices)


import numpy as np
arr = np.array([100,200,300])
result = arr * 2
print(result)

