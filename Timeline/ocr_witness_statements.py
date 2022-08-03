import os
import requests
from pathlib import Path
import pandas as pd
import pikepdf


def ocr_pdfs(input_dir, output_dir):
    df = pd.read_csv(input_dir)
    i = 0
    for (name, link) in zip(df["name"], df["link"]):
        response = requests.get(link)
        path = output_dir + "Original/" + str(i) + ".pdf"
        filepath = Path(path)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        file = open(path, "wb")
        file.write(response.content)
        file.close()
        pdf = pikepdf.open(path, allow_overwriting_input=True)
        pdf.save(path)

        ocr_path = output_dir + "Readable/" + str(i) + "_readable.pdf"
        os.system("ocrmypdf --rotate-pages --deskew " + path + " " + ocr_path)
        i += 1


ocr_pdfs("Data/depp_witness_statements.csv", "Data/Depp/")
ocr_pdfs("Data/Heard/heard_witness_statements.csv", "Data/Heard/")
