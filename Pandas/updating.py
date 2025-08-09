# updating 
import pandas as pd
data = {
    "Name":["Saim","Ahmer","Ashar","Bilal","Hurais","Haris"],
    "Age":[10,20,30,40,50,60],
    "Salary":[1000,2000,3000,4000,5000,6000],
    "Performance score":[100,200,300,400,500,600]
}
df = pd.DataFrame(data)
print(df)
print("---------------")
#.loc[]
# df.loc[row_index,"column name"] = new_value
df.loc[0,"Salary"] = 400
print(df)