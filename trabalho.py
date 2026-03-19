import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
 
# --- Carregamento ---
URL = "https://data.brasil.io/dataset/covid19/caso_full.csv.gz"
COLUNAS = ['date', 'state', 'place_type', 'is_last',
           'new_confirmed', 'new_deaths',
           'last_available_deaths', 'estimated_population',
           'last_available_death_rate']
 
import requests, io

resposta = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'}, stream=True)
df = pd.read_csv(io.BytesIO(resposta.content), compression='gzip', usecols=COLUNAS, low_memory=False)
 
# --- Limpeza ---
df['date'] = pd.to_datetime(df['date'])
df = df[df['place_type'] == 'state'].copy()
df['new_confirmed'] = df['new_confirmed'].clip(lower=0)
df['new_deaths']    = df['new_deaths'].clip(lower=0)
 
df_last = df[df['is_last'] == True]
 
# --- Estatísticas básicas ---
print("=== COVID-19 Brasil ===")
print(f"Período  : {df['date'].min().date()} → {df['date'].max().date()}")
print(f"Óbitos   : {df_last['last_available_deaths'].sum():,.0f}")
print(f"Mortalidade média: {df_last['last_available_death_rate'].mean()*100:.2f}%")
 
# --- Gráfico 1: Evolução semanal de novos casos ---
br = df.groupby('date')[['new_confirmed', 'new_deaths']].sum().reset_index()
 
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6), sharex=True)
fig.suptitle('Evolução Semanal da COVID-19 no Brasil', fontweight='bold')
 
ax1.bar(br['date'], br['new_confirmed'], color='steelblue', alpha=0.6, width=5)
ax1.plot(br['date'], br['new_confirmed'].rolling(4).mean(), color='steelblue', linewidth=2)
ax1.set_ylabel('Novos Casos')
 
ax2.bar(br['date'], br['new_deaths'], color='tomato', alpha=0.6, width=5)
ax2.plot(br['date'], br['new_deaths'].rolling(4).mean(), color='tomato', linewidth=2)
ax2.set_ylabel('Novos Óbitos')
 
for ax in (ax1, ax2):
    ax.grid(axis='y', alpha=0.4)
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/fig1_evolucao.png', dpi=150, bbox_inches='tight')
plt.show()
plt.close()
 
# --- Gráfico 2: Óbitos por 100k habitantes por estado ---
df_last = df_last.copy()
df_last['obitos_100k'] = df_last['last_available_deaths'] / df_last['estimated_population'] * 100_000
df_plot = df_last.sort_values('obitos_100k')
 
fig, ax = plt.subplots(figsize=(9, 7))
ax.barh(df_plot['state'], df_plot['obitos_100k'], color='tomato', alpha=0.8)
ax.set_title('Óbitos por 100 mil habitantes — por Estado', fontweight='bold')
ax.set_xlabel('Óbitos / 100k hab.')
ax.grid(axis='x', alpha=0.4)
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/fig2_obitos_estado.png', dpi=150, bbox_inches='tight')
plt.show()
plt.close()
 
# --- Gráfico 3: Taxa de mortalidade por estado ---
df_taxa = df_last.sort_values('last_available_death_rate')
 
fig, ax = plt.subplots(figsize=(9, 7))
ax.barh(df_taxa['state'], df_taxa['last_available_death_rate'] * 100, color='steelblue', alpha=0.8)
ax.axvline(df_taxa['last_available_death_rate'].median() * 100, color='gray', linestyle='--', linewidth=1.5, label='Mediana')
ax.set_title('Taxa de Mortalidade por Estado (%)', fontweight='bold')
ax.set_xlabel('Taxa de Mortalidade (%)')
ax.legend()
ax.grid(axis='x', alpha=0.4)
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/fig3_taxa_mortalidade.png', dpi=150, bbox_inches='tight')
plt.show()
plt.close()
 
print("Gráficos gerados com sucesso!")