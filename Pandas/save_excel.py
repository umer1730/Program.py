import pandas as pd
data= {
    "Name":["Saim","Babar","Rizwan"],
    "Age":[10,20,30],
    "City":["London","Karachi","Peshawer"]
}
df = pd.DataFrame(data)
print(df)

df.to_excel("output.xlsx", index = False)      # if you don't want to index then write this otherwise remove. , index = False
print("Excel file saved successfully")