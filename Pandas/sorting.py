#sorting data
# sorting data 1 column sort_values()
# df.sort_values(by="Column Name",True/False,inplace = True)
import pandas as pd
data = {
    "Name":["Argun","Varun","Karan"],
    "Age":[28,34,22],
    "Salary":[10000,20000,30000]
}
df = pd.DataFrame(data)
df.sort_values(by="Age", ascending=True,inplace = True)
print("Sorted age by ascending")
print(df)
print("-----****-----")
df.sort_values(by=["Age","Salary"], ascending=[True,False],inplace = True)
print("Sorted age by ascending")
print(df)
