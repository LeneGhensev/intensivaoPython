import pyautogui
import pyperclip
import time
import pandas as pd

pyautogui.PAUSE = 1 #define um valor fixado para pausa entre cada comando

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.hotkey("ctrl", "t") #atalho para abrir nova aba
pyperclip.copy("https://drive.google.com/drive/folders/160LsOE-hqu7W6i-E8v63N-ZsbWDbz7yV")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)

#time.sleep(5)
#print(pyautogui.position()) usar esses dois comando para verificar posição do mouse
pyautogui.hotkey("alt", "F10") #atalho para maximizar a tela
pyautogui.click(x=411, y=411, clicks=2)
time.sleep(5)

pyautogui.click(x=1284, y=125) # clicar no fazer download

tabela = pd.read_csv(r"C:\Users\Lene Ghensev\Downloads\Compras.csv", sep=";")
print(tabela)

faturamento = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = faturamento / quantidade

print(faturamento)
print(quantidade)
print(preco_medio)

pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(10)

pyautogui.click(x=74, y=177)

time.sleep(5)
pyautogui.click(x=875, y=246)
pyautogui.write("lenegghensev@gmail.com")
pyautogui.press("tab")

pyautogui.press("tab")
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab")

texto = f"""
Prezados,

Segue relatório do total de vendas de ontem.

Faturamento: R${faturamento:,.2f}
Quantidade de produtos vendidos: {quantidade:,}
Preço Médio: R${preco_medio:,.2f}

Qualquer dúvida estou à disposição.
Att.,
Lene Ghensev
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("ctrl", "enter") #atalho para enviar a mensagem