import pyautogui
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#git add .
#git commit -m "Mensagem explicando a alteração"
#git push


# pyautogui.click -> clicar em alguma lugar
# pyautogui.press -> apertar uma tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinação de teclas (ctrl, c)

pyautogui.PAUSE = 0.3

# Passo 1 ENTRAR NO SISTEMA DA EMPRESA - https://dlp.hashtagtreinamentos.com/python/intensivao/tabela

#pyautogui.press("win")  # tempo de espera entre cada comando
#pyautogui.write("chrome")
#pyautogui.press("enter")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
driver.get(site)

time.sleep(1.0)


#=======================================================================#

# PASSO 2 FAZER LOGIN

email = driver.find_element(By.ID, "email")
senha = driver.find_element(By.ID, "password")

email.send_keys("generico@gmail.com")
senha.send_keys("senha123")
senha.send_keys(Keys.ENTER)

time.sleep(2)
#=======================================================================#
# PASSO 3 IMPORTAR A BASE DE DADOS
# import pandas as pd

tabela = pd.read_csv("PYTHON_POWER_UP/produtos.csv")

# PASSO 4 CADASTRAR UM PRODUTO
# PASSO 5 REPETIR PARA TODOS OS PRODUTOS

for linha in tabela.index:
    pyautogui.scroll(10000)  # scroll 

    driver.find_element(By.XPATH, '//*[@id="codigo"]').click()

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