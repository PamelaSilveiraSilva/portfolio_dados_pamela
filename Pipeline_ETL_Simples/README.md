#🚀 Portfólio de Engenharia de Dados – ETL & Análise de Vendas

Este repositório reúne projetos de Engenharia de Dados, mostrando todo o fluxo ETL (Extração, Transformação e Carga) aplicado a dados de vendas, além de análises e visualizações. Ideal para demonstrar habilidades práticas para recrutadores!


🗂 Estrutura do Repositório

portfolio/
 ├─ notebooks/
 │    ├─ 01_Pipeline_ETL_Simples.ipynb   # Pipeline ETL completo
 │    └─ 02_Analise_Vendas.ipynb         # Consultas SQL e gráficos
 ├─ database/
 │    └─ vendas.db                        # Banco SQLite com dados tratados
 └─ README.md                             # Este arquivo

 🚀 Projetos
1️⃣ Pipeline ETL – Vendas

Objetivo: Demonstrar o fluxo completo de ETL, desde a leitura do CSV até o armazenamento em banco de dados.

Principais etapas:

Extração dos dados do CSV 📥

Transformação: limpeza, padronização, tratamento de nulos e criação da coluna valor_total 🔄💰

Carga no banco SQLite 💾

Ferramentas usadas: Python (pandas), SQLite, Colab

2️⃣ Análise de Vendas

Objetivo: Gerar insights a partir do banco de dados criado no pipeline ETL.

Principais análises:

Total de vendas por cidade 🏙️

Total de vendas por produto 👗👖

Quantidade de vendas por vendedor 🧑‍💼

Evolução das vendas ao longo do tempo 📈

Ferramentas usadas: Python (pandas, matplotlib, seaborn), SQLite

💡 Insights e Aprendizado

Aprendi a construir pipelines ETL simples e funcionais

Pratiquei consultas SQL e manipulação de dados

Desenvolvi visualizações claras e interativas para comunicar resultados

Criei um projeto pronto para portfólio de Engenharia de Dados

📌 Como usar

Clonar o repositório:
git clone https://github.com/PamelaSilveiraSilva/portfolio_dados_pamela.git

Abrir os notebooks no Colab ou Jupyter.

Rodar primeiro o notebook 01_Pipeline_ETL_Simples.ipynb para criar o banco.

Rodar depois o notebook 02_Analise_Vendas.ipynb para gerar gráficos e insights.

🛠 Ferramentas e Tecnologias

Python: pandas, matplotlib, seaborn

Banco de dados: SQLite

Plataforma: Google Colab
