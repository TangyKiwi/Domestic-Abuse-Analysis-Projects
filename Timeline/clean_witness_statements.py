import pandas as pd
from pathlib import Path


def clean_csv(input_dir, output_dir, reference_dir):
    df = pd.read_csv(input_dir)
    df = df[(df["label"] == "timexy") & (df["id"].str.contains("DATE"))]

    reference_df = pd.read_csv(reference_dir)
    names = []
    for file in df["file"]:
        index = int(file.split(".")[0])
        names.append(reference_df["name"].iloc[index])
    df["name"] = names

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

    filepath = Path(output_dir)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath, index=False)


clean_csv("Data/Depp/depp_times.csv", "Data/Depp/timexy_depp_times.csv", "Data/Depp/depp_witness_statements.csv")
clean_csv("Data/Heard/heard_times.csv", "Data/Heard/timexy_heard_times.csv", "Data/Heard/heard_witness_statements.csv")