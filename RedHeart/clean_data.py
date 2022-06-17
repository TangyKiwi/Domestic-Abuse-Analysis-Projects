import pandas as pd
from pathlib import Path

df = pd.read_csv("https://raw.githubusercontent.com/TangyKiwi/Worldie/master/RedHeart/redheart_data.csv")

# change all non numeric age values to 0 if under 1 year, -1 if unknown
for i in range(len(df["age"])):
    if not df["age"][i].isnumeric():
        if df["age"][i] == "Unknown": df.at[i, "age"] = -1
        else: df.at[i, "age"] = 0

# standardize all gender types, strip() bc of "male" and "male " instances
# df.replace to fix all typos, "associate violence" case should be "male"
df["gender"] = df["gender"].str.lower()
df["gender"] = df["gender"].str.strip()
df = df.replace({"gender": {"male, fema":"male, female", "unknown gender":"unknown", "associate violence":"male"}})

filepath = Path("redheart_data_cleaned.csv")
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath, index=False)
