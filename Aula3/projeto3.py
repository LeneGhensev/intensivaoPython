from selenium import webdriver
import pandas as pd

navegador = webdriver.Chrome() #necessário baixar o chromedriver e salvar no mesmo local que o python está instalado
navegador.get("https://www.google.com/")

tabela = pd.read_excel("commodities.xlsx")
print(tabela)

for linha in tabela.index: #para cada linha detnro das linhas da tabela
    produto = tabela.loc[linha, "Produto"] #descobre qual é o produto, no 'loc' informa linha e coluna do campo que desejo
    
    print(produto)
    produto = produto.replace("ó", "o").replace("ã", "a").replace("á", "a").replace(
    "ç", "c").replace("ú", "u").replace("é", "e") #o 'replace' transforma o texto, substituindo os campos. Como os nomes de alguns produtos possuem acentuação, retirar pra conseguir fazer a busca na url
    
    link = f"https://www.melhorcambio.com/{produto}-hoje"
    print(link)
    navegador.get(link)

    preco = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value') #primeiro procura por um elemento na página e de depois pega os dados que estão no campo desse XPath //*[@id="comercial"], no caso pega o atributo value 
    preco = preco.replace(".", "").replace(",", ".") #o 'replace' transforma o texto, substituindo os campos
    print(preco)
    tabela.loc[linha, "Preço Atual"] = float(preco) #o 'loc' informa linha e coluna do campo que deverá ser editado na tabela e depois o float vai transformar em número
    
print("Acabou")
print(tabela)

tabela["Comprar"] = tabela["Preço Atual"] < tabela["Preço Ideal"] #informa se true ou false e preenche na coluna Comprar
print(tabela)

# tabela.to_excel("commodities_atualizado.xlsx", index=False) #exporta a tabela para o excel, retirando a coluna de índices

navegador.quit() #fecha o navegador   