import pandas as pd
data={
    "Name": ["Ali","Usama","Abrar","Taha","Usman"],
    "Age": [25,None,18,19,None],
    "Salary":[1000,None,2999,None,3000]        
}
df=pd.DataFrame(data)
print("Original data")
print(df)

print()
print(df.isnull().sum())
print()
print(df.isnull().sum().sum())
print("------_------")
print()
df=df.dropna()    # remove content in which missing value
print(df)       # if i place {df_drop=df.dropna(inplace=True)} then update missing dataset
df=df.dropna(inplace=True)
print(df)
print('ffffffff')

df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)
print(df)
print()
print("-----next-----")
print()
# Mode fill
df["Age"].fillna(df["Age"].mode()[0], inplace=True)
print(df)
print()
print("=========")
print(df.isnull().mean()*100)