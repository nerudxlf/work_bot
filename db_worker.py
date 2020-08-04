import sqlite3
import config

def checking_db_connection():
    try:
        connect = sqlite3.connect(config.DB)
        return connect
    except sqlite3.Error:
        return 0
