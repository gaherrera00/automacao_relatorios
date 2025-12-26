# importacao das bibliotecas
from pathlib import Path
import pandas as pd


# Carrega o csv e valida ele
def carregar_dados(caminho):
    arquivo = Path(caminho)
    # Verifica se existe algo em data
    if arquivo.exists():
        # Verifica se é um arquivo
        if arquivo.is_file():
            try:
                # Verifica se o arquivo é um csv
                df = pd.read_csv(arquivo, sep=",")
                print("\n## Arquivo encontrado com sucesso ##")
                return df
            except Exception:
                print("\n## Arquivo de formato incompativel ##")
                return None
        else:
            print("\n## Arquivo invalido,é um diretorio ou outro tipo de caminho ##")
            return None
    else:
        print("\n## Arquivo não encontrado##\n")
        return None


# verifica se o arquivo tem os valores necessarios
def validar_colunas(dados):
    lista_chegando = list(dados.columns)
    lista_esperada = ["data", "produto", "quantidade", "preco_unitario"]
    if lista_esperada == lista_chegando:
        print("## Colunas como o padrao ##\n")
        return True
    else:
        print("## Colunas fora do padrao ##\n")
        return False
