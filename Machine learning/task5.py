# Linear regression
# 1 finds a pattern in old data
# 2 straight line
# 3 y =mx + b
# 4 [[value]] 2d list
# 5 [[6]]
# 6
# [6]

from sklearn.linear_model import LinearRegression
x=[[1],[2],[3],[4],[5]]
y=[40,50,60,70,90]
model= LinearRegression

model.fit(x,y)
hours= float(input("Enter:"))
predicted_marks = model.predict([[hours]])
print(f"Based on your hours {hours} you may score around {predicted_marks}")