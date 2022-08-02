import spacy
from spacypdfreader import pdf_reader
from timexy import Timexy
import pandas as pd
from pathlib import Path
import os

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


def process_pdf(pdf_path, file_name, df):
    doc = pdf_reader(pdf_path, nlp)
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
            df = df.append({"file":file_name, "label":label, "page":pg, "text":text, "id":time_id, "surrounding_text":surrounding_text}, ignore_index=True)
    print("===========================================================================================================")
    print(str(counter) + "/" + str(len(doc.ents)) + " date-times found")
    print("===========================================================================================================")
    return df


def process_folder(folder_path, csv_path):
    df = pd.DataFrame(columns=["file", "label", "page", "text", "id", "surrounding_text"])
    for file in os.listdir(folder_path):
        df = process_pdf(folder_path + "/" + file, file, df)
    filepath = Path(csv_path)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath, index=False)


process_folder("Data/Depp_Heard/Depp/Readable", "Data/Depp_Heard/Depp/depp_times.csv")
process_folder("Data/Depp_Heard/Heard/Readable", "Data/Depp_Heard/Heard/heard_times.csv")


