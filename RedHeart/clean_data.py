import pandas as pd
from pathlib import Path
import re

df = pd.read_csv("https://raw.githubusercontent.com/TangyKiwi/Worldie/master/RedHeart/redheart_data.csv")

# Age
# change all non numeric age values to 0 if under 1 year, -1 if unknown
for i in range(len(df["age"])):
    if not df["age"][i].isnumeric():
        if df["age"][i] == "Unknown": df.at[i, "age"] = -1
        else: df.at[i, "age"] = 0

# Gender
# standardize all gender types, strip() bc of "male" and "male " instances
# df.replace to fix all typos, "associate violence" case should be "male"
df["gender"] = df["gender"].str.lower()
df["gender"] = df["gender"].str.strip()
df = df.replace({"gender":{"male, fema":"male, female", "unknown gender":"unknown", "associate violence":"male"}})

# Context
# df.replace to fix all typos
df["context"] = df["context"].str.lower()
df["context"] = df["context"].str.strip()
df = df.replace({"context":{"unknown context":"unknown", "unsolved":"unknown", "unknown context of death":"unknown", "incomplete entry":"unknown", "bashing":"unknown", "domestic violece":"domestic violence", "associate vioence":"associate violence", "neighbour violence":"associate violence", "stanger violence":"stranger violence"}})

# Cause
df["cause"] = df["cause"].str.lower()
df["cause"] = df["cause"].str.strip()
df["cause"] = df["cause"].replace({"raped":"rape", "raper":"rape", "bashed":"bashing", "unknown cause of death":"unknown", "poisoned": "poison", "poisoning": "poison", "shootingg": "shooting", "tortured": "torture", "drowned": "drowning", "shaken":"shaking", "stabbbing":"stabbing", "\}":")", "\.":", "}, regex=True)
df["cause"] = df["cause"].str.replace("shooting", "shootin")
df["cause"] = df["cause"].str.replace("shootin", "shooting")
df["cause"] = df["cause"].str.replace("bombing", "bomb")
df["cause"] = df["cause"].str.replace("bomb", "bombing")
df["cause"] = df["cause"].str.replace("drug overdose", "overdose")
df["cause"] = df["cause"].str.replace("overdose", "drug overdose")
df["cause"] = df["cause"].replace({"gas poison":"gas poisoning", "unknown cause":"unknown"}, regex=True)
for i in range(len(df["cause"])):
    df.at[i, "cause"] = re.sub(r'\([^)]*\)', '', df["cause"][i])
df["cause"] = df["cause"].str.replace("asphyxiation ,stabbing", "asphyxiation, stabbing")
df["cause"] = df["cause"].str.strip()

filepath = Path("redheart_data_cleaned.csv")
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath, index=False)
