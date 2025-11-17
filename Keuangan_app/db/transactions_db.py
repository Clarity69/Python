import sqlite3
from tkinter import messagebox
from db.connection import connect_db

def init_transaksi():
    conn= connect_db()
    cur= conn.cursor()
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS transactions(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    kategori_id INTEGER NOT NULL,
                    tipe TEXT CHECK(TIPE IN ('Pemasukan', 'Pengeluaran')) NOT NULL,
                    jumlah REAL NOT NULL,
                    tanggal timESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(user_id) REFERENCES users(id) on DELETE CASCADE,
                    FOREIGN KEY(kategori_id) REFERENCES kategori(id) on DELETE CASCADE
                )""")
    conn.commit()
    conn.close()

def tambah_transaksi(user_id, tipe, jumlah):
    #VALIDASI DATA
    if tipe not in ['Pemasukan', 'Pengeluaran']:
        messagebox.showerror("Error", "Tipe transaksi harus 'Pemasukan' atau 'Pengeluaran'")
        return False
    if jumlah <= 0:
        messagebox.showerror("Error", "Jumlah transaksi harus lebih dari 0")
        return False
    # if not isinstance(user_id, int) or not isinstance(kategori_id, int):
    #     messagebox.showerror("Error", "User ID dan Kategori ID harus berupa angka")
    #     return False
    
    conn=connect_db()
    cur=conn.cursor()
    try:
        cur.execute("INSERT INTO transactions (user_id, kategori_id, tipe, jumlah) VALUES (?, ?, ?, ?)",
                    (user_id, tipe, jumlah))
        conn.commit()
        messagebox.showinfo("Sukses", "Transaksi berhasil ditambahkan")
        return True
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Gagal menambahkan transaksi: {e}") 
        return False
    finally:
        conn.close()

