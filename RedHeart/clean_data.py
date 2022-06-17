import pandas as pd
from pathlib import Path

df = pd.read_csv("https://raw.githubusercontent.com/TangyKiwi/Worldie/master/RedHeart/redheart_data.csv")
for i in range(len(df["age"])):
    if not df["age"][i].isnumeric():
        if df["age"][i] == "Unknown": df.at[i, "age"] = -1
        else: df.at[i, "age"] = 0

df["gender"] = df["gender"].str.lower()

filepath = Path("redheart_data_cleaned.csv")
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath, index=False)
