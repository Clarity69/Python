import sqlite3

DB_FILE = "keuangan.db"

def connect_db():
    try:
        return sqlite3.connect(DB_FILE)
    except sqlite3.Error as e:
        print(f"Gagal connect ke database: {e}")
        return None
