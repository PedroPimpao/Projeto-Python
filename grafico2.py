# ============================================================
#  Análise de Dados - COVID-19 Brasil
#  Fonte: Brasil.IO — caso_full.csv.gz
#  Bibliotecas: apenas Pandas e Matplotlib
# ============================================================
 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
 
# ── 1. CARREGAR OS DADOS ────────────────────────────────────
print("Carregando dados...")
URL = "caso_full.csv.gz"
df = pd.read_csv(URL, compression="gzip", low_memory=False)
print(f"Shape: {df.shape}")
print(df.dtypes)
print(df.head(3))
 
# ── 2. LIMPEZA BÁSICA ───────────────────────────────────────
# Converter data para datetime
df["date"] = pd.to_datetime(df["date"])
 
# Filtrar apenas nível estadual (place_type == 'state') 
# para evitar dupla contagem com os municípios
df_state = df[df["place_type"] == "state"].copy()
 
# Remover colunas desnecessárias para esta análise
cols = ["date", "state", "last_available_deaths", "new_deaths",
        "last_available_confirmed", "new_confirmed", "estimated_population"]
df_state = df_state[cols].dropna(subset=["last_available_deaths", "last_available_confirmed"])
 
print(f"\nRegistros após limpeza: {df_state.shape[0]}")
print(df_state.isnull().sum())
 
# ── 3. ANÁLISE EXPLORATÓRIA ─────────────────────────────────
# Totais por estado (último registro de cada estado)
df_latest = (df_state.sort_values("date")
                      .groupby("state")
                      .last()
                      .reset_index())
 
df_latest["letalidade"] = (df_latest["last_available_deaths"] / df_latest["last_available_confirmed"] * 100).round(2)
df_latest["mortes_por_100k"] = (df_latest["last_available_deaths"] / df_latest["estimated_population"] * 100_000).round(1)
 
print("\nTop 5 estados em óbitos totais:")
print(df_latest.nlargest(5, "last_available_deaths")[["state","last_available_confirmed","last_available_deaths","letalidade"]])
 
# ── 4. DADOS NACIONAIS - SÉRIE TEMPORAL ─────────────────────
df_brasil = (df_state.groupby("date")[["new_confirmed","new_deaths"]]
                     .sum()
                     .reset_index()
                     .sort_values("date"))
 
# Média móvel 7 dias
df_brasil["mm7_casos"]  = df_brasil["new_confirmed"].rolling(7).mean()
df_brasil["mm7_mortes"] = df_brasil["new_deaths"].rolling(7).mean()
 
# ── 5. VISUALIZAÇÕES ────────────────────────────────────────
plt.style.use("seaborn-v0_8-whitegrid")
fig = plt.figure(figsize=(18, 14))
fig.suptitle("COVID-19 no Brasil — Análise por Estado e Temporal",
             fontsize=16, fontweight="bold", y=0.98)
 
BLUE   = "#2563EB"
RED    = "#DC2626"
ORANGE = "#F59E0B"
GRAY   = "#94A3B8"
 
# ── Gráfico 1: Casos diários (série temporal + MM7) ─────────
ax1 = fig.add_subplot(3, 2, 1)
ax1.bar(df_brasil["date"], df_brasil["new_confirmed"],
        color=BLUE, alpha=0.3, label="Casos diários")
ax1.plot(df_brasil["date"], df_brasil["mm7_casos"],
         color=BLUE, linewidth=2, label="Média móvel 7d")
ax1.set_title("Novos casos diários — Brasil", fontweight="bold")
ax1.set_ylabel("Casos")
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x/1e6:.1f}M" if x >= 1e6 else f"{x/1e3:.0f}k"))
ax1.legend(fontsize=8)
ax1.tick_params(axis="x", rotation=30)
 
# ── Gráfico 2: Óbitos diários (série temporal + MM7) ────────
ax2 = fig.add_subplot(3, 2, 2)
ax2.bar(df_brasil["date"], df_brasil["new_deaths"],
        color=RED, alpha=0.3, label="Óbitos diários")
