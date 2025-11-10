import tkinter as tk
from tkinter import ttk
import sqlite3

# Setup Database
DB_FILE = "keuangan.db"

def connect_db():
    try:
        conn: sqlite3.Connection = sqlite3.connect(DB_FILE)
        return conn
    except sqlite3.Error as e:
        print(f"Gagal Connect ke Database{e}")
        return None