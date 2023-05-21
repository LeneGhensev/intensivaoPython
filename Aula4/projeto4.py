import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split #não importa a biblioteca, só um pactoe específico. O sklearn é uma biblioteca para criar inteligências artificiais.
from sklearn.linear_model import LinearRegression #esse modelo vai plotando os dados em um gráfico e depois traça uma reta com os dados plotados, para tentar fazer a previsão.
from sklearn.ensemble import RandomForestRegressor #esse modelo cria uma árvore com perguntas para a base de dados, com respostas sim e não, até chegar nas informações necessárias pra fazer a previsão.
from sklearn import metrics

tabela = pd.read_csv("barcos_ref.csv")
print(tabela)
print(tabela.info) #mostra as informações da tabela
print(tabela.corr) #calcula a correlação dos valores da tabela. Correlação é a proporção da qual dois valores aumentan ou diminuem na mesma proporção.

print(tabela.corr()[["Preco"]]) #faz a correlação só na coluna do preço

sns.heatmap(tabela.corr()[["Preco"]], annot=True, cmap="Blues") #criação do gráfico no estilo de mapa de calor (heatmap), pegando o preço, inserindo as anotações e usando a cor azul
plt.show() #exibe informações no gráfico

y = tabela["Preco"] #defino o que quero prever, no caso a coluna de preço
x = tabela.drop("Preco", axis=1) #características que serão usadas pra previsão, ou seja, todas as colunas menos a coluna de preço (axis=1 eixo das colunas e axis=0 eixo das linhas)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3) #O train_test_split faz divisão da base de dados para treino e parte para teste. Pois a IA precisa de parte da base de dados para treinar e o restante da base de dados para fazer as previsões. 

# cria dois modelos de inteligencias artificiais para compará-los
modelo_regressaolinear = LinearRegression() 
modelo_arvoredecisao = RandomForestRegressor() 

# treina as inteligencias artificias
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

previsao_regressaolinear = modelo_regressaolinear.predict(x_teste) #cria a previsão usando o modelo de regressão linear, com a base de teste
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste) #cria a previsão usando o modelo de árvore de decisão, com a base de teste

# compara os modelos
print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste, previsao_arvoredecisao))  

# monta para exibir os resultados num gráfico de linha
tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_teste"] = y_teste
tabela_auxiliar["Previsoes ArvoreDecisao"] = previsao_arvoredecisao
tabela_auxiliar["Previsoes Regressao Linear"] = previsao_regressaolinear

sns.lineplot(data=tabela_auxiliar) 
plt.show()

#Cria uma tabela com a previsão dos preços para cada produto com as especificações
nova_tabela = pd.read_csv("novos_barcos.csv")
print(nova_tabela)
previsao = modelo_arvoredecisao.predict(nova_tabela)
print(previsao)