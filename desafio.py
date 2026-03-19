"""
==============================================================================
ANÁLISE EXPLORATÓRIA DE DADOS — COVID-19 no Brasil
Fonte: Brasil.IO (tabela caso_full)
Colunas utilizadas: date, state, place_type, new_confirmed, new_deaths,
                    last_available_death_rate, estimated_population
==============================================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import warnings
warnings.filterwarnings('ignore')

# ------------------------------------------------------------------------------
# 1. CARREGAMENTO
# ------------------------------------------------------------------------------
URL = "https://data.brasil.io/dataset/covid19/caso_full.csv.gz"

COLUNAS = ['date', 'state', 'place_type', 'is_last',
           'new_confirmed', 'new_deaths',
           'last_available_confirmed', 'last_available_deaths',
           'last_available_death_rate', 'estimated_population']

try:
    df = pd.read_csv(URL, compression='gzip', usecols=COLUNAS, low_memory=False)
    print(f"✓ Dados carregados | {df.shape[0]:,} registros")
except Exception:
    print("✗ Download falhou — usando dados sintéticos para demonstração")
    import numpy as np
    np.random.seed(42)
    states = ['SP','RJ','MG','BA','PR','RS','PE','CE','GO','AM',
              'PA','SC','ES','RN','AL','MT','MS','MA','PI','PB']
    pop    = [45919049,17264943,21292666,14873064,11433957,11377239,
               9616621, 9132078, 7055228, 4144597,
               8602865, 7164788, 4018650, 3534165, 3337357,
               3484466, 2778986, 7075181, 3273227, 4018386]
    dates = pd.date_range('2020-03-01', '2022-12-31', freq='W')
    rows = []
    for st, pop_val in zip(states, pop):
        conf = deaths = 0
        for d in dates:
            nc = int(np.random.gamma(2, pop_val / 5000))
            nd = int(nc * np.random.uniform(0.01, 0.04))
            conf += nc; deaths += nd
            rows.append({'date': d, 'state': st, 'place_type': 'state',
                         'is_last': (d == dates[-1]),
                         'new_confirmed': nc, 'new_deaths': nd,
                         'last_available_confirmed': conf,
                         'last_available_deaths': deaths,
                         'last_available_death_rate': deaths / max(conf, 1),
                         'estimated_population': pop_val})
    df = pd.DataFrame(rows)

# ------------------------------------------------------------------------------
# 2. LIMPEZA
# ------------------------------------------------------------------------------
df['date'] = pd.to_datetime(df['date'])
df = df[df['place_type'] == 'state'].copy()
df['new_confirmed'] = df['new_confirmed'].clip(lower=0)
df['new_deaths']    = df['new_deaths'].clip(lower=0)

df_last = df[df['is_last'] == True]
if df_last.empty:
    df_last = df.groupby('state').last().reset_index()

# ------------------------------------------------------------------------------
# 3. ESTATÍSTICAS DESCRITIVAS
# ------------------------------------------------------------------------------
print(f"\nTotal de casos (BR) : {df_last['last_available_confirmed'].sum():,.0f}")
print(f"Total de óbitos (BR): {df_last['last_available_deaths'].sum():,.0f}")
print(f"Taxa de mortalidade média: {df_last['last_available_death_rate'].mean()*100:.2f}%")
print(f"Período analisado: {df['date'].min().date()} → {df['date'].max().date()}")

# ------------------------------------------------------------------------------
# 4. GRÁFICOS
# ------------------------------------------------------------------------------
COR1, COR2, COR3 = '#2196F3', '#F44336', '#4CAF50'

# --- Gráfico 1: Evolução semanal de casos e óbitos no Brasil ----------------
br = (df.groupby('date')[['new_confirmed', 'new_deaths']]
        .sum().reset_index().sort_values('date'))
br['mm_casos']  = br['new_confirmed'].rolling(4).mean()
br['mm_obitos'] = br['new_deaths'].rolling(4).mean()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 7), sharex=True)
fig.suptitle('Evolução Semanal da COVID-19 no Brasil', fontsize=14, fontweight='bold')

ax1.bar(br['date'], br['new_confirmed'], color=COR1, alpha=0.3, width=5)
ax1.plot(br['date'], br['mm_casos'], color=COR1, linewidth=2, label='Média móvel (4 sem.)')
ax1.set_ylabel('Novos Casos'); ax1.legend(); ax1.grid(axis='y', alpha=0.4)
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_: f'{x/1e3:.0f}k'))

ax2.bar(br['date'], br['new_deaths'], color=COR2, alpha=0.3, width=5)
ax2.plot(br['date'], br['mm_obitos'], color=COR2, linewidth=2, label='Média móvel (4 sem.)')
ax2.set_ylabel('Novos Óbitos'); ax2.legend(); ax2.grid(axis='y', alpha=0.4)
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x,_: f'{x/1e3:.0f}k'))

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/fig1_evolucao_temporal.png', dpi=150, bbox_inches='tight')
plt.close()
print("\n✓ fig1_evolucao_temporal.png")

# --- Gráfico 2: Óbitos por 100k habitantes por estado -----------------------
df_last = df_last.copy()
df_last['obitos_100k'] = (df_last['last_available_deaths'] /
                          df_last['estimated_population'] * 100_000)
df_plot = df_last.sort_values('obitos_100k', ascending=True)

fig, ax = plt.subplots(figsize=(10, 7))
bars = ax.barh(df_plot['state'], df_plot['obitos_100k'], color=COR2, alpha=0.8)
ax.set_title('Óbitos por COVID-19 por 100 mil habitantes — por Estado', fontweight='bold')
ax.set_xlabel('Óbitos por 100 mil habitantes')
ax.bar_label(bars, fmt='%.0f', padding=3, fontsize=8)
ax.grid(axis='x', alpha=0.4)
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/fig2_obitos_por_estado.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ fig2_obitos_por_estado.png")

# --- Gráfico 3: Taxa de mortalidade por estado (barras) ---------------------
df_taxa = df_last.sort_values('last_available_death_rate', ascending=True)
cores = [COR3 if v < df_taxa['last_available_death_rate'].median() else COR2
         for v in df_taxa['last_available_death_rate']]

fig, ax = plt.subplots(figsize=(10, 7))
bars = ax.barh(df_taxa['state'], df_taxa['last_available_death_rate'] * 100,
               color=cores, alpha=0.85)
ax.axvline(df_taxa['last_available_death_rate'].median() * 100,
           color='gray', linestyle='--', linewidth=1.5, label='Mediana nacional')
ax.set_title('Taxa de Mortalidade por COVID-19 — por Estado (%)', fontweight='bold')
ax.set_xlabel('Taxa de Mortalidade (%)')
ax.bar_label(bars, fmt='%.2f%%', padding=3, fontsize=8)
ax.legend()
ax.grid(axis='x', alpha=0.4)
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/fig3_taxa_mortalidade.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ fig3_taxa_mortalidade.png")

print("\nAnálise concluída!")