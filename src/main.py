import pandas as pd
from src.leitura import carregar_dados
from src.processamento import calcular_metricas

dados = carregar_dados("data/vendas.csv")

if dados is None:
    exit()

dados["data"] = pd.to_datetime(dados["data"])

metricas = calcular_metricas(dados)
print("\n=== MÉTRICAS DE VENDAS ===")
print(f"Faturamento total : R$ {metricas['faturamento_total']:.2f}")
print(f"Produto campeão   : {metricas['produto_campeao']}")
print(f"Ticket médio      : R$ {metricas['ticket_medio']:.2f}")
