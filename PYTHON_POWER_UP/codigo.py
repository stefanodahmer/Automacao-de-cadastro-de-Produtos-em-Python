import pyautogui
import time
import pandas as pd

# pyautogui.click -> clicar em alguma lugar
# pyautogui.press -> apertar uma tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinação de teclas (ctrl, c)

pyautogui.PAUSE = 0.3

# Passo 1 ENTRAR NO SISTEMA DA EMPRESA - https://dlp.hashtagtreinamentos.com/python/intensivao/tabela

pyautogui.press("win")  # tempo de espera entre cada comando
pyautogui.write("chrome")
pyautogui.press("enter")

site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(site)
pyautogui.press("enter")

time.sleep(0.5)
pyautogui.click(x=1842, y=41) 

#=======================================================================#

# PASSO 2 FAZER LOGIN

pyautogui.click(x=732, y=473)
pyautogui.write("generico@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("enter")

time.sleep(1.5)
pyautogui.click(x=1618, y=138)

#=======================================================================#
# PASSO 3 IMPORTAR A BASE DE DADOS
# import pandas as pd

tabela = pd.read_csv("PYTHON_POWER_UP/produtos.csv")

# PASSO 4 CADASTRAR UM PRODUTO
time.sleep(1.0)

pyautogui.click(x=680, y=316)  # clicar em adicionar produto



# PASSO 5 REPETIR PARA TODOS OS PRODUTOS

for linha in tabela.index:
    pyautogui.scroll(10000)  # scroll 

    pyautogui.click(x=680, y=316)  # clicar em adicionar produto

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    
    pyautogui.press("tab")
    pyautogui.press("enter")


# pyautogui  -> fazer automações com python