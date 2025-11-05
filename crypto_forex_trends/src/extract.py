import requests
import pandas as pd
from datetime import datetime
import os

# Criar pasta data se não existir
os.makedirs("data", exist_ok=True)

def get_crypto_data(crypto_list=["bitcoin","ethereum"]):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(crypto_list),
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    resp = requests.get(url, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    df = pd.DataFrame(data).T.reset_index()
    df.columns = ["coin","price_usd","change_24h"]
    df["timestamp"] = datetime.now()
    return df

def get_forex_data(base="USD", symbols=["EUR","BRL"]):
    url = f"https://api.frankfurter.app/latest?from={base}&to={','.join(symbols)}"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    if "rates" not in data:
        return pd.DataFrame(columns=["currency","rate","timestamp"])
    df = pd.DataFrame(list(data["rates"].items()), columns=["currency","rate"])
    df["timestamp"] = datetime.now()
    return df

def save_csv(df, filename):
    path = os.path.join("data", filename)
    df.to_csv(path, index=False)
    return path

if __name__ == "__main__":
    crypto_df = get_crypto_data(["bitcoin","ethereum"])
    forex_df = get_forex_data("USD", ["BRL","EUR"])

    crypto_path = save_csv(crypto_df, "crypto_data.csv")
    forex_path = save_csv(forex_df, "forex_data.csv")

    print(f"Crypto salvo em: {crypto_path}")
    print(f"Forex salvo em: {forex_path}")
    print(crypto_df)
    print(forex_df)
