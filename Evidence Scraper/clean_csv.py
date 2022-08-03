import pandas as pd
from pathlib import Path


def clean_csv(input_dir, output_dir, reference_dir):
    reference_csv = pd.read_csv(reference_dir)
    df = pd.read_csv(input_dir)
    df = df[(df["label"] == "timexy") & (df["id"].str.contains("DATE"))]

    dates = []
    for date in df["id"]:
        dates.append(date.partition("value=")[2].strip('"')[:10])
    df["calculated_date"] = dates
    df["calculated_date"] = pd.to_datetime(df["calculated_date"])
    df = df.sort_values(by="calculated_date")

    pretty_dates = []
    month_names = df["calculated_date"].dt.month_name(locale="English")
    i = 0
    for month in month_names:
        temp = str(month)
        if len(temp) > 3:
            temp = temp[:3] + "."
        pretty_dates.append(temp + " " + str(df["calculated_date"].iloc[i])[:4])
        i += 1
    df["pretty_date"] = pretty_dates

    links = []
    for (file, page) in zip(df["file"], df["page"]):
        links.append((reference_csv.loc[reference_csv["file_name"] == file.replace("_readable", "")])["link"].iloc[0] + "#page=" + str(page))
    df["link"] = links

    filepath = Path(output_dir)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath, index=False)


clean_csv("Data/Depp_Heard/Depp/depp_times.csv", "Data/Depp_Heard/Depp/timexy_depp_times.csv", "Data/Depp_Heard/Plaintiff_John_C_Depp_II.csv")
clean_csv("Data/Depp_Heard/Heard/heard_times.csv", "Data/Depp_Heard/Heard/timexy_heard_times.csv", "Data/Depp_Heard/Defendant_Amber_Laura_Heard.csv")