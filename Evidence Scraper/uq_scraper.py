import pandas as pd
import requests
from bs4 import BeautifulSoup
from pathlib import Path

import warnings
# pandas doesn't like df.append, use this to stop console from being spammed with warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

r = requests.get("https://law.uq.edu.au/research/dv/using-law-leaving-domestic-violence/case-studies")
soup = BeautifulSoup(r.text, "html.parser")

df = pd.DataFrame(columns=["name", "key_words", "story"])
for div in soup.find_all("div", {"class": "accordion__item"}):
    name = div.find("h2").get_text()
    i = 0
    key_words = ""
    story = ""
    for p in div.find_all("p"):
        if i == 0:
            key_words = str(p.get_text()).replace("Key words: ", "").replace("Key words: ", "").replace("Key words:", "")
            i += 1
        else:
            story += str(p.get_text()).replace(" ", " ").replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"') + " "

    df = df.append({"name":name, "key_words":key_words, "story":story}, ignore_index=True)


filepath = Path("Data/UQ Case Studies/uq_case_studies.csv")
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath, index=False)



