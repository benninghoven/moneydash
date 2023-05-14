import sqlite3
import datetime
import pytz
from globals import GLOBALS as G


def ExportBankAccounts(data=None):
    if (data is None):
        return False

    conn = sqlite3.connect(G.databasePath)

    conn.execute('''
                 CREATE TABLE IF NOT EXISTS bank_accounts(
                     id TEXT PRIMARY KEY,
                     name TEXT NOT NULL,
                     nickname TEXT NOT NULL,
                     balance REAL
                     );
                 ''')

    for v in data:
        conn.execute('''
                     INSERT OR REPLACE INTO bank_accounts(
                         id,
                         name,
                         nickname,
                         balance)
                     VALUES (?, ?, ?, ?)
                     ''', (
                         v.id,
                         v.name,
                         v.nickname,
                         v.balance,
                         ))

    conn.commit()
    conn.close()


def ExportTransactions(data=None):
    if (data is None):
        return False

    conn = sqlite3.connect(G.databasePath)

    conn.execute('''
                 CREATE TABLE IF NOT EXISTS transactions (
                     transaction_id TEXT PRIMARY KEY,
                     card_nickname TEXT NOT NULL,
                     amount REAL,
                     date text NOT NULL,
                     categories TEXT NOT NULL,
                     name TEXT NOT NULL
                     );
                 ''')

    for v in data:
        conn.execute('''
                     INSERT OR REPLACE INTO transactions(
                         transaction_id,
                         card_nickname,
                         amount,
                         date,
                         categories,
                         name)
                     VALUES (?, ?, ?, ?, ?, ?)
                     ''', (
                         v.id,
                         v.card_nickname,
                         v.amount,
                         v.date,
                         v.categories,
                         v.name,
                         ))

    conn.commit()
    conn.close()


def UpdateLastUpdated():
    conn = sqlite3.connect(G.databasePath)
    conn.execute("CREATE TABLE IF NOT EXISTS last_updated (timestamp TEXT)")

    la_timezone = pytz.timezone('America/Los_Angeles')
    current_time = datetime.datetime.now(la_timezone).strftime('%Y-%m-%d %H:%M:%S')
    print(current_time)

    if conn.execute("SELECT COUNT(*) FROM last_updated").fetchone()[0] == 0:
        conn.execute("INSERT INTO last_updated(timestamp) VALUES (?)", (current_time,))
    else:
        conn.execute("UPDATE last_updated SET timestamp = ?", (current_time,))
    conn.commit()
    conn.close()


def ExportInvestments(data=None):
    if (data is None):
        return False
    conn = sqlite3.connect(G.databasePath)

    conn.execute('''
                 CREATE TABLE IF NOT EXISTS investments(
                     name TEXT PRIMARY KEY,
                     total_shares REAL,
                     total_value REAL
                     );
                 ''')

    for k, inv in data.items():
        conn.execute('''
                     INSERT OR REPLACE INTO investments(
                         name,
                         total_shares,
                         total_value)
                     VALUES (?, ?, ?)
                     ''', (
                         inv.name,
                         inv.total_shares,
                         inv.total_value,
                         ))

    conn.commit()
    conn.close()
