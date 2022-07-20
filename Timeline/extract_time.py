import spacy
from spacypdfreader import pdf_reader
from timexy import Timexy
import pandas as pd
from pathlib import Path

import warnings
# pandas doesn't like df.append, use this to stop console from being spammed with warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

# "en_core_web_sm" for efficiency
nlp = spacy.load("en_core_web_sm")

# Optionally add config if varying from default values
config = {
    "kb_id_type": "timex3",  # possible values: 'timex3'(default), 'timestamp'
    "label": "timexy",       # default: 'timexy'
    "overwrite": False       # default: False
}
nlp.add_pipe("timexy", config=config, before="ner")

# doc = pdf_reader("Documents/depp_v_ngn_closing_claimant.pdf", nlp)
# doc = pdf_reader("Documents/depp_v_ngn_closing_annex.pdf", nlp)
doc = pdf_reader("Documents/depp_v_ngn_closing_defendant_readable.pdf", nlp)
df = pd.DataFrame(columns=["label", "text", "id", "surrounding_text"])
counter = 0
for i in range(len(doc.ents)):
    e = doc.ents[i]
    label = e.label_
    text = e.text.strip()
    id = e.kb_id_
    if label == "timexy" or label == "DATE":
        pg = e[0]._.page_number
        lines = str(doc._.page(pg)).split("\n")
        lines = [i for i in lines if i] # remove all empty lines
        surrounding_text = ""
        for line in lines:
            if text in line:
                surrounding_text = line
                break
        if label == "DATE":
            false_positive = False
            for word in line.split():
                if "[" not in word and text in word and "]" not in word:
                    false_positive = True
                    break
            if false_positive: continue

        counter += 1
        print(str(i + 1) + "/" + str(len(doc.ents)) + " [pg. " + str(pg) + "] : " + label + " | " + text + " | " + id + " | " + surrounding_text)
        df = df.append({"label":label, "text":text, "id":id, "surrounding_text":surrounding_text}, ignore_index=True)
print(str(counter) + "/" + str(len(doc.ents)) + " date-times found")

# filepath = Path("Data/depp_v_ngn_closing_claimant.csv")
# filepath = Path("Data/depp_v_ngn_closing_annex.csv")
filepath = Path("Data/depp_v_ngn_closing_defendant.csv")
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath, index=False)