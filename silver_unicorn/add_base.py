import pandas as pd
from sqlalchemy import create_engine
import psycopg2

engine = create_engine('postgresql+psycopg2://postgres:08098899@localhost:5432/silver_unicorn')
with pd.ExcelFile('book.xlsx') as xls:
    df = pd.read_excel(xls)
    df.to_sql(name='products_products', con=engine, if_exists='append', index=False)
