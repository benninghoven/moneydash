import sqlite3
import datetime
from globals import GLOBALS as G


def ExportRobinhoodData(data=None):
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
    if (data is None):
        return False
    conn = sqlite3.connect(G.databasePath)

    conn.execute('''
                 CREATE TABLE IF NOT EXISTS bofa_transactions (
                     transaction_id TEXT PRIMARY KEY,
                     account_id TEXT NOT NULL,
                     amount REAL,
                     date text NOT NULL,
                     categories TEXT NOT NULL,
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
                         categories,
                         name,
                         payment_channel)
                     VALUES (?, ?, ?, ?, ?, ?, ?)
                     ''', (
                         k,
                         v["account_id"],
                         v["amount"],
                         v["date"],
                         v["categories"],
                         v["name"],
                         v["payment_channel"]
                         ))

    conn.commit()
    conn.close()


def UpdateLastUpdated():
    conn = sqlite3.connect(G.databasePath)
    conn.execute("CREATE TABLE IF NOT EXISTS last_updated (timestamp TEXT)")
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if conn.execute("SELECT COUNT(*) FROM last_updated").fetchone()[0] == 0:
        conn.execute("INSERT INTO last_updated(timestamp) VALUES (?)", (current_time,))
    else:
        conn.execute("UPDATE last_updated SET timestamp = ?", (current_time,))
    conn.commit()
    conn.close()


def ExportCoinbaseData(data=None):
    if (data is None):
        return False
    conn = sqlite3.connect(G.databasePath)

    conn.execute('''
                 CREATE TABLE IF NOT EXISTS coinbase_coins(
                     name TEXT PRIMARY KEY,
                     amount_of_coins REAL,
                     total_value REAL
                     );
                 ''')

    for k, v in data.items():
        conn.execute('''
                     INSERT OR REPLACE INTO coinbase_coins(
                         name,
                         amount_of_coins,
                         total_value)
                     VALUES (?, ?, ?)
                     ''', (
                         k,
                         v["amount_of_coins"],
                         v["total_value"]
                         ))

    conn.commit()
    conn.close()
