import io
import time
from datetime import date

import pandas as pd
import requests

import scheduler


def download_who_table() -> pd.DataFrame:
    response = requests.get(
        "https://covid19.who.int/WHO-COVID-19-global-table-data.csv",
    )
    io_stream = io.StringIO(response.content.decode("utf-8"))
    return pd.read_csv(io_stream).rename(
        {"Name": "WHO_Name", "WHO Region": "WHO_Region"}, axis=1
    )


def job() -> None:
    df = download_who_table()
    df.to_csv(
        f"scraped/who_table_{date.today().strftime('%Y-%m-%d_23-00')}.csv",
        index=False,
    )


if __name__ == "__main__":
    schedule.every().day.at("23:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
