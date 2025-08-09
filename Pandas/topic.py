# shape (tell rows) & columns (tell col name)
import pandas as pd
data = {
    "Name":["Saim","Ahmer","Ashar","Bilal","Hurais","Haris"],
    "Age":[10,20,30,40,50,60],
    "Salary":[100,200,300,400,500,600],
    "Performance score":[10,20,30,40,50,60]
}
df = pd.DataFrame(data)
print(df)
print(f"Shape:{df.shape}")
print(f"Column Names: {df.columns}")