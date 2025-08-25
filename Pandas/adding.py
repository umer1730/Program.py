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

print()
print("--------------")

# The import statement is already at the top of your file, so you don't need to import pandas again here.
# If you are still getting "Import 'pandas' could not be resolved from source", try the following steps:
# 1. Make sure pandas is installed: pip install pandas
# 2. Restart your code editor or IDE.
# 3. Check your Python interpreter/environment settings to ensure pandas is installed in the correct environment.
# 4. If using VS Code, select the correct Python interpreter (bottom left corner or Ctrl+Shift+P > Python: Select Interpreter).

# The code below demonstrates creating a pandas Series with a custom index.
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)