import pandas as pd


print('Carregando dados...')

URL = "caso_full.csv.gz"
df = pd.read_csv(URL, compression="gzip", low_memory=False)
print(f'Shape {df.shape}')
print(df.dtypes)
print(df.tail(10))
# print(df.info())
# print(df.describe())

# print(df['place_type'].value_counts())
# print(df['city'].nunique())
# df.dropna()
# df.drop_duplicates()
# df_dim = df [[
#     "city",
#     "date",
#     "epidemiological_week",
#     "estimated_population",
#     "last_available_deaths"
# ]].drop_duplicates().dropna()

# print(df_dim)
# df_dim