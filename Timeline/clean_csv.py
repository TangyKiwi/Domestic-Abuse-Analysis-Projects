import pandas as pd
from pathlib import Path


def clean_csv(input_dir, output_dir, link):
    df = pd.read_csv(input_dir)
    df = df[(df["label"] == "timexy") & (df["id"].str.contains("DATE"))]
    links = []
    for pg in df["page"]:
        links.append(link + "#page=" + str(pg))
    df["link"] = links

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


clean_csv("Data/depp_v_ngn_closing_annex.csv", "Data/timexy_depp_v_ngn_closing_annex.csv", "https://www.nickwallis.com/_files/ugd/5df505_02c32292979f45da962280c334bc5815.pdf")
clean_csv("Data/depp_v_ngn_closing_claimant.csv", "Data/timexy_depp_v_ngn_closing_claimant.csv", "https://www.nickwallis.com/_files/ugd/5df505_9aaf63a412534537b472b5f5e8e6ddf0.pdf")
clean_csv("Data/depp_v_ngn_closing_defendant.csv", "Data/timexy_depp_v_ngn_closing_defendant.csv", "https://www.nickwallis.com/_files/ugd/5df505_23ef139d05094dbb981cd11ff3d7240f.pdf")