"""
Men Absolute error
1 tke the mistake difference
2 remove the minus sign
3 add
4 divide
7.5 on average

MSE Mean squared error
1 mistakes square them 
2 add 
3 divide total

MSE= 62.5

RMSE
Root mean squared error"""

from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# real scores
real_scores= [90, 60, 80, 100]
 #model guess
predicted_scores= [85,70,70,95]

mae = mean_absolute_error(real_scores, predicted_scores)
mse = mean_squared_error(real_scores, predicted_scores)
rmse = np.sqrt(mse)

print("MAE: On average off by: ", mae)
print("MSE: On average off by: ", mse)
print("RMSE: On average off by: ", rmse)