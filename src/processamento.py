def calcular_metricas(dados) -> dict:
    dados = dados.copy()

    # total por linha
    dados["total"] = dados["quantidade"] * dados["preco_unitario"]

    # faturamento_total
    faturamento_total = dados["total"].sum()

    # quantidade_total
    quantidade_total = dados["quantidade"].sum()

    # faturamento_por_produto
    faturamento_por_produto = (
        dados.groupby("produto")["total"].sum().sort_values(ascending=False)
    )

    # produto_campeao
    produto_campeao = faturamento_por_produto.index[0]

    # ticket_medio
    ticket_medio = faturamento_total / len(dados)

    # Empacota tudo em um dicionário
    metricas = {
        "faturamento_total": faturamento_total,
        "quantidade_total": quantidade_total,
        "ticket_medio": ticket_medio,
        "produto_campeao": produto_campeao,
        "faturamento_por_produto": faturamento_por_produto,
        "df": dados,
    }
    return metricas
