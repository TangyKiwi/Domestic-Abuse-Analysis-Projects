import os
import requests
from pathlib import Path
import pandas as pd
import pikepdf


def ocr_pdfs(input_dir, output_dir):
    df = pd.read_csv(input_dir)
    i = 0
    for link in df["link"]:
        if df["type"].iloc[i] == "pdf":
            response = requests.get(link)
            path = output_dir + "Original/" + df["file_name"].iloc[i]
            filepath = Path(path)
            filepath.parent.mkdir(parents=True, exist_ok=True)
            file = open(path, "wb")
            file.write(response.content)
            file.close()
            pdf = pikepdf.open(path, allow_overwriting_input=True)
            pdf.save(path)

            ocr_path = output_dir + "Readable/" + df["file_name"].iloc[i].split(".")[0] + "_readable.pdf"
            os.system("ocrmypdf --rotate-pages --deskew " + path + " " + ocr_path)
        i += 1


ocr_pdfs("Data/Depp_Heard/Defendant_Amber_Laura_Heard.csv", "Data/Depp_Heard/Heard/")
ocr_pdfs("Data/Depp_Heard/Plaintiff_John_C_Depp_II.csv", "Data/Depp_Heard/Depp/")
