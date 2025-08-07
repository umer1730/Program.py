import pandas as pd
data = {
    "Name":["Saim","Ahmer","Ashar","Bilal","Hurais","Haris"],
    "Age":[10,20,30,40,50,60],
    "Salary":[1000,2000,3000,4000,5000,6000],
    "Performance score":[100,200,300,400,500,600]
}
df = pd.DataFrame(data)
high_salary = df[df["Salary"] > 2500]
print("Employee's with salary greater then 2500")
print(high_salary)
print("-----&&------")
# age greter then 15 and salary greater then 2500
filtered= df[(df["Age"] > 15) & (df["Salary"] > 2500)]
print(f"Employee list age greater then 15 + Salary greater then 2500")
print(filtered)
print("***********")

# now 
filtered_or = df[(df["Age"] > 25) | (df["Performance score"] > 200)]
print("Employee older then 25 or performance greater then 200")
print(filtered_or)