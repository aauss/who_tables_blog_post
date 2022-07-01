import io
import time
from datetime import date

import pandas as pd
import requests

import scheduler


def download_who_table() -> pd.DataFrame:
    """Downloads table on COVID-19 data from WHO.

    Returns:
        pd.DataFrame: WHO's COVID-19 data with renamed columns
    """
    response = requests.get(
        "https://covid19.who.int/WHO-COVID-19-global-table-data.csv",
    )
    io_stream = io.StringIO(response.content.decode("utf-8"))
    return pd.read_csv(io_stream).rename(
        {"Name": "WHO_Name", "WHO Region": "WHO_Region"}, axis=1
    )


def job() -> None:
    """Downloads COVID-19 table from WHO and saves it."""
    df = download_who_table()
    df.to_csv(
        f"scraped/who_table_{date.today().strftime('%Y-%m-%d_23-00')}.csv",
        index=False,
    )


if __name__ == "__main__":
    scheduler.every().day.at("23:00").do(job)
    while True:
        scheduler.run_pending()
        time.sleep(1)
