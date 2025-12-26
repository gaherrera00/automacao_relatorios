from pathlib import Path
import pandas as pd

from src.leitura import carregar_dados
from src.processamento import calcular_metricas
from src.relatorio_excel import gerar_relatorio_excel, nome_relatorio_excel_com_data
from src.relatorio_pdf import gerar_relatorio_pdf, nome_relatorio_pdf_com_data


def main():
    dados = carregar_dados("data/vendas.csv")
    if dados is None:
        print("Execução interrompida.")
        return

    # (se leitura.py já converteu, isso não atrapalha)
    dados["data"] = pd.to_datetime(dados["data"])

    metricas = calcular_metricas(dados)

    print("\n=== MÉTRICAS DE VENDAS ===")
    print(f"Faturamento total : R$ {metricas['faturamento_total']:,.2f}")
    print(f"Produto campeão   : {metricas['produto_campeao']}")
    print(f"Ticket médio      : R$ {metricas['ticket_medio']:,.2f}")
    print(f"Quantidade total  : {metricas['quantidade_total']}")
    print(f"Nº de vendas      : {metricas['numero_vendas']}")
    print("================================\n")

    # Excel
    xlsx_nome = nome_relatorio_excel_com_data()
    xlsx_saida = Path("output") / xlsx_nome
    gerar_relatorio_excel(metricas, str(xlsx_saida))
    print(f"Excel gerado: {xlsx_saida}")

    # PDF
    pdf_nome = nome_relatorio_pdf_com_data()
    pdf_saida = Path("output") / pdf_nome
    gerar_relatorio_pdf(metricas, str(pdf_saida))
    print(f"PDF gerado:   {pdf_saida}\n")


if __name__ == "__main__":
    main()
