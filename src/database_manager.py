import sqlite3
from globals import GLOBALS as G


def ExportRobinhoodData(data=None):
    print("exporting robinhood data")
    if (data is None):
        return False
    conn = sqlite3.connect(G.databasePath)

    conn.execute('''
                 CREATE TABLE IF NOT EXISTS stonks (
                     name TEXT PRIMARY KEY,
                     ammount_of_shares REAL,
                     total_value REAL
                     );
                 ''')

    for k, v in data.items():
        conn.execute('''
                     INSERT OR REPLACE INTO stonks(
                         name,
                         ammount_of_shares,
                         total_value)
                     VALUES (?, ?, ?)
                     ''', (
                         k,
                         v["ammount_of_shares"],
                         v["total_value"]
                         ))

    conn.commit()
    conn.close()


def ExportAccountData(data=None):
    print("exporting account data")
    if (data is None):
        return False
    conn = sqlite3.connect(G.databasePath)

    conn.execute('''
                 CREATE TABLE IF NOT EXISTS bofa_accounts (
                     id TEXT PRIMARY KEY,
                     name TEXT NOT NULL,
                     nickname TEXT NOT NULL,
                     current_balance REAL
                     );
                 ''')

    for k, v in data.items():
        conn.execute('''
                     INSERT OR REPLACE INTO bofa_accounts (
                         id,
                         name,
                         nickname,
                         current_balance)
                         VALUES (?, ?, ?, ?)
                         ''', (
                             k,
                             v["name"],
                             v["nickname"],
                             v["current_balance"]
                             ))

    conn.commit()
    conn.close()


def ExportBOFATransactions(data=None):
    print("exporting bofa transactions data")
    if (data is None):
        return False
    conn = sqlite3.connect(G.databasePath)

    conn.execute('''
                 CREATE TABLE IF NOT EXISTS bofa_transactions (
                     transaction_id TEXT PRIMARY KEY,
                     account_id TEXT NOT NULL,
                     amount REAL,
                     date text NOT NULL,
                     category_id REAL,
                     name TEXT NOT NULL,
                     payment_channel TEXT NOT NULL
                     );
                 ''')

    for k, v in data.items():
        conn.execute('''
                     INSERT OR REPLACE INTO bofa_transactions (
                         transaction_id,
                         account_id,
                         amount,
                         date,
                         category_id,
                         name,
                         payment_channel)
                         VALUES (?, ?, ?, ?, ?, ?, ?)
                         ''', (
                             k,
                             v["account_id"],
                             v["amount"],
                             v["date"],
                             v["category_id"],
                             v["name"],
                             v["payment_channel"]
                             ))

    conn.commit()
    conn.close()
