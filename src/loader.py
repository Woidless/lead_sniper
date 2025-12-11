import pandas as pd

def load_raw_data():
    df = pd.read_excel("data/raw/list_page_1.xlsx")
    for i in range(2, 4):
        df = pd.concat([df, pd.read_excel(f"data/raw/list_page_{i}.xlsx")], ignore_index=True)
    return df
