from pathlib import Path
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
)


def nome_relatorio_pdf_com_data() -> str:
    return f"relatorio_{date.today().isoformat()}.pdf"


def _salvar_grafico_top_produtos(metricas: dict, caminho_png: Path):
    top = metricas["top_produtos"]
    plt.figure()
    top.sort_values().plot(kind="barh")
    plt.title("Top 10 Produtos por Faturamento")
    plt.tight_layout()
    plt.savefig(caminho_png, dpi=180)
    plt.close()


def _salvar_grafico_por_dia(metricas: dict, caminho_png: Path):
    serie = metricas["faturamento_por_dia"]
    plt.figure()
    serie.plot()
    plt.title("Faturamento por Dia")
    plt.tight_layout()
    plt.savefig(caminho_png, dpi=180)
    plt.close()


def gerar_relatorio_pdf(metricas: dict, caminho_saida: str) -> str:
    saida = Path(caminho_saida)
    saida.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(saida),
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36,
    )
    styles = getSampleStyleSheet()
    elementos = []

    # Cabeçalho
    elementos.append(Paragraph("<b>Relatório de Vendas</b>", styles["Title"]))
    elementos.append(Spacer(1, 8))
    elementos.append(
        Paragraph(f"Gerado em: <b>{date.today().isoformat()}</b>", styles["Normal"])
    )

    ini = metricas["periodo_inicio"]
    fim = metricas["periodo_fim"]
    if pd.notna(ini) and pd.notna(fim):
        elementos.append(
            Paragraph(
                f"Período analisado: <b>{ini.date()}</b> até <b>{fim.date()}</b>",
                styles["Normal"],
            )
        )
    elementos.append(Spacer(1, 12))

    # KPIs
    kpi_data = [
        ["Faturamento total", f"R$ {metricas['faturamento_total']:,.2f}"],
        ["Quantidade total", f"{metricas['quantidade_total']}"],
        ["Número de vendas", f"{metricas['numero_vendas']}"],
        ["Ticket médio", f"R$ {metricas['ticket_medio']:,.2f}"],
        ["Produto campeão", metricas["produto_campeao"]],
        [
            "Dia recorde",
            str(metricas["dia_recorde"]) if metricas["dia_recorde"] else "",
        ],
        ["Faturamento dia recorde", f"R$ {metricas['faturamento_dia_recorde']:,.2f}"],
    ]

    elementos.append(Paragraph("<b>Resumo (KPIs)</b>", styles["Heading2"]))
    t = Table(kpi_data, colWidths=[220, 260])
    t.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.grey),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.grey),
                (
                    "ROWBACKGROUNDS",
                    (0, 0),
                    (-1, -1),
                    [colors.whitesmoke, colors.lightgrey],
                ),
                ("ALIGN", (1, 0), (1, -1), "RIGHT"),
            ]
        )
    )
    elementos.append(t)
    elementos.append(Spacer(1, 12))

    # Gráficos temporários
    pasta_temp = saida.parent
    png_top = pasta_temp / "tmp_top_produtos.png"
    png_dia = pasta_temp / "tmp_faturamento_dia.png"

    _salvar_grafico_top_produtos(metricas, png_top)
    _salvar_grafico_por_dia(metricas, png_dia)

    elementos.append(Paragraph("<b>Gráficos</b>", styles["Heading2"]))
    elementos.append(Spacer(1, 6))
    elementos.append(Image(str(png_top), width=520, height=260))
    elementos.append(Spacer(1, 10))
    elementos.append(Image(str(png_dia), width=520, height=260))
    elementos.append(Spacer(1, 12))

    # Tabela Top 10
    top = metricas["top_produtos"]
    part = metricas["participacao_top"]
    linhas = [["Produto", "Faturamento (R$)", "Participação (%)"]]
    for produto, valor in top.items():
        pct = float(part.loc[produto]) if produto in part.index else 0.0
        linhas.append([produto, f"{valor:,.2f}", f"{pct:.2f}%"])

    elementos.append(Paragraph("<b>Top 10 Produtos</b>", styles["Heading2"]))
    tt = Table(linhas, colWidths=[240, 160, 80])
    tt.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.black),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
            ]
        )
    )
    elementos.append(tt)

    doc.build(elementos)

    # limpar temporários
    try:
        png_top.unlink(missing_ok=True)
        png_dia.unlink(missing_ok=True)
    except Exception:
        pass

    return str(saida)
