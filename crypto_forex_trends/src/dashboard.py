# src/dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

st.set_page_config(page_title="Crypto & Forex Dashboard", layout="wide")
st.title("📊 Crypto & Forex Realtime Dashboard")

# Conecta ao banco SQLite gerado pelo ETL
db_path = "data/crypto_forex.db"  # altere se seu banco tiver outro nome
try:
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM crypto", conn)
except Exception as e:
    st.error(f"Erro ao acessar o banco SQLite: {e}")
    st.stop()
finally:
    conn.close()

# Gráfico 1: Preço das Criptos em USD
fig_usd = px.bar(df, x="coin", y="price_usd", color="coin",
                 title="💵 Preço das Criptomoedas (USD)")
st.plotly_chart(fig_usd, use_container_width=True)

# Gráfico 2: Preço das Criptos em BRL e EUR
df_melt = df.melt(id_vars=["coin"], value_vars=["price_brl","price_eur"],
                  var_name="Currency", value_name="Price")
fig_fx = px.bar(df_melt, x="coin", y="Price", color="Currency",
                barmode="group", title="💱 Preço das Criptos em BRL e EUR")
st.plotly_chart(fig_fx, use_container_width=True)

# Gráfico 3: Variação diária
fig_change = px.bar(df, x="coin", y="change_24h", color="coin",
                    title="📉 Variação diária (%)")
st.plotly_chart(fig_change, use_container_width=True)

# Tabela de dados
st.subheader("📄 Dados detalhados")
st.dataframe(df)
