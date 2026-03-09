import pandas as pd #type: ignore
import matplotlib.pyplot as plt


df = pd.read_csv("dataset_clima-1.csv") 

# Para ver os nomes das colunas
# print(df.head())

dfGroup = df.copy()

# Para ver a incidência de cada mês, os registros estão desproporcionais
# print(dfGroup["Mês"].value_counts())

# Criando uma lista para reindexar os meses baseado na ordem cronológica
ordem_meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

# Agrupar por mês e propriedade, tirando uma média dos valores de registro e reorganizar em ordem cronológica
dfGroupCarros = dfGroup.groupby("Mês")["Número_de_Carros_na_Rua"].mean().reindex(ordem_meses)
dfGroupTempMed = dfGroup.groupby("Mês")["Temperatura_Média"].mean().reindex(ordem_meses)
dfGroupPrecip = dfGroup.groupby("Mês")["Precipitação_mm"].mean().reindex(ordem_meses)
dfGroupVelVento = dfGroup.groupby("Mês")["Velocidade_Vento_kmh"].mean().reindex(ordem_meses)
dfGroupUmiRel = dfGroup.groupby("Mês")["Umidade_Relativa_%"].mean().reindex(ordem_meses)
dfGroupPressAt = dfGroup.groupby("Mês")["Pressão_Atmosférica_hPa"].mean().reindex(ordem_meses)

# Cria um grid para plotar vários gráficos na mesma janela
fig, axe = plt.subplots(3, 2, figsize=(10, 12))

# Ax = matriz do grid
dfGroupCarros.plot(ax=axe[0, 0], kind="bar", xlabel="", title="Carros na Rua")
dfGroupTempMed.plot(ax=axe[1, 0], kind="bar",xlabel="", title="Temp Media")
dfGroupPrecip.plot(ax=axe[2, 0], kind="bar",xlabel="",  title="Precipitação")
dfGroupVelVento.plot(ax=axe[0, 1], kind="bar",xlabel="",  title="Vel. Vento")
dfGroupUmiRel.plot(ax=axe[1, 1], kind="bar",xlabel="",  title="Umi. Rel.")
dfGroupPressAt.plot(ax=axe[2, 1], kind="bar",xlabel="",  title="Press. Atm.")

# Evita a sobreposição
plt.tight_layout()

plt.show()