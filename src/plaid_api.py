import plaid
from plaid.api import plaid_api
from plaid.model.accounts_get_request import AccountsGetRequest
from plaid.model.transactions_get_request import TransactionsGetRequest
import datetime

from globals import GLOBALS as G
from load_credentials import LoadCredentials
from classes.bankaccount import BankAccount
from classes.transaction import Transaction


def GetPlaidClient():

    credentials = LoadCredentials(G.credentialsPath)
    plaidCredentials = credentials["plaid"]

    client_id = plaidCredentials["client_id"]
    secret = plaidCredentials["secret"]

    configuration = plaid.Configuration(
            host=plaid.Environment.Development,
            api_key={
                'clientId': client_id,
                'secret': secret,
                }
            )
    api_client = plaid.ApiClient(configuration)

    return plaid_api.PlaidApi(api_client)


def GetAccessToken():

    credentials = LoadCredentials(G.credentialsPath)
    plaidCredentials = credentials["plaid"]

    return plaidCredentials["access_token"]


def FetchBankAccounts():

    loot = []

    access_token = GetAccessToken()
    client = GetPlaidClient()

    request = AccountsGetRequest(access_token=access_token)
    response = client.accounts_get(request)
    accounts = response['accounts']

    for account in accounts:
        if (str(account.type) == "credit"):
            account.balances.current *= -1

        id = account.account_id
        name = account.official_name
        nickname = account.name
        balance = account.balances.current

        temp = BankAccount(id, name, nickname, balance)

        loot.append(temp)

    return loot


def FetchTransactions():

    loot = []

    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=30)

    access_token = GetAccessToken()
    client = GetPlaidClient()

    request = TransactionsGetRequest(
            access_token=access_token,
            start_date=start_date,
            end_date=end_date,
            )

    response = client.transactions_get(request)

    transactions = response['transactions']

    for transaction in transactions:

        pending = transaction["pending"]
        if pending:
            continue

        transaction_id = transaction["transaction_id"]
        account_id = transaction["account_id"]
        amount = transaction["amount"]
        date = transaction["date"]
        category = transaction["category"]
        name = transaction["name"]

        category = sorted(category)
        categories = ', '.join(category)

        temp = Transaction(
                transaction_id,
                account_id,
                amount,
                date,
                categories,
                name
                )

        loot.append(temp)

    return loot
