import pandas as pd


print('Carregando dados...')

URL = "caso_full.csv.gz"
df = pd.read_csv(URL, compression="gzip", low_memory=False)
print(f'Shape {df.shape}')
print(df.dtypes)
print(df.head())

# print(df['place_type'].value_counts())
print(df['city'].nunique())

