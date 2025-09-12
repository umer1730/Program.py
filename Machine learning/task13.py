import pandas as pd
from sklearn.preprocessing import LabelEncoder
data = {'name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David']}
df = pd.DataFrame(data)
le= LabelEncoder()
le.fit_transform(df["name"])
print(le.fit_transform(df["name"]))
# data encoding

print("-------------")
print()
df["en_name"]=le.fit_transform(df["name"])
print(df)