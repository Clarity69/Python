import customtkinter as ctk
from tkinter import messagebox
from db.user_db import check_login, init_user
from db.transactions_db import  tambah_transaksi, init_transaksi

class MainWindow(ctk.CTk):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.title("Manajemen Keuangan")
        self.geometry("600x400")
        ctk.set_appearance_mode("dark") # light, dark, system

        self.create_widgets()
        self.mainloop()

    def handle_tambah_transaksi(self):
        TambahTransaksiWindow(self.user[0])
        try:
            tambah_transaksi()
            messagebox.showinfo("Sukses", "Transaksi berhasil ditambahkan.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menambahkan transaksi: {e}")
    
    def create_widgets(self):
        ctk.CTkLabel(self, text="Dashboard Keuangan", font=("Inter", 16, "bold")).pack(pady=20)

        ctk.CTkButton(
            self,
            text="Tambah Transaksi",
            command=self.handle_tambah_transaksi,
            fg_color="#3DC2EC",
            hover_color="#25A7C7",
            text_color="black",
            corner_radius=8,
            font=("Poppins", 13, "bold"),
            width=160
        ).pack(side="top", padx=10, pady=10)

        ctk.CTkButton(
            self,
            text="Lihat Transaksi",
            command=self.dummy_action,
            fg_color="#AAAAAA",
            text_color="black",
            corner_radius=8,
            font=("Poppins", 13, "bold"),
            width=160
        ).pack(side="top", padx=10, pady=10)

    def dummy_action(self):
        messagebox.showinfo("Info", "Fitur ini belum diimplementasikan.")
        
class TambahTransaksiWindow(ctk.CTk):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.title("Tambah Transaksi")
        self.geometry("400x375")
        ctk.set_appearance_mode("dark") # light, dark, system

        self.create_widgets()
        self.mainloop()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Tambah Transaksi", font=("Poppins", 14, "bold")).pack(pady=20)
        # Tambahkan widget form di sini
        # --- INPUT NAMA ---
        ctk.CTkLabel(self, text="Nama Transaksi:", font=("Inter", 12)).pack(pady=5)
        self.nama_entry = ctk.CTkEntry(self, placeholder_text="Contoh: Makan siang")
        self.nama_entry.pack(pady=5)

        # --- INPUT JUMLAH ---
        ctk.CTkLabel(self, text="Jumlah (Rp):", font=("Inter", 12)).pack(pady=5)
        self.jumlah_entry = ctk.CTkEntry(self, placeholder_text="Contoh: 25000")
        self.jumlah_entry.pack(pady=5)
        
        # ctk.CTkLabel(self, text="Kategori ID:", font=("Inter", 12)).pack(pady=5)
        # self.kategori_id_entry = ctk.CTkEntry(self, placeholder_text="Masukkan ID kategori")
        # self.kategori_id_entry.pack(pady=5)

        # --- INPUT KATEGORI ---
        ctk.CTkLabel(self, text="Tipe Transaksi:").pack(pady=(5,0))
        self.tipe_var = ctk.StringVar(value="Pemasukan")
        ctk.CTkOptionMenu(self, variable=self.tipe_var, 
                          values=["Pemasukan", "Pengeluaran"]).pack(pady=(0,10))
        # ctk.CTkLabel(self, text="Kategori ID:", font=("Inter", 12)).pack(pady=5)
        # self.kategori_id_entry = ctk.CTkEntry(self, placeholder_text="Contoh: 1")
        # self.kategori_id_entry.pack(pady=5)
        
        ctk.CTkButton(
            self,
            text="Simpan",
            command=self.simpan_data,
            fg_color="#4CAF50",
            hover_color="#45A049",
            text_color="white",
            corner_radius=8,
            font=("Poppins", 13, "bold"),
            width=120
        ).pack(pady=20)
        
    def simpan_data(self):
        user_id = self.user_id
        # kategori_id = self.kategori_id_entry.get()
        jumlah = float(self.jumlah_entry.get())
        tipe = self.tipe_var.get()
        nama = self.nama_entry.get()
        try:
            # kategori_id = int(self.kategori_id_entry.get())
            tipe = self.tipe_option.get()
            jumlah = float(self.jumlah_entry.get())
            user_id = self.user_id

            # panggil fungsi database
            tambah_transaksi(self.user_id, tipe, jumlah)

            messagebox.showinfo("Sukses", "Transaksi berhasil ditambahkan!")
            self.destroy()

        except ValueError:
            messagebox.showerror("Error", "Pastikan kategori dan jumlah berupa angka.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menambahkan transaksi: {e}")

