import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

# Data
data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "TestScore": [40, 50, 60, 70, 80],
}
df = pd.DataFrame(data)

# Standard Scaler
standard_scaler = StandardScaler()
standard_scaled = standard_scaler.fit_transform(df)
print("Standard Scaler Output:")
print(pd.DataFrame(standard_scaled, columns=["StudyHours", "TestScore"]))


minmax_scaler = MinMaxScaler()
minmax_scaled = minmax_scaler.fit_transform(df)
print("MinMax Scaled Output:")
print(pd.DataFrame(minmax_scaled, columns=["StudyHours", "TestScore"]))


x = df[["StudyHours"]]
y = df[["TestScore"]]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=40)
print("Training Features (x_train):")
print(x_train)

print("Testing Features (x_test):")
print(x_test)

print("Training Labels (y_train):")
print(y_train)

print("Testing Labels (y_test):")
print(y_test)
