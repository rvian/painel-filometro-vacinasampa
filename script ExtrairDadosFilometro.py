# acessar API via HttpPost.
import requests as r
# arquivo de retorno para o Power BI (DataFrame)
import pandas as pd


url = "https://deolhonafila.prefeitura.sp.gov.br/processadores/dados.php"

resposta = r.post(url, data={"dados":"dados"}).json()
# "converte" json para um objeto DataFrame (lib pandas), tipo de objeto esperado pelo Power BI
dataFrame = pd.DataFrame.from_dict(resposta)

print(dataFrame.describe())


# print(dataFrame)
