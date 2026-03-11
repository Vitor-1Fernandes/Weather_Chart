import pandas as pd  # type: ignore
import matplotlib.pyplot as plt

# Ler dataset
df = pd.read_csv("dataset_clima-1.csv")

# Ordem cronológica dos meses
ordem_meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
               "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

# Agrupar média de carros por mês
dfGroupCarros = df.groupby("Mês")["Número_de_Carros_na_Rua"].mean().reindex(ordem_meses)

# Criar gráfico
plt.figure(figsize=(10,5))

dfGroupCarros.plot(kind="bar", color="steelblue")

plt.title("Número médio de carros nas ruas por mês")
plt.xlabel("Mês")
plt.ylabel("Número médio de carros")
plt.grid(axis="y")

# CHUVA VS CARROS
plt.figure(figsize=(7,5))

plt.scatter(df["Precipitação_mm"], df["Número_de_Carros_na_Rua"], alpha=0.6)

plt.title("Relação entre chuva e número de carros")
plt.xlabel("Precipitação (mm)")
plt.ylabel("Número de carros")

# TEMORERATURA VS CARROS
plt.figure(figsize=(7,5))

plt.scatter(df["Temperatura_Média"], df["Número_de_Carros_na_Rua"], alpha=0.6)

plt.title("Relação entre temperatura e número de carros")
plt.xlabel("Temperatura média")
plt.ylabel("Número de carros")

# Agrupar dados por mês
dfGroupCarros = df.groupby("Mês")["Número_de_Carros_na_Rua"].mean().reindex(ordem_meses)
dfGroupTempMed = df.groupby("Mês")["Temperatura_Média"].mean().reindex(ordem_meses)
dfGroupPrecip = df.groupby("Mês")["Precipitação_mm"].mean().reindex(ordem_meses)

# Criar gráfico comparativo
plt.figure(figsize=(10,5))

dfGroupCarros.plot(label="Carros")
dfGroupTempMed.plot(label="Temperatura")
dfGroupPrecip.plot(label="Precipitação")

plt.title("Comparação entre carros, temperatura e precipitação")
plt.xlabel("Mês")

plt.legend()
plt.grid(True)
plt.show()