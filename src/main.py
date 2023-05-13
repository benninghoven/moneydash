from coinbase_api import FetchCoinbaseInvestments
from robinhood_api import FetchRobinhoodInvestments
from plaid_api import FetchBankAccounts
from plaid_api import FetchTransactions

from database_manager import ExportInvestments
from database_manager import ExportBankAccounts
from database_manager import ExportTransactions
from database_manager import UpdateLastUpdated


coinbaseInvestments = FetchCoinbaseInvestments()
robinhoodInvestments = FetchRobinhoodInvestments()

investmentsList = coinbaseInvestments + robinhoodInvestments
investmentsDict = dict()

for inv in investmentsList:
    if inv.name not in investmentsDict:
        investmentsDict[inv.name] = inv
    else:
        investmentsDict[inv.name] = investmentsDict[inv.name] + inv
ExportInvestments(investmentsDict)


bankAccounts = FetchBankAccounts()
ExportBankAccounts(bankAccounts)


transactions = FetchTransactions()
account_id_to_nickname_dict = dict()
for account in bankAccounts:
    account_id_to_nickname_dict[account.id] = account.nickname

for t in transactions:
    t.card_nickname = account_id_to_nickname_dict[t.account_id]

ExportTransactions(transactions)
UpdateLastUpdated()
