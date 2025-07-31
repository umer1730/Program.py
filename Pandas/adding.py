# adding columns
import pandas as pd
data = {
    "Name":["Saim","Ahmer","Ashar","Bilal","Hurais","Haris"],
    "Age":[10,20,30,40,50,60],
    "Salary":[1000,2000,3000,4000,5000,6000],
    "Performance score":[100,200,300,400,500,600]
}
df = pd.DataFrame(data)
print(df)
print()
df["bonus"] = df["Salary"]*0.1
print(df)
print("---------")
# using insert()
# df.insert(loc,"column name",some_data)
df.insert(0,"Employee ID",[1,2,3,4,5,6])
print(df)