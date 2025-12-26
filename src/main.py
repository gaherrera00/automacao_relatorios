from src.leitura import carregar_dados
from src.processamento import calcular_metricas
from src.relatorio import gerar_relatorio_excel, nome_relatorio_com_data
from pathlib import Path
import pandas as pd

# 1) Leitura
dados = carregar_dados("data/vendas.csv")
if dados is None:
    exit()

# 2) Normalização
dados["data"] = pd.to_datetime(dados["data"])

# 3) Processamento (AQUI metricas é criada)
metricas = calcular_metricas(dados)

# 4) Relatório
df_detalhado = metricas["df"]
nome_arquivo = nome_relatorio_com_data()
caminho_saida = Path("output") / nome_arquivo

gerar_relatorio_excel(metricas, df_detalhado, str(caminho_saida))

print(f"\nRelatório gerado com sucesso em: {caminho_saida}\n")
