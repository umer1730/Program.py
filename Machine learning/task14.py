import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
size_map = {"s": 0, "m": 1, "xl": 2}
df = pd.DataFrame({"size": ["s", "m", "xl", "m", "s"]})
oe = OrdinalEncoder()
df["size_en"] = oe.fit_transform(df[["size"]])
df["size_en_map"] = df["size"].map(size_map)

print(df)
