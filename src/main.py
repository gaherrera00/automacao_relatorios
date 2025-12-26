import pandas as pd
from src.leitura import carregar_dados, validar_colunas

dados = carregar_dados("data/vendas.csv")

if dados is not None and validar_colunas(dados):
    dados["data"] = pd.to_datetime(dados["data"])
    print(dados.head())
    print(dados.dtypes)
    print(dados.shape)
