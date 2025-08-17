# removing columns
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
#df.drop(columns = ["ColumnName"], inplace=True)
df.drop(columns=["Performance score","Age"],inplace=True)
print(df)

print()
print("-----------")
import pandas as pd

# Create a sample DataFrame with remove duplicate rows
data = {'col1': [1, 2, 3, 2, 4, 3],
        'col2': ['A', 'B', 'C', 'B', 'D', 'C']}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df_cleaned = df.drop_duplicates()
print("DataFrame after removing duplicates:")
print(df_cleaned)