from robinhood_manager import FetchRobinhoodData
from plaid_manager import FetchPlaidData
from plaid_manager import FetchBOFATransactions

from database_manager import ExportRobinhoodData
from database_manager import ExportAccountData
from database_manager import ExportBOFATransactions

robinData = FetchRobinhoodData()
plaidData = FetchPlaidData()
bofaTransactions = FetchBOFATransactions()

ExportRobinhoodData(robinData)
ExportAccountData(plaidData)
ExportBOFATransactions(bofaTransactions)

print("finished running main")
