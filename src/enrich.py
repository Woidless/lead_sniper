from time import sleep
from .rusprofile import fetch_html, get_okved_main
import pandas as pd

def enrich_with_okved(df):
    df['okved_main'] = pd.NA
    df = df.reset_index(drop=True)

    inns = df.inn.copy()

    for i in range(df.shape[0]):
        url = f'https://www.rusprofile.ru/search?query={inns.loc[i]}'
        okved_main = get_okved_main(fetch_html(url))
        df.at[i, 'okved_main'] = okved_main
        sleep(2)

    df = df[df.okved_main.notna()]
    df = df.reset_index(drop=True)
    return df