ax2.plot(df_brasil["date"], df_brasil["mm7_mortes"],
         color=RED, linewidth=2, label="Média móvel 7d")
ax2.set_title("Novos óbitos diários — Brasil", fontweight="bold")
ax2.set_ylabel("Óbitos")
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x/1e3:.0f}k" if x >= 1000 else str(int(x))))
ax2.legend(fontsize=8)
ax2.tick_params(axis="x", rotation=30)
 
# ── Gráfico 3: Top 10 estados — óbitos totais ───────────────
ax3 = fig.add_subplot(3, 2, 3)
top10_mortes = df_latest.nlargest(10, "last_available_deaths").sort_values("last_available_deaths")
colors = [RED if s == "SP" else BLUE for s in top10_mortes["state"]]
bars = ax3.barh(top10_mortes["state"], top10_mortes["last_available_deaths"], color=colors)
ax3.set_title("Top 10 estados — óbitos acumulados", fontweight="bold")
ax3.set_xlabel("Óbitos")
ax3.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x/1e3:.0f}k"))
for bar, val in zip(bars, top10_mortes["last_available_deaths"]):
    ax3.text(bar.get_width() + 500, bar.get_y() + bar.get_height()/2,
             f"{val:,.0f}", va="center", fontsize=7)
 
# ── Gráfico 4: Taxa de letalidade por estado ────────────────
ax4 = fig.add_subplot(3, 2, 4)
df_let = df_latest.sort_values("letalidade", ascending=False)
colors4 = [RED if v > df_let["letalidade"].mean() else ORANGE for v in df_let["letalidade"]]
ax4.bar(df_let["state"], df_let["letalidade"], color=colors4)
ax4.axhline(df_let["letalidade"].mean(), color="black",
            linestyle="--", linewidth=1, label=f'Média: {df_let["letalidade"].mean():.1f}%')
ax4.set_title("Taxa de letalidade por estado (%)", fontweight="bold")
ax4.set_ylabel("Letalidade (%)")
ax4.tick_params(axis="x", rotation=90)
ax4.legend(fontsize=8)
 
# ── Gráfico 5: Óbitos por 100 mil habitantes ────────────────
ax5 = fig.add_subplot(3, 2, 5)
df_100k = df_latest.sort_values("mortes_por_100k", ascending=False)
ax5.bar(df_100k["state"], df_100k["mortes_por_100k"], color=ORANGE)
ax5.axhline(df_100k["mortes_por_100k"].mean(), color="black",
            linestyle="--", linewidth=1,
            label=f'Média: {df_100k["mortes_por_100k"].mean():.0f}')
ax5.set_title("Óbitos por 100 mil habitantes", fontweight="bold")
ax5.set_ylabel("Óbitos / 100k hab.")
ax5.tick_params(axis="x", rotation=90)
ax5.legend(fontsize=8)
 
# ── Gráfico 6: Correlação casos × óbitos por estado ─────────
ax6 = fig.add_subplot(3, 2, 6)
ax6.scatter(df_latest["last_available_confirmed"], df_latest["last_available_deaths"],
            color=BLUE, alpha=0.7, s=60, zorder=3)
for _, row in df_latest.iterrows():
    ax6.annotate(row["state"],
                 (row["last_available_confirmed"], row["last_available_deaths"]),
                 fontsize=6, alpha=0.75,
                 xytext=(4, 2), textcoords="offset points")
ax6.set_title("Correlação: casos × óbitos por estado", fontweight="bold")
ax6.set_xlabel("Casos confirmados")
ax6.set_ylabel("Óbitos")
ax6.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x/1e6:.1f}M"))
ax6.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x/1e3:.0f}k"))
 
plt.tight_layout()
plt.savefig("covid_brasil_analise.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nGráfico salvo como covid_brasil_analise.png")