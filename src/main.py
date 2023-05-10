from robinhood_manager import FetchRobinhoodData
from plaid_manager import FetchPlaidData
from plaid_manager import FetchBOFATransactions

from database_manager import ExportRobinhoodData
from database_manager import ExportAccountData
from database_manager import ExportBOFATransactions


robin_data = FetchRobinhoodData()
plaid_Data = FetchPlaidData()
bofaTransactions = FetchBOFATransactions()

ExportRobinhoodData(robin_data)
ExportAccountData(plaid_Data)
ExportBOFATransactions(bofaTransactions)


print("finished running main")
