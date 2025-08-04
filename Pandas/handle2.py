import pandas as pd
data = {
    "Name":["Saim",None,"Ahmer","Ashar","Bilal","Hurais","Haris"],
    "Age":[10,20,None,30,40,50,60],
    "Salary":[1000,2000,None,3000,4000,5000,6000],
    "Performance score":[100,None,200,300,400,500,600]
}
df = pd.DataFrame(data)
print(df)
print("-------")
#df.fillna(0,inplace=True)
df["Age"].fillna(df["Age"].mean(),inplace=True)
df["Salary"].fillna(df["Salary"].mean(),inplace = True)
print(df)