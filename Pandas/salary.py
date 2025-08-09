import pandas as pd
data = {
    "Name":["Saim","Ahmer","Ashar","Bilal","Hurais","Haris"],
    "Age":[10,20,30,40,50,60],
    "Salary":[100,200,300,400,500,600],
    "Performance score":[10,20,30,40,50,60]
}
df = pd.DataFrame(data)
print("Sample Dataframe")
print(df)
print("Names (Single column return series)")
name = df["Name"]
print(name)
# and if we want salary
subset = df[["Name","Salary"]]
print("\nSubset with Name and Salary")
print(subset)