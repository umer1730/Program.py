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
# increase salary by 5%
df["Salary"] = df["Salary"]*1.05
print(df)

import pandas as pd

data= {
    "employee_id": [3,90,9,60,49,43],
    "name": ["Bob","Alice","Tatiana","Annabelle","Jonathan","Khaled"],
    "department": ["operations","Sales","Engineering","InformationTechnology","HumanResources","Administration"],
    "salary": [48675,11096,33805,37678,23793,40454]
}
df = pd.DataFrame(data)
result =df.head(3)
print(result)

print()

result =df.tail(3)
print(result)