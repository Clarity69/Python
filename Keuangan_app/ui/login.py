import customtkinter as ctk
from tkinter import messagebox
from db.user_db import check_login, init_user, tambah_user
from db.transactions_db import init_transaksi, tambah_transaksi
from ui.main_window import MainWindow

class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login - Manajemen Keuangan")
        self.geometry("500x300")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark") # light, dark, system
        ctk.set_default_color_theme("blue")

        self.create_widgets()
        
        self.bind("<Return>", lambda event: self.handle_login())

    def create_widgets(self):
        ctk.CTkLabel(self, text="Username:", font=("Inter", 12, "bold")).pack(pady=(20, 5))
        self.entry_username = ctk.CTkEntry(self, corner_radius=8, width=220)
        self.entry_username.pack()

        ctk.CTkLabel(self, text="Password:", font=("Inter", 12, "bold")).pack(pady=(10, 5))
        self.entry_password = ctk.CTkEntry(self, corner_radius=8, show="*", width=220)
        self.entry_password.pack()

        ctk.CTkButton(
            self,
            text="Login",
            command=self.handle_login,
            fg_color="#4CAF50",
            hover_color="#45A049",
            text_color="white",
            corner_radius=8,
            font=("Poppins", 13, "bold"),
            width=120
        ).pack(pady=20)
        ctk.CTkButton(
            self,
            text="Register",
            command=lambda:RegisterWindow(),
            fg_color="#2196F3",
            hover_color="#0B7DD1",
            text_color="white",
            corner_radius=8,
            font=("Poppins", 13, "bold"),
            width=120
        ).pack()
    def handle_login(self):
        # ctk.set_appearance_mode("dark")
        username = self.entry_username.get()
        password = self.entry_password.get()
        user = check_login(username, password)
        
        #VALIDASI LOGIN
        if not username or not password:
            messagebox.showerror("Gagal", "Username dan password tidak boleh kosong!")
            return
        user = check_login(username, password)
        if user:
            messagebox.showinfo("Sukses", f"Selamat datang, {user[3]}!")
            self.destroy()
            MainWindow(user)
        else:
            messagebox.showerror("Gagal", "Username atau password salah!")

class RegisterWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Register - Manajemen Keuangan")
        self.geometry("400x350")
        ctk.set_appearance_mode("dark")
        
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Username:", font=("Poppins", 12)).pack(pady=(20,5))
        self.entry_username = ctk.CTkEntry(self, corner_radius=8, width=220)
        self.entry_username.pack()

        ctk.CTkLabel(self, text="Password:", font=("Poppins", 12)).pack(pady=(10,5))
        self.entry_password = ctk.CTkEntry(self, corner_radius=8, show="*", width=220)
        self.entry_password.pack()

        ctk.CTkLabel(self, text="Nama:", font=("Poppins", 12)).pack(pady=(10,5))
        self.entry_nama = ctk.CTkEntry(self, corner_radius=8, width=220)
        self.entry_nama.pack()

        ctk.CTkButton(
            self,
            text="Register",
            command=self.handle_register,
            fg_color="#4CAF50",
            hover_color="#45A049",
            text_color="white",
            corner_radius=8,
            font=("Poppins", 13, "bold"),
            width=120
        ).pack(pady=20)

    def handle_register(self):
        from db.user_db import tambah_user  # fungsi yang menambahkan user ke DB

        username = self.entry_username.get()
        password = self.entry_password.get()
        nama = self.entry_nama.get()
        #VALIDASI INPUT
        if not username or not password or not nama:
            messagebox.showerror("Gagal", "Semua field harus diisi!")
            return
        
        if tambah_user(username, password, nama):
            messagebox.showinfo("Sukses", "User berhasil didaftarkan!")
            self.destroy()
        else:
            messagebox.showerror("Gagal", "Username sudah digunakan atau input tidak valid.")
