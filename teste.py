import pandas as pd
import matplotlib.pyplot as plt
# ==============================
# 1. Carregamento dos Dados
# ==============================
# Dataset de casos COVID Brasil (Brasil.io - formato CSV público)
url = "caso_full.csv.gz"
# Adicionando um User-Agent para evitar o erro 403 Forbidden do Brasil.io
# storage_options = {'User-Agent': 'Mozilla/5.0'}
df = pd.read_csv(url, compression='gzip', low_memory=False)
# ==============================
# 2. Limpeza e Preparação
# ==============================
# Filtrar apenas dados agregados por estado
df_estados = df[df['place_type'] == 'state'].copy()
# Converter data
df_estados['date'] = pd.to_datetime(df_estados['date'])
# Remover valores nulos
df_estados = df_estados.dropna(subset=['new_confirmed', 'new_deaths'])
# Agregar por data (Brasil inteiro)
df_brasil = df_estados.groupby('date')[['new_confirmed','new_deaths']].sum().reset_index()
# Criar média móvel de 7 dias
df_brasil['media_movel_casos'] = df_brasil['new_confirmed'].rolling(window=7).mean()
# ==============================
# 3. GRÁFICO 1 – Evolução de Casos Diários
# ==============================
plt.figure()
plt.plot(df_brasil['date'], df_brasil['new_confirmed'])
plt.title("Evolução de Casos Diários de COVID-19 no Brasil")
plt.xlabel("Data")
plt.ylabel("Novos Casos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# ==============================
# 4. GRÁFICO 2 – Média Móvel de 7 dias
# ==============================
plt.figure()
plt.plot(df_brasil['date'], df_brasil['media_movel_casos'])
plt.title("Média Móvel de 7 dias - Novos Casos")
plt.xlabel("Data")
plt.ylabel("Média Móvel (7 dias)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# ==============================
# 5. GRÁFICO 3 – Estados com Mais Óbitos
# ==============================
# Total de óbitos por estado

obitos_estado = df_estados.groupby('state')['new_deaths'].sum().sort_values(ascending=False).head(10)
plt.figure()
plt.bar(obitos_estado.index, obitos_estado.values)
plt.title("Top 10 Estados com Maior Número de Óbitos")
plt.xlabel("Estado")
plt.ylabel("Total de Óbitos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()