from sklearn.linear_model import LogisticRegression
x=[[1],[2],[3],[4]]
y=[0,0,1,1]
model = LogisticRegression()
model.fit(x,y)
hours= float(input("Enter: "))
result=model.predict([[hours]])[0]
if result == 1:
    print(f"Based on hours {hours}, you are likely to pass")
else:
    print(f"Based on hours {hours}, you are likely to fail")