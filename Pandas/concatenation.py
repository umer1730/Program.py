#  vertically and horizontally
import pandas as pd
df_Regional1 = pd.DataFrame({
    "CustomerID":[1,2],
    "Name":["Google","Amazon"]
}) 
df_Regiona2 = pd.DataFrame({
    "CustomerID":[3,4],
    "Name":["Alibaba","Microsoft"]
})
df_concat = pd.concat([df_Regional1,df_Regiona2],ignore_index = True) #vertically
print(df_concat)
print("---***---")
df_concat = pd.concat([df_Regional1,df_Regiona2],axis = 1,ignore_index = True) #horizontally
print(df_concat)