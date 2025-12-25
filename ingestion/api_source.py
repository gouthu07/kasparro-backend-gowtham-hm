import requests

def fetch_api_data(api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    resp = requests.get("https://api.example.com/data", headers=headers)
    return resp.json()
