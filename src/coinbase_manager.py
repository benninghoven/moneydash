from globals import GLOBALS as G
from load_credentials import LoadCredentials
import time
import hmac
import hashlib
import requests


def FetchPriceOf(cryptoKey):
    url = 'https://api.coinbase.com/v2/prices/{}/spot'
    response = requests.get(url.format(cryptoKey + '-USD'))
    data = response.json()
    crypto_price = data['data']['amount']
    return float(crypto_price)


def FetchCoinbaseData():

    loot = dict()

    credentials = LoadCredentials(G.credentialsPath)
    coinbaseCredentials = credentials["coinbase"]
    API_KEY = coinbaseCredentials["api_key"]
    API_SECRET = coinbaseCredentials["api_secret"]

    URL = 'https://api.coinbase.com/v2/accounts'
    headers = {
        'CB-ACCESS-KEY': API_KEY,
        'CB-ACCESS-SIGN': '',
        'CB-ACCESS-TIMESTAMP': '',
        'CB-VERSION': '2017-08-07',
    }

    timestamp = str(int(time.time()))
    message = timestamp + 'GET' + '/v2/accounts' + ''  # empty body for GET requests
    signature = hmac.new(API_SECRET.encode(), message.encode(), hashlib.sha256).hexdigest()
    headers['CB-ACCESS-SIGN'] = signature
    headers['CB-ACCESS-TIMESTAMP'] = timestamp
    response = requests.get(URL, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for account in data['data']:
            currency = account["currency"]
            code = currency["code"]
            if account['type'] == 'wallet':
                amount = float(account["balance"]["amount"])
                if amount > 0.0:
                    code = account["balance"]["currency"]
                    total_value = FetchPriceOf(code)*amount
                    loot[code] = {"amount_of_coins": amount,
                                  "total_value": total_value,
                                  }
        return loot
    else:
        print('Request failed with status code:', response.status_code)
        return None
# Check response status code
