import pandas as pd

df = pd.read_csv('dados.csv', sep=';')

df['created_at'] = pd.to_datetime(df['created_at']).dt.date

df['updated_at'] = pd.to_datetime(df['updated_at']).dt.date

#df['Push'] = pd.to_datetime(df['Push']).dt.date

print(df.head())

with open("dados2.csv", "a", encoding="utf-8") as f:
    f.write(df.to_csv(sep=';', na_rep='null', header=True, index=False, lineterminator='\n'))