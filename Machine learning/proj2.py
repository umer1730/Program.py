import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

# load dataset
data = pd.read_csv("D:\studies\program.py\Machine learning\students performance dataset.csv")

#input & output
x= data[["Study_Hours_per_Week"]]
y= data["Final_Scocre"]
z=data["Attendance_Percentage"]
a=data["Assignments_Completed"]
b=data["Test_Marks"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
#train model

model=LinearRegression()
model.fit(x_train, y_train)
predicted_score= model.predict(x)

# valid regression metrics
mae=mean_squared_error(y, predicted_score)
mse=mean_squared_error(y, predicted_score)
rmse=np.sqrt(mse)
r2=r2_score(y, predicted_score)

#show results
print("Mean Absolute Error (MAE): ")
print("Mean Squared Error (MSE): ")
print("Root Mean Squared Error (RMSE): ")
print("Root Mean Squared Error (RMSE): ")
print("R^2 Score (Model Accuracy): ", round(r2, 4)) #closer to 1 then better

# histogram
plt.figure(figsize=(10,6))
plt.hist(data["Final_Scocre"], bins=30, color="skyblue", edgecolor="black")
plt.title("Distribution of final exam scores")
plt.xlabel("Final exam score", fontsize= 15)
plt.ylabel("Number of students", fontsize= 15)
plt.grid(True)
plt.show()

#scatter plot
plt.figure(figsize=(10,6))
plt.scatter(x, y, color="blue", label="Actual Scores")
plt.plot(x, predicted_score, color="red", label="Predicted Scores (Regression line)")           
plt.title("Modern Prediction vs Actual Score")
plt.xlabel("Study hours per week", fontsize= 15)
plt.ylabel("Final Output", fontsize=15)
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
x_vals = np.arange(10)
y_vals = data["Attendance_Percentage"][:10]
plt.bar(x_vals, y_vals, color="blue", label="Attendance %")
plt.xticks(x_vals, [f"Student {i+1}" for i in x_vals])
plt.title("Attendance of First 10 Students")
plt.xlabel("Students",fontsize=15)
plt.ylabel("Attendance Percentage",fontsize=15)
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10,6))
plt.hist(data["Assignments_Completed"], bins=30, color="purple", edgecolor="black")
plt.title("Assignments")
plt.xlabel("Total Assignments", fontsize= 15)
plt.ylabel("Number of students", fontsize= 15)
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
x_vals = np.arange(10)
y_vals = data["Test_Marks"][:10]
plt.bar(x_vals, y_vals, color="orange", label="Marks")
plt.xticks(x_vals, [f"Student {i+1}" for i in x_vals])
plt.title("Test marks of First 10 Students")
plt.xlabel("Students",fontsize=15)
plt.ylabel("Attendance Percentage",fontsize=15)
plt.legend()
plt.grid(True)
plt.show()

new_hours = 9
predicted_new_score = model.predict([[new_hours]])
print(f"Predicted Final score for {new_hours} Hours is {predicted_new_score} score")


""" Add attendence
and many things"""