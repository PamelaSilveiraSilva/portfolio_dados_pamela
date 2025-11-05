# src/load.py
import pandas as pd
from sqlalchemy import create_engine
import os
import sys

# criar pasta data se não existir
os.makedirs("data", exist_ok=True)

DB_PATH = "sqlite:///data/crypto_forex.db"
engine = create_engine(DB_PATH, echo=False)

def load_csv_to_sql(csv_path, table_name):
    if not os.path.exists(csv_path):
        print(f"Arquivo não encontrado: {csv_path}")
        return
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, engine, if_exists="append", index=False)
    print(f"Dados de {csv_path} inseridos na tabela {table_name}.")

if __name__ == "__main__":
    # exemplo: carregar último transformed_*.csv
    files = [f for f in os.listdir("data") if f.startswith("transformed_") and f.endswith(".csv")]
    if not files:
        print("Nenhum arquivo transformed_*.csv encontrado. Rode transform.py primeiro.")
        sys.exit(1)
    files.sort()
    last = files[-1]
    load_csv_to_sql(os.path.join("data", last), "crypto")
