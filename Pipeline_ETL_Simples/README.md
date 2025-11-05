# Pipeline_ETL_Simples

Este projeto é um exemplo de **pipeline ETL (Extract, Transform, Load)** simples, desde a geração de um dataset fictício até a análise de dados.  
O objetivo é demonstrar o fluxo completo de dados, manipulação com Python e criação de visualizações.

---

## 🗂 Estrutura do Repositório

Pipeline_ETL_Simples/
Data/
        └─ vendas.db # Dataset gerado
        └── banco_vendas.db # Banco SQLite gerado pelo ETL
notbooks/ 
        └─01_Pipeline_ETL_Simples.ipynb # Pipeline ETL completo
         └─ 02_Analise_Vendas.ipynb # Consultas SQL e gráficos
         └── 03_analise_dados.ipynb # Análise de dados: EDA, gráficos e insights
README.md

---

## **🛠 Tecnologias utilizadas**

- **Python** – manipulação de dados e scripts ETL  
- **pandas** – tratamento e análise de dados  
- **sqlite3** – armazenamento de dados em banco SQLite  
- **Matplotlib / Seaborn** – visualização de dados  
- **Google Colab** – ambiente de desenvolvimento  

---

## **📌 Descrição dos notebooks**

### 1️⃣ 01_geracao_dataset.ipynb
- Cria um dataset fictício de vendas com colunas como `produto`, `preco`, `quantidade` e `data_venda`  
- Salva o dataset em CSV (`data/vendas.csv`)  

### 2️⃣ 02_pipeline_ETL.ipynb
- Carrega o CSV do notebook anterior  
- Realiza transformações e limpeza (remover duplicados, ajustar tipos de dados)  
- Salva os dados transformados em um **banco SQLite** (`data/banco_vendas.db`)  

### 3️⃣ 03_analise_dados.ipynb
- Conecta ao banco SQLite e carrega os dados em um DataFrame  
- Faz **análise exploratória** (EDA): linhas, colunas, tipos de dados, valores nulos, estatísticas descritivas  
- Cria gráficos e visualizações:  
  - Distribuição de preços  
  - Total de vendas por produto  
  - Evolução de vendas ao longo do tempo  
- Salva os gráficos como imagens (`.png`) para portfólio ou redes sociais  

---

## **⚡ Como executar o projeto**

1. Abra o **Google Colab** ou seu ambiente local  
2. Abra e execute os notebooks na ordem:  
3. Verifique se a pasta `data/` contém o CSV e o banco SQLite  
4. Os gráficos gerados serão exibidos no notebook e também podem ser salvos como imagens  

---

## **📊 Objetivo do projeto**

- Demonstrar **pipeline ETL completo** de dados fictícios  
- Mostrar capacidade de:  
- Gerar datasets realistas  
- Limpar e transformar dados  
- Criar banco de dados para análise  
- Gerar visualizações e insights  
- Servir como **portfólio** para vagas em **engenharia de dados** ou análise de dados  

---

## **📌 Observações**

- O projeto foi feito de forma **didática e simples**, ideal para estudantes e iniciantes em ETL e análise de dados  
- Todos os caminhos de arquivos estão centralizados na pasta `data/` para organização  

---


