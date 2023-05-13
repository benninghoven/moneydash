import robin_stocks.robinhood as r
import pyotp

from globals import GLOBALS as G
from load_credentials import LoadCredentials
from classes.investment import Investment


def GetPriceOfCrypto(key, totalShares):
    crypto_info = r.crypto.get_crypto_quote(key)
    return float(crypto_info['mark_price']) * totalShares


def FetchRobinhoodInvestments():
    loot = []

    credentials = LoadCredentials(G.credentialsPath)
    robinhoodCredentials = credentials["robinhood"]
    username = robinhoodCredentials["username"]
    password = robinhoodCredentials["password"]
    otp_secret = credentials["otp_secret"]
    totp = pyotp.TOTP(otp_secret).now()

    r.login(username, password, mfa_code=totp)

# shares
    holdings = r.build_holdings()
    for key, value in holdings.items():
        quant = float(value['quantity'])
        share_price = float(value['price'])
        total_value = quant * share_price
        temp = Investment(key, quant, total_value)
        loot.append(temp)

# crypto
    crypto_positions = r.crypto.get_crypto_positions()
    for c in crypto_positions:
        avail = float(c['quantity_available'])
        if (avail <= 0):
            continue
        key = (c['currency']['code'])
        totalValueOfShares = GetPriceOfCrypto(key, avail)
        temp = Investment(key, avail, totalValueOfShares)
        loot.append(temp)

    return loot
