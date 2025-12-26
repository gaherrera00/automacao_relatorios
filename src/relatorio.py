from pathlib import Path
from datetime import date
import pandas as pd


def gerar_relatorio_excel(
    metricas: dict, df_detalhado: pd.DataFrame, caminho_saida: str
) -> str:
    """
    Gera um arquivo Excel com duas abas:
      - Resumo: métricas principais
      - Detalhado: tabela completa (inclui coluna 'total')

    Retorna o caminho final do arquivo gerado (string).
    """
    saida = Path(caminho_saida)
    saida.parent.mkdir(parents=True, exist_ok=True)

    df_resumo = pd.DataFrame(
        {
            "Métrica": [
                "Faturamento total",
                "Quantidade total",
                "Produto campeão",
                "Ticket médio",
            ],
            "Valor": [
                metricas["faturamento_total"],
                metricas["quantidade_total"],
                metricas["produto_campeao"],
                metricas["ticket_medio"],
            ],
        }
    )

    with pd.ExcelWriter(saida, engine="openpyxl") as writer:
        df_resumo.to_excel(writer, sheet_name="Resumo", index=False)
        df_detalhado.to_excel(writer, sheet_name="Detalhado", index=False)

        wb = writer.book
        ws_resumo = wb["Resumo"]
        ws_det = wb["Detalhado"]

        # ===== Resumo =====
        for cell in ws_resumo[1]:
            cell.font = cell.font.copy(bold=True)

        ws_resumo.column_dimensions["A"].width = 22
        ws_resumo.column_dimensions["B"].width = 22

        ws_resumo["B2"].number_format = "R$ #,##0.00"  # faturamento_total
        ws_resumo["B3"].number_format = "0"  # quantidade_total
        ws_resumo["B5"].number_format = "R$ #,##0.00"  # ticket_medio

        # ===== Detalhado =====
        for cell in ws_det[1]:
            cell.font = cell.font.copy(bold=True)

        # Ajuste de largura (se existir a coluna, aplica)
        colunas_largura = {
            "data": 14,
            "produto": 18,
            "quantidade": 12,
            "preco_unitario": 16,
            "total": 16,
        }

        # Mapa: nome_da_coluna -> letra no Excel (A, B, C...)
        # (Excel começa em 1; DataFrame começa em 0)
        letras = {}
        for i, nome_col in enumerate(df_detalhado.columns, start=1):
            letras[nome_col] = _num_para_letra(i)

        for nome_col, largura in colunas_largura.items():
            if nome_col in letras:
                ws_det.column_dimensions[letras[nome_col]].width = largura

        # Formatação por tipo/semântica
        # - data: formato de data
        # - quantidade: inteiro
        # - preco_unitario e total: moeda
        col_data = letras.get("data")
        col_qtd = letras.get("quantidade")
        col_preco = letras.get("preco_unitario")
        col_total = letras.get("total")

        for row in range(2, ws_det.max_row + 1):
            if col_data:
                ws_det[f"{col_data}{row}"].number_format = "YYYY-MM-DD"
            if col_qtd:
                ws_det[f"{col_qtd}{row}"].number_format = "0"
            if col_preco:
                ws_det[f"{col_preco}{row}"].number_format = "R$ #,##0.00"
            if col_total:
                ws_det[f"{col_total}{row}"].number_format = "R$ #,##0.00"

    return str(saida)


def nome_relatorio_com_data() -> str:
    """Gera nome padrão relatorio_YYYY-MM-DD.xlsx"""
    hoje = date.today().isoformat()
    return f"relatorio_{hoje}.xlsx"


def _num_para_letra(n: int) -> str:
    """Converte 1->A, 2->B, ..., 26->Z, 27->AA, etc."""
    letras = ""
    while n > 0:
        n, resto = divmod(n - 1, 26)
        letras = chr(65 + resto) + letras
    return letras
