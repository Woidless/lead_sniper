import pandas as pd

def drop_unused_columns(df):
    return df.drop(columns=[
        'Ссылка на www.list-org.com',
        'Юридическое наименование',
        'Статус',
        'ОГРН',
        'Руководитель',
        'Прибыль (Ф2.2400)',
        'Стоимость (Ф1.1300)',
        'В избранном',
        'Описание',
    ])

def rename_columns(df):
    return df.rename(columns={
      'Наименование': 'name',
      'ИНН': 'inn',
      'Телефон (один из)': 'phone',
      'E-mail': 'email',
      'Сайт': 'site',
      'Юридический адрес': 'address',
      'Сотрудников': 'employees',
      'Выручка (Ф2.2110)': 'revenue',
    })

def add_constant_columns(df):
    df['revenue_year'] = 2024
    df['source'] = 'list-org.com'
    return df

def extract_region(df):
    df['region'] = df.address.str.split(',').str[1].str.strip().str.title()
    df = df.drop(columns=['address'])
    return df

def fix_phone(df):
    phone_mask = df.phone.str.startswith('+7')
    df.loc[~phone_mask, "phone"] = pd.NA
    return df

def drop_no_revenue(df):
    return df[df.revenue.notna()]
