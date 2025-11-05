import pandas as pd
from datetime import datetime
import os
import sys

# Pasta de dados
DATA_DIR = "data"

# Verifica se a pasta existe
if not os.path.exists(DATA_DIR):
    print("Pasta data não existe. Execute extract.py primeiro.")
    sys.exit(1)

# Procurar arquivos CSV de crypto e forex
crypto_file = os.path.join(DATA_DIR, "crypto_data.csv")
forex_file = os.path.join(DATA_DIR, "forex_data.csv")

if not os.path.exists(crypto_file) or not os.path.exists(forex_file):
    print("Arquivos CSV de extração não encontrados. Execute extract.py primeiro.")
    sys.exit(1)

# Ler CSVs
crypto_df = pd.read_csv(crypto_file)
forex_df = pd.read_csv(forex_file)

# Padronizar colunas e tipos
crypto_df["coin"] = crypto_df["coin"].astype(str).str.capitalize()
crypto_df["price_usd"] = pd.to_numeric(crypto_df["price_usd"], errors="coerce")
crypto_df["change_24h"] = pd.to_numeric(crypto_df["change_24h"], errors="coerce")
crypto_df["timestamp"] = pd.to_datetime(crypto_df["timestamp"], errors="coerce")

forex_df["currency"] = forex_df["currency"].astype(str).str.upper()
forex_df["rate"] = pd.to_numeric(forex_df["rate"], errors="coerce")
forex_df["timestamp"] = pd.to_datetime(forex_df["timestamp"], errors="coerce")

# Enriquecimento: converter USD para BRL/EUR
brl_rate = forex_df.loc[forex_df["currency"]=="BRL", "rate"].values[0] if "BRL" in forex_df["currency"].values else None
eur_rate = forex_df.loc[forex_df["currency"]=="EUR", "rate"].values[0] if "EUR" in forex_df["currency"].values else None

if brl_rate is not None:
    crypto_df["price_brl"] = crypto_df["price_usd"] * brl_rate
else:
    crypto_df["price_brl"] = None

if eur_rate is not None:
    crypto_df["price_eur"] = crypto_df["price_usd"] * eur_rate
else:
    crypto_df["price_eur"] = None

# Insight simples
if not crypto_df["change_24h"].isna().all():
    max_change = crypto_df.loc[crypto_df["change_24h"].abs().idxmax()]
    print(f"Maior variação: {max_change['coin']} ({max_change['change_24h']:.2f}%)")

# Salvar CSV transformado
transformed_file = os.path.join(DATA_DIR, f"transformed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
crypto_df.to_csv(transformed_file, index=False)

print(f"Transformado salvo em: {transformed_file}")
print(crypto_df.head())
