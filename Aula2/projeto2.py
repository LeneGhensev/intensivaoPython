import pandas as pd
import plotly.express as px

tabela = pd.read_csv("telecom_users.csv", encoding="latin") #lê a tabela e traduz os caracteres especiais

tabela = tabela.drop("Unnamed: 0", axis=1) #esse método remove uma coluna (axis=1) ou linha (axis=0)

tabela["Codigo"] = pd.to_numeric(tabela["Codigo"], errors="coerce") #transforma os dados da coluna código para numérico

tabela = tabela.dropna(how="all", axis=1) #apaga colunas vazias
tabela = tabela.dropna(how="any", axis=0) #apaga linhas vazias

print(tabela.info())
print(tabela)

print(tabela.describe())
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

#primeiro precisa criar o gráfico e depois exibir, usando o plotly
for coluna in tabela.columns: #para cada coluna da tabela irá criar um gráfico e exibir
    grafico = px.histogram(tabela, x=coluna, text_auto=True, nbins=10)
    grafico.show()

#text_auto=True serve pra mostrar as infos assim que passar o mouse sobre o gráfico
#nbins=10 informa o npumero máximo de divisões pra unir informações em faixas de valores
    