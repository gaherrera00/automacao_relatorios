# 📊 Automação de Relatórios de Vendas (Python)

## Descrição do Projeto

Este projeto em **Python** simula um **pipeline real de dados** em um ambiente corporativo. Ele realiza a leitura, validação e processamento de métricas de negócio a partir de um arquivo CSV de vendas, culminando na **geração automática de relatórios** em formatos Excel e PDF, prontos para análise e apresentação.

O objetivo é demonstrar a capacidade de ir da ingestão de dados brutos até a entrega de relatórios finais de forma estruturada e profissional.

---

## 🚀 Funcionalidades Principais

O script executa as seguintes tarefas:

*   **Leitura e Validação** de arquivo CSV de vendas.
*   **Tratamento e Normalização** de dados para garantir a qualidade.
*   **Cálculo de Métricas de Negócio (KPIs)**, incluindo:
    *   Faturamento total
    *   Quantidade total vendida
    *   Número de vendas
    *   Ticket médio
    *   Produto campeão
    *   Faturamento por produto e por dia
    *   Dia de maior faturamento
*   **Geração Automática de Relatórios** com nomeação dinâmica (incluindo data de geração):
    *   **📄 Excel (.xlsx)**: Com abas separadas, gráficos e formatação profissional.
    *   **📑 PDF Estilizado**: Contendo KPIs destacados, tabelas e gráficos para apresentação executiva.
*   **Estrutura Modular e Organizada**, seguindo um padrão de desenvolvimento profissional.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
| :--- | :--- |
| **Python 3** | Linguagem principal de desenvolvimento. |
| **pandas** | Manipulação e análise eficiente de dados. |
| **openpyxl** | Geração e formatação avançada de arquivos Excel. |
| **matplotlib** | Criação de gráficos para visualização de dados. |
| **reportlab** | Geração de relatórios em PDF com estilização. |
| **pathlib** | Manipulação de caminhos de arquivos de forma orientada a objetos. |

---

## 📂 Estrutura do Projeto

```
automacao_relatorios/
│
├── data/
│   └── vendas.csv              # Arquivo de dados de entrada
│
├── output/
│   ├── relatorio_YYYY-MM-DD.xlsx # Relatório Excel gerado
│   └── relatorio_YYYY-MM-DD.pdf  # Relatório PDF gerado
│
├── src/
│   ├── leitura.py            # Leitura e validação do CSV
│   ├── processamento.py     # Cálculo das métricas
│   ├── relatorio_excel.py   # Geração do relatório Excel
│   ├── relatorio_pdf.py     # Geração do relatório PDF
│   └── main.py               # Orquestração do fluxo principal
│
├── requirements.txt          # Dependências do projeto
├── .gitignore                # Arquivos a serem ignorados pelo Git
└── README.md                 # Este arquivo
```

---

## ▶️ Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o projeto em sua máquina local.

### 1. Clonar o Repositório

```bash
git clone <url-do-repositorio>
cd automacao_relatorios
```

### 2. Configurar o Ambiente Virtual

É altamente recomendado o uso de um ambiente virtual para isolar as dependências.

```bash
python -m venv venv
```

**Ativação do Ambiente:**

| Sistema Operacional | Comando de Ativação |
| :--- | :--- |
| **Windows** | `venv\Scripts\activate` |
| **Linux / Mac** | `source venv/bin/activate` |

### 3. Instalar Dependências

Com o ambiente virtual ativo, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

### 4. Executar o Script

Execute o arquivo principal para iniciar o pipeline de automação:

```bash
python -m src.main
```

---

## 📄 Resultado Esperado

Após a execução, dois arquivos de relatório serão gerados na pasta `output/`.

### 📊 Relatório Excel (`relatorio_YYYY-MM-DD.xlsx`)

O arquivo Excel é composto pelas seguintes abas e elementos visuais:

| Aba | Conteúdo |
| :--- | :--- |
| **Resumo** | KPIs principais e período analisado. |
| **Por Produto** | Ranking de produtos e participação percentual (%). |
| **Por Dia** | Faturamento diário. |
| **Detalhado** | Todas as vendas com a coluna de total calculada. |

**Gráficos Incluídos:**
*   Top 10 produtos por faturamento.
*   Faturamento por dia.

### 📑 Relatório PDF (`relatorio_YYYY-MM-DD.pdf`)

O PDF é formatado para uma **apresentação executiva** e contém:

*   Capa com título, data e período analisado.
*   KPIs destacados.
*   Gráficos de **Top 10 produtos por faturamento** e **Faturamento por dia**.
*   Tabela com Top 10 produtos e participação percentual.

---

## 🖥️ Exemplo de Saída no Terminal

```
=== MÉTRICAS DE VENDAS ===
Faturamento total : R$ 683.177,68
Produto campeão   : Notebook
Ticket médio      : R$ 4.554,52
Quantidade total  : 864
Nº de vendas      : 150
================================

Excel gerado: output/relatorio_2025-12-26.xlsx
PDF gerado:   output/relatorio_2025-12-26.pdf
```

---

## 📌 Observações Finais

Este projeto é um excelente material para portfólio em Python e Análise de Dados, destacando:

*   Estrutura com separação clara de responsabilidades.
*   Código limpo, modular e fácil de manter.
*   Relatórios pensados para uso e consumo corporativo.

---

## 👨‍💻 Autor

**Gabriel Herrera Demarchi**

*Projeto desenvolvido para fins de estudo e demonstração técnica.*
