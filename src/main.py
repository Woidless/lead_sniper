from .loader import load_raw_data
from .cleaner import (
    drop_unused_columns,
    rename_columns,
    add_constant_columns,
    extract_region,
    fix_phone,
    drop_no_revenue,
)
from .enrich import enrich_with_okved

def main():

    df = load_raw_data()

    df = drop_unused_columns(df)
    df = rename_columns(df)
    df = add_constant_columns(df)
    df = extract_region(df)
    df = fix_phone(df)
    df = drop_no_revenue(df)

    df = enrich_with_okved(df)

    # нормализация сотрудников
    max_e = df.employees.max()
    min_e = df.employees.min()
    df['employees_norm'] = (df.employees - min_e) / (max_e - min_e)

    # перестановка колонок
    cols = ['inn','name','employees','employees_norm','okved_main',
            'source','revenue_year','revenue','site','region','phone','email']
    df = df[cols]

    df['source'] = df['source'] + ', rusprofile.ru'

    df.to_csv("data/companies.csv", index=False)

if __name__ == "__main__":
    main()
