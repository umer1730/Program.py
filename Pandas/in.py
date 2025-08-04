import pandas as pd
df = pd.read_json("sample_Data.json")
print("Displaying the info of data set")
print(df.info()) 
print("----------")
print("-----**-----")

import pandas as pd
data= {
    "Name":["Saim","Babar","Rizwan"],
    "Age":[10,20,30],
    "City":["London","Karachi","Peshawer"]
}
df = pd.DataFrame(data)
print("Displaying the info of data set")
print(df.info()) 