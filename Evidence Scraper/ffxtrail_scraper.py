import pandas as pd
import requests
from bs4 import BeautifulSoup
from pathlib import Path

import warnings
# pandas doesn't like df.append, use this to stop console from being spammed with warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

depp_url = "https://ffxtrail.azurewebsites.net/?handler=Dir&directory=Plaintiff%20John%20C.%20Depp,%20II/"
depp_dates = ["5-17-2022", "5-16-2022", "5-4-2022", "4-28-2022", "4-27-2022", "4-25-2022", "4-21-2022", "4-26-2022",
              "4-20-2022", "4-18-2022", "4-13-2022"]
depp_dates.sort()

heard_url = "https://ffxtrail.azurewebsites.net/?handler=Dir&directory=Defendant%20Amber%20Laura%20Heard/"
heard_dates = ["5-18-2022", "5-24-2022", "5-25-2022", "5-16-2022", "5-5-2022", "5-19-2022", "5-17-2022", "5-2-2022",
               "5-4-2022", "4-28-2022", "4-27-2022", "4-21-2022", "4-25-2022", "4-26-2022", "4-20-2022", "4-18-2022",
               "4-12-2022", "4-14-2022", "4-13-2022"]
heard_dates.sort()


def scrape_evidence(name, dates, url):
    df = pd.DataFrame(columns=["date", "type", "file_name", "link"])
    for date in dates:
        evidence_url = url + date
        r = requests.get(evidence_url)
        soup = BeautifulSoup(r.text, "html.parser")

        for div in soup.find_all("a"):
            link = div.get("href")
            if date in link:
                file_name = div.get("download")
                df = df.append({"date":date, "type":link.split(".")[-1], "file_name":file_name, "link":link}, ignore_index=True)

                # Downloading takes forever, we probably don't need to do it, would rather store data links in a CSV
                # output_file = Path("Data" + "/" + name + "/" + date + "/" + file_name)
                # output_file.parent.mkdir(exist_ok=True, parents=True)
                # open(output_file, "wb").write(requests.get(link).content)
                # print("Downloaded: " + date + " " + output_file.name)

    filepath = Path("Data/" + name + ".csv")
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath, index=False)


scrape_evidence("Plaintiff John C. Depp, II", depp_dates, depp_url)
scrape_evidence("Defendant Amber Laura Heard", heard_dates, heard_url)
