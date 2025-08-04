# if multi group
import pandas as pd
data = {

   "Name":["Argun","Varun","Karan","ARR","TYTY"],
    "Age":[28,34,22,38,27],
    "Salary":[10000,20000,30000,45000,60000]
}
df = pd.DataFrame(data) 
grouped = df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)