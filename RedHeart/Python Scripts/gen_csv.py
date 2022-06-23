from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

import warnings
# pandas doesn't like df.append, use this to stop console from being spammed with warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

with open("../Data/Database _ The RED HEART Campaign.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

div_tags = soup.find_all("div")
ids = []
for div in div_tags:
    ID = div.get("id")
    if ID is not None and "res-" in ID:
        ids.append(ID)

print(ids)

# Div Tags
# class="custom_case-display custom-tooltip [id#]"
# data-age_of_death
# data-cause_of_death
# data-charge
# data-context_of_death
# data-gender
# data-img
# data-location
# data-min_sentence
# data-rel_to_victim
# data-source1
# data-source2
# data-story
# data-victim_name
# data-year_of_death
# id

df = pd.DataFrame(columns=["id", "year", "name", "age", "gender", "cause", "charge", "context", "location", "sentence", "relation", "source1", "source2", "story"])
for id in ids:
    div = soup.find("div", {"id": id})

    year = div.get("data-year_of_death")
    name = div.get("data-victim_name")
    age = div.get("data-age_of_death")
    gender = div.get("data-gender")
    cause = div.get("data-cause_of_death")
    charge = div.get("data-charge")
    context = div.get("data-context_of_death")
    location = div.get("data-location")
    sentence = div.get("data-min_sentence")
    relation = div.get("data-rel_to_victim")
    source1 = div.get("data-source1")
    source2 = div.get("data-source2")
    story = div.get("data-story")

    data_row = {"id":id, "year":year, "name":name, "age":age, "gender":gender, "cause":cause, "charge":charge, "context":context, "location":location, "sentence":sentence, "relation":relation, "source1":source1, "source2":source2, "story":story}
    print(data_row)
    df = df.append(data_row, ignore_index=True)

filepath = Path("../redheart_data.csv")
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath, index=False)

