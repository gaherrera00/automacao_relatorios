from pathlib import Path
import pandas as pd


COLUNAS_OBRIGATORIAS = ["data", "produto", "quantidade", "preco_unitario"]


def validar_colunas(df: pd.DataFrame) -> bool:
    # aceita colunas extras, mas exige as obrigatórias
    return set(COLUNAS_OBRIGATORIAS).issubset(df.columns)


def carregar_dados(caminho: str) -> pd.DataFrame | None:
    arquivo = Path(caminho)

    if not arquivo.exists():
        print("Erro: arquivo não encontrado.")
        return None

    if not arquivo.is_file():
        print("Erro: caminho inválido (não é arquivo).")
        return None

    if arquivo.suffix.lower() != ".csv":
        print("Erro: arquivo não é .csv.")
        return None

    try:
        df = pd.read_csv(arquivo, sep=",")
    except Exception as e:
        print(f"Erro: falha ao ler o CSV. Detalhe: {e}")
        return None

    if not validar_colunas(df):
        print(f"Erro: colunas obrigatórias ausentes. Esperado: {COLUNAS_OBRIGATORIAS}")
        print(f"Colunas encontradas: {list(df.columns)}")
        return None

    # normalizações de tipo
    df["data"] = pd.to_datetime(df["data"], errors="coerce")
    df["quantidade"] = pd.to_numeric(df["quantidade"], errors="coerce")
    df["preco_unitario"] = pd.to_numeric(df["preco_unitario"], errors="coerce")

    # validações básicas de dados
    if df["data"].isna().any():
        print("Erro: há datas inválidas na coluna 'data'.")
        return None

    if df["quantidade"].isna().any() or df["preco_unitario"].isna().any():
        print("Erro: há valores inválidos em 'quantidade' ou 'preco_unitario'.")
        return None

    # quantidade deve ser inteira e positiva
    if (df["quantidade"] <= 0).any():
        print("Erro: 'quantidade' deve ser > 0.")
        return None

    if (df["preco_unitario"] <= 0).any():
        print("Erro: 'preco_unitario' deve ser > 0.")
        return None

    # força tipos finais
    df["quantidade"] = df["quantidade"].astype(int)
    df["preco_unitario"] = df["preco_unitario"].astype(float)

    print("OK: arquivo carregado e validado.")
    return df
