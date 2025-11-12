import sqlite3
from tkinter import messagebox

DB_FILE = "keuangan.db"

def connect_db():
    try:
        conn: sqlite3.Connection = sqlite3.connect(DB_FILE)
        return conn
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Gagal Connect ke Database: {e}")
        return None

def init_user():
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    nama TEXT NOT NULL
                )""")
#user default atau admin
    cur.execute("INSERT OR IGNORE INTO users (username, password, nama) VALUES (?, ?, ?)", 
                ("admin", "admin123", "Administrator"))
    messagebox.showinfo("Info", "User default: admin/admin123")
    conn.commit()
    conn.close()
    
def check_login(username, password):
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cur.fetchone()
    
    conn.close()
    return user

def handle_login(username, password):
    username=username.get()
    password=password.get()
    user=check_login(username, password)
    if user:
        messagebox.showinfo("Sukses", f"Selamat datang, {user[3]}!")
    else:
        messagebox.showerror("Gagal", "Username atau password salah!")