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


def process_pdf(pdf_path, csv_path):
    doc = pdf_reader(pdf_path, nlp)
    df = pd.DataFrame(columns=["label", "page", "text", "id", "surrounding_text"])
    counter = 0
    for i in range(len(doc.ents)):
        e = doc.ents[i]
        label = e.label_
        text = e.text.strip()
        time_id = e.kb_id_
        if label == "timexy" or label == "DATE":
            pg = e[0]._.page_number
            lines = str(doc._.page(pg)).split("\n\n")
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
            print(str(i + 1) + "/" + str(len(doc.ents)) + " [pg. " + str(pg) + "] : " + label + " | " + text + " | " + time_id + " | " + surrounding_text)
            df = df.append({"label":label, "page":pg, "text":text, "id":time_id, "surrounding_text":surrounding_text}, ignore_index=True)
    print("===========================================================================================================")
    print(str(counter) + "/" + str(len(doc.ents)) + " date-times found, " + csv_path + " created")
    print("===========================================================================================================")

    filepath = Path(csv_path)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath, index=False)


process_pdf("Documents/depp_v_ngn_closing_claimant.pdf", "Data/depp_v_ngn_closing_claimant.csv")
process_pdf("Documents/depp_v_ngn_closing_annex.pdf", "Data/depp_v_ngn_closing_annex.csv")
process_pdf("Documents/depp_v_ngn_closing_defendant_readable.pdf", "Data/depp_v_ngn_closing_defendant.csv")
