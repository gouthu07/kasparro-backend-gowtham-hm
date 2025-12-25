import requests
from datetime import datetime

URL = "https://api.coinpaprika.com/v1/tickers"

def fetch_coinpaprika_data(limit=10):
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    data = response.json()[:limit]

    records = []
    for coin in data:
        records.append({
            "source": "coinpaprika",
            "id": coin["id"],
            "symbol": coin["symbol"],
            "price": coin["quotes"]["USD"]["price"],
            "timestamp": datetime.utcnow().isoformat()
        })

    return records
