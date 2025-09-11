import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

data= pd.read_csv("student-Sheet1.csv")

x= data[["Hours"]]
y= data[["Score"]]

model=LinearRegression()
model.fit(x,y)

predicted_score = model.predict(x)

#evaluate
mae= mean_absolute_error(y, predicted_score)
mse= mean_squared_error(y, predicted_score)
rmse= np.sqrt(mse)

#show results
print("Mean Absolute Error: ", mae)
print("Mean Squared Error: ", mse)
print("Root mean squared Error: ", rmse)

# new_hour=float(input("Enter a hour: "))
# new_pred=model.predict(new_hour)
# print(f"Prediction for {new_hour} is score = {new_pred}") 


# now addd
new_prediction= model.predict([[7]])
print(f"Predicted score for 7 hours", new_prediction)