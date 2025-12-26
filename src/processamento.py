import pandas as pd


def calcular_metricas(df: pd.DataFrame) -> dict:
    df = df.copy()

    # total por linha
    df["total"] = df["quantidade"] * df["preco_unitario"]

    faturamento_total = float(df["total"].sum())
    quantidade_total = int(df["quantidade"].sum())
    numero_vendas = int(len(df))
    ticket_medio = float(faturamento_total / numero_vendas) if numero_vendas else 0.0

    # período
    periodo_inicio = df["data"].min()
    periodo_fim = df["data"].max()

    # por produto
    faturamento_por_produto = (
        df.groupby("produto")["total"].sum().sort_values(ascending=False)
    )

    produto_campeao = (
        str(faturamento_por_produto.index[0]) if len(faturamento_por_produto) else ""
    )

    # participação por produto (%)
    participacao_por_produto = (
        (faturamento_por_produto / faturamento_total * 100).round(2)
        if faturamento_total
        else faturamento_por_produto * 0
    )

    top_produtos = faturamento_por_produto.head(10)
    participacao_top = participacao_por_produto.head(10)

    # por dia
    faturamento_por_dia = df.groupby(df["data"].dt.date)["total"].sum().sort_index()

    dia_recorde = faturamento_por_dia.idxmax() if len(faturamento_por_dia) else None
    faturamento_dia_recorde = (
        float(faturamento_por_dia.max()) if len(faturamento_por_dia) else 0.0
    )

    # stats
    stats = {
        "media_quantidade": float(df["quantidade"].mean()),
        "mediana_quantidade": float(df["quantidade"].median()),
        "media_preco_unitario": float(df["preco_unitario"].mean()),
        "mediana_preco_unitario": float(df["preco_unitario"].median()),
    }

    return {
        "faturamento_total": faturamento_total,
        "quantidade_total": quantidade_total,
        "numero_vendas": numero_vendas,
        "ticket_medio": ticket_medio,
        "produto_campeao": produto_campeao,
        "periodo_inicio": periodo_inicio,
        "periodo_fim": periodo_fim,
        "faturamento_por_produto": faturamento_por_produto,
        "participacao_por_produto": participacao_por_produto,
        "top_produtos": top_produtos,
        "participacao_top": participacao_top,
        "faturamento_por_dia": faturamento_por_dia,
        "dia_recorde": dia_recorde,
        "faturamento_dia_recorde": faturamento_dia_recorde,
        "stats": stats,
        "df": df,  # detalhado com total
    }
