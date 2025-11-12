import tkinter as tk
from tkinter import ttk, messagebox
from db.user_db import check_login, init_user
import sqlite3

init_user()
# Setup Database
DB_FILE = "keuangan.db"

def connect_db():
    try:
        conn: sqlite3.Connection = sqlite3.connect(DB_FILE)
        return conn
    except sqlite3.Error as e:
        print(f"Gagal Connect ke Database{e}")
        return None
class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login - Manajemen Keuangan")
        self.geometry("300x200")
        self.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Username:").pack(pady=(20, 5))
        self.entry_username = ttk.Entry(self)
        self.entry_username.pack()

        ttk.Label(self, text="Password:").pack(pady=(10, 5))
        self.entry_password = ttk.Entry(self, show="*")
        self.entry_password.pack()

        ttk.Button(self, text="Login", command=self.handle_login).pack(pady=20)

    def handle_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        user = check_login(username, password)

        if user:
            messagebox.showinfo("Sukses", f"Selamat datang, {user[3]}!")
            self.destroy()  # Tutup jendela login
            self.open_main_window()
        else:
            messagebox.showerror("Gagal", "Username atau password salah!")

    def open_main_window(self):
        MainWindow()


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Manajemen Keuangan - Dashboard")
        self.geometry("600x400")
        self.create_widgets()
        self.mainloop()

    def create_widgets(self):
        ttk.Label(self, text="Dashboard Keuangan", font=("Arial", 16)).pack(pady=20)
        ttk.Button(self, text="Tambah Transaksi", command=self.dummy_action).pack(pady=10)
        ttk.Button(self, text="Lihat Transaksi", command=self.dummy_action).pack(pady=10)

    def dummy_action(self):
        messagebox.showinfo("Info", "Fitur ini belum diimplementasikan")


if __name__ == "__main__":
    login = LoginWindow()
    login.mainloop()