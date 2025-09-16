import pyautogui as pa
import time
import pandas as pd

# Time para as ações
pa.PAUSE = 0.5

# Abrir o navegador
pa.press("win")
pa.write("Chrome")
pa.press("enter")

# Entrar no site
pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pa.press("enter")

# Sleep de 1 segundo

time.sleep(1)

# Insere o login
pa.click(x=756, y=371)
pa.write("arthurzaca@gmail.com")

# Insere a senha
pa.press("tab")
pa.write("123456789")
pa.press("tab")

# Envia
pa.press("enter")

# Lê a tabela
tabela = pd.read_csv("C:\\Users\\Arthur\\Documents\\vscode\\EstudandoPython\\Jornada Python - Hashtag\\Aula 01\\produtos.csv")

# Loop para inserir os produtos
for linha in tabela.index:
    # Começa a inserir os dados
    # codigo
    pa.click(x=714, y=257)
    codigo = tabela.loc[linha, "codigo"]
    pa.write(str(codigo))

    # marca
    pa.press("tab")
    marca = tabela.loc[linha, "marca"]
    pa.write(str(marca))

    # tipo
    pa.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pa.write(str(tipo))

    # categoria
    pa.press("tab")
    categoria = tabela.loc[linha, "categoria"]
    pa.write(str(categoria))

    # preco_unitario
    pa.press("tab")
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pa.write(str(preco_unitario))

    # custo
    pa.press("tab")
    custo = tabela.loc[linha, "custo"]
    pa.write(str(custo))

    # observacao
    pa.press("tab")
    observacao = tabela.loc[linha, "obs"]

    # Valida se a observação é um NaN
    if str(observacao) != "nan":
        pa.write(str(observacao))

    # Sleep de 1 s
    time.sleep(1)

    # Salva o produto  Hashtag 
    pa.press("tab")
    pa.press("enter")

    # Volta o scroll pra cima
    pa.scroll(10000)

    