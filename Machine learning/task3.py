from sklearn.preprocessing import LabelEncoder

import pandas as pd
df=pd.read_csv("sales_data_sample.csv")
df_label=df.copy()

le= LabelEncoder()
df_label["Gender_Encoded"] = le.fit_transform(df_label["Gender"])
df_label["Passed_Encoded"] = le.fit_transform(df_label["Passed"])
print("Label Encoded Data")
print(df_label[["Name","Gender","Gender_Encoded","Passed","Passed_Encoded"]])