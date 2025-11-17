import sqlite3
from tkinter import messagebox
from db.connection import connect_db

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
#cek table kosong
    cur.execute("SELECT COUNT(*) FROM users")
    count = cur.fetchone()[0]
    if count == 0:
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

def tambah_user(username, password, nama):
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, password, nama) VALUES (?, ?, ?)", 
                    (username, password, nama))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username sudah digunakan.")
        return False
    finally:
        conn.close()