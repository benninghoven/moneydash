from robinhood_manager import FetchRobinhoodData
from plaid_manager import FetchPlaidData
from plaid_manager import FetchBOFATransactions
from coinbase_manager import FetchCoinbaseData

from database_manager import ExportRobinhoodData
from database_manager import ExportAccountData
from database_manager import ExportBOFATransactions
from database_manager import ExportCoinbaseData
from database_manager import UpdateLastUpdated

robinData = FetchRobinhoodData()
plaidData = FetchPlaidData()
coinbaseData = FetchCoinbaseData()
bofaTransactions = FetchBOFATransactions()

ExportRobinhoodData(robinData)
ExportAccountData(plaidData)
ExportBOFATransactions(bofaTransactions)
ExportCoinbaseData(coinbaseData)

UpdateLastUpdated()

print("finished running main")
