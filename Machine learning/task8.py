from sklearn.tree import DecisionTreeClassifier
x=[
    [7,2],
    [8,3],
    [9,8],
    [10,9]
]
y=[0,0,1,1]
model =DecisionTreeClassifier()
model.fit(x,y)

size=float(input("Enter the fruit size in cm: "))
shade=float(input("Enter the color shade (1 - 10): "))
result = model.predict([[size,shade]])[0]
if result == 0:
    print("This is likely an apple")
else:
    print("This is likely an orange")