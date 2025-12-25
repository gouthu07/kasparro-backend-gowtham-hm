import requests
from datetime import datetime

URL = "https://api.coingecko.com/api/v3/coins/markets"

def fetch_coingecko_data(limit=10):
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1
    }

    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    records = []
    for coin in data:
        records.append({
            "source": "coingecko",
            "id": coin["id"],
            "symbol": coin["symbol"],
            "price": coin["current_price"],
            "timestamp": datetime.utcnow().isoformat()
        })

    return records
