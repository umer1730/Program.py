# pd.merge [df1, df2, on="Column_Name", how="type of join"]
import pandas as pd
df_customers = pd.DataFrame({
    "CustomerID":[1,2,3],
    "Name":["ALi","Arslan","Alyan"]
})
# order dataframe
df_orders = pd.DataFrame({
    "CustomerID":[1,2,4],
    "Name":["Rimsha","Maryam","Fiza"]
})
df_merged = pd.merge(df_customers,df_orders,on="CustomerID",how="inner")
print("inner join")
print(df_merged)   # jin ki keys match ho gi sirf wohi data ae ga
print("------")
print()
# now outer
df_merged = pd.merge(df_customers,df_orders,on="CustomerID",how="outer")
print("outer join")
print(df_merged)    # sari ae gi
print("---**---")
print()

df_merged = pd.merge(df_customers,df_orders,on="CustomerID",how="left")
print("left join")
print(df_merged)
print("--***----")
print()

df_merged = pd.merge(df_customers,df_orders,on="CustomerID",how="right")
print("right join")
print(df_merged) 