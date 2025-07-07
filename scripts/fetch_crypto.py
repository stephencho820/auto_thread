import requests

def get_hot_cryptos():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "percent_change_24h_desc",
        "per_page": 3,
        "page": 1
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    cryptos = get_hot_cryptos()
    print(cryptos)
