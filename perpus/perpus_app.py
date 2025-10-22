import tkinter as tk
from tkinter import ttk, messagebox
import re
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# -------------------- CONFIG --------------------
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'perpustakaan_db'
}

# -------------------- DB HELPERS --------------------
def get_db_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        raise e


def safe_query(query, params=(), fetch=False, many=False):
    """Execute a query, return fetched rows if fetch=True."""
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor(dictionary=True)
        if many:
            cur.executemany(query, params)
        else:
            cur.execute(query, params)
        if fetch:
            rows = cur.fetchall()
            return rows
        else:
            conn.commit()
            return None
    except Error as e:
        raise e
    finally:
        if conn:
            conn.close()


# -------------------- VALIDATION HELPERS --------------------
def is_valid_email(email):
    if not email:
        return True  # optional field
    regex = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return re.match(regex, email) is not None


def is_positive_int(value):
    try:
        return int(value) >= 0
    except Exception:
        return False


# -------------------- GUI CLASSES --------------------
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Login - Perpustakaan')
        self.root.geometry('380x260')
        self.root.resizable(False, False)

        frame = ttk.Frame(root, padding=20)
        frame.pack(expand=True, fill='both')

        ttk.Label(frame, text='Username:').grid(row=0, column=0, sticky='w')
        self.username_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.username_var).grid(row=0, column=1, pady=5)

        ttk.Label(frame, text='Password:').grid(row=1, column=0, sticky='w')
        self.password_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.password_var, show='*').grid(row=1, column=1, pady=5)

        login_btn = ttk.Button(frame, text='Login', command=self.login)
        login_btn.grid(row=2, column=0, columnspan=2, pady=10)

        register_btn = ttk.Button(frame, text='Register', command=self.open_register)
        register_btn.grid(row=3, column=0, columnspan=2)

        self.status_label = ttk.Label(frame, text='')
        self.status_label.grid(row=4, column=0, columnspan=2)

        # center
        try:
            self.root.eval('tk::PlaceWindow %s center' % self.root.winfo_toplevel())
        except Exception:
            pass

    def login(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()

        if not username or not password:
            messagebox.showwarning('Input Error', 'Username dan password tidak boleh kosong.')
            return

        try:
            rows = safe_query('SELECT id, username, role FROM users WHERE username=%s AND password=%s',
                              (username, password), fetch=True)
            if not rows:
                messagebox.showerror('Login Gagal', 'Username atau password salah.')
                return

            user = rows[0]
            self.root.destroy()
            app = tk.Tk()
            MainApp(app, user)
            app.mainloop()

        except Error as e:
            messagebox.showerror('Database Error', f'Gagal koneksi/kueri ke database.\n{e}')

    def open_register(self):
        RegisterWindow(self.root)


class RegisterWindow:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title('Register Akun Baru')
        self.top.geometry('420x320')
        self.top.resizable(False, False)

        frame = ttk.Frame(self.top, padding=20)
        frame.pack(expand=True, fill='both')

        ttk.Label(frame, text='Username:').grid(row=0, column=0, sticky='w')
        self.username_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.username_var).grid(row=0, column=1, pady=5)

        ttk.Label(frame, text='Password:').grid(row=1, column=0, sticky='w')
        self.password_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.password_var, show='*').grid(row=1, column=1, pady=5)

        ttk.Label(frame, text='Konfirmasi Password:').grid(row=2, column=0, sticky='w')
        self.password2_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.password2_var, show='*').grid(row=2, column=1, pady=5)

        ttk.Label(frame, text='Role:').grid(row=3, column=0, sticky='w')
        self.role_var = tk.StringVar(value='petugas')
        ttk.Combobox(frame, textvariable=self.role_var, values=['admin', 'petugas'], state='readonly').grid(row=3, column=1, pady=5)

        ttk.Button(frame, text='Register', command=self.register).grid(row=4, column=0, columnspan=2, pady=10)

    def register(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        password2 = self.password2_var.get().strip()
        role = self.role_var.get().strip()

        if not username or not password:
            messagebox.showwarning('Input Error', 'Username dan password wajib diisi.')
            return
        if password != password2:
            messagebox.showwarning('Input Error', 'Konfirmasi password tidak cocok.')
            return
        try:
            rows = safe_query('SELECT id FROM users WHERE username=%s', (username,), fetch=True)
            if rows:
                messagebox.showerror('Error', 'Username sudah digunakan.')
                return
            safe_query('INSERT INTO users (username, password, role) VALUES (%s,%s,%s)', (username, password, role))
            messagebox.showinfo('Sukses', 'Registrasi berhasil. Silakan login.')
            self.top.destroy()
        except Error as e:
            messagebox.showerror('Database Error', f'Gagal register.\n{e}')


class MainApp:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.root.title('Sistem Manajemen Perpustakaan')
        self.root.geometry('900x600')

        # menu/top frame
        top_frame = ttk.Frame(root, padding=10)
        top_frame.pack(side='top', fill='x')

        welcome = ttk.Label(top_frame, text=f"Welcome, {user['username']} ({user['role']})", font=('Segoe UI', 11))
        welcome.pack(side='left')

        logout_btn = ttk.Button(top_frame, text='Logout', command=self.logout)
        logout_btn.pack(side='right')

        # left navigation
        nav_frame = ttk.Frame(root, padding=(10, 10))
        nav_frame.pack(side='left', fill='y')

        btn_dashboard = ttk.Button(nav_frame, text='Dashboard', width=20, command=self.show_dashboard)
        btn_buku = ttk.Button(nav_frame, text='Manajemen Buku', width=20, command=self.show_buku)
        btn_anggota = ttk.Button(nav_frame, text='Manajemen Anggota', width=20, command=self.show_anggota)

        btn_dashboard.pack(pady=5)
        btn_buku.pack(pady=5)
        btn_anggota.pack(pady=5)

        # main content area
        self.content = ttk.Frame(root, padding=10)
        self.content.pack(side='left', fill='both', expand=True)

        # initialize frames
        self.frames = {}
        for F in (DashboardFrame, BukuFrame, AnggotaFrame):
            frame = F(self.content, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_dashboard()

    def show_dashboard(self):
        frame = self.frames['DashboardFrame']
        frame.refresh()
        frame.tkraise()

    def show_buku(self):
        frame = self.frames['BukuFrame']
        frame.refresh()
        frame.tkraise()

    def show_anggota(self):
        frame = self.frames['AnggotaFrame']
        frame.refresh()
        frame.tkraise()

    def logout(self):
        confirm = messagebox.askyesno('Logout', 'Apakah Anda yakin ingin logout?')
        if confirm:
            self.root.destroy()
            root = tk.Tk()
            LoginWindow(root)
            root.mainloop()


class DashboardFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text='Dashboard', font=('Segoe UI', 14)).pack(anchor='w')

        stats_frame = ttk.Frame(self, padding=10)
        stats_frame.pack(fill='x')

        self.label_total_buku = ttk.Label(stats_frame, text='Total Buku: -', font=('Segoe UI', 11))
        self.label_total_anggota = ttk.Label(stats_frame, text='Total Anggota: -', font=('Segoe UI', 11))

        self.label_total_buku.pack(anchor='w', pady=5)
        self.label_total_anggota.pack(anchor='w', pady=5)

    def refresh(self):
        try:
            rows = safe_query('SELECT COUNT(*) AS cnt FROM buku', fetch=True)
            total_buku = rows[0]['cnt'] if rows else 0
            rows2 = safe_query('SELECT COUNT(*) AS cnt FROM anggota', fetch=True)
            total_anggota = rows2[0]['cnt'] if rows2 else 0
            self.label_total_buku.config(text=f'Total Buku: {total_buku}')
            self.label_total_anggota.config(text=f'Total Anggota: {total_anggota}')
        except Error as e:
            messagebox.showerror('Database Error', f'Gagal mengambil statistik.\n{e}')


class BukuFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        header = ttk.Frame(self)
        header.pack(fill='x')
        ttk.Label(header, text='Manajemen Buku', font=('Segoe UI', 14)).pack(side='left')

        form = ttk.LabelFrame(self, text='Form Buku', padding=10)
        form.pack(fill='x', pady=10)

        # fields
        self.kode_var = tk.StringVar()
        self.judul_var = tk.StringVar()
        self.pengarang_var = tk.StringVar()
        self.penerbit_var = tk.StringVar()
        self.tahun_var = tk.StringVar()
        self.stok_var = tk.StringVar()
        
        labels = ['Kode Buku', 'Judul', 'Pengarang', 'Penerbit', 'Tahun Terbit', 'Stok']
        vars = [self.kode_var, self.judul_var, self.pengarang_var, self.penerbit_var, self.tahun_var, self.stok_var]

        for i, (lab, var) in enumerate(zip(labels, vars)):
            ttk.Label(form, text=lab+':').grid(row=i, column=0, sticky='w', pady=2)
            ttk.Entry(form, textvariable=var, width=40).grid(row=i, column=1, pady=2, sticky='w')

        btn_frame = ttk.Frame(form)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=8)
        ttk.Button(btn_frame, text='Tambah', command=self.add_buku).pack(side='left', padx=4)
        ttk.Button(btn_frame, text='Update', command=self.update_buku).pack(side='left', padx=4)
        ttk.Button(btn_frame, text='Hapus', command=self.delete_buku).pack(side='left', padx=4)
        ttk.Button(btn_frame, text='Clear', command=self.clear_form).pack(side='left', padx=4)

        # search
        search_frame = ttk.Frame(self)
        search_frame.pack(fill='x', pady=5)
        ttk.Label(search_frame, text='Cari (judul / pengarang):').pack(side='left')
        self.search_var = tk.StringVar()
        ttk.Entry(search_frame, textvariable=self.search_var, width=30).pack(side='left', padx=5)
        ttk.Button(search_frame, text='Search', command=self.search_buku).pack(side='left')
        ttk.Button(search_frame, text='Refresh', command=self.refresh).pack(side='left', padx=4)

        # treeview
        cols = ('kode_buku', 'judul', 'pengarang', 'penerbit', 'tahun_terbit', 'stok')
        self.tree = ttk.Treeview(self, columns=cols, show='headings', selectmode='browse')
        for c in cols:
            self.tree.heading(c, text=c.replace('_', ' ').title())
            self.tree.column(c, anchor='w')
        self.tree.pack(fill='both', expand=True, pady=5)
        self.tree.bind('<<TreeviewSelect>>', self.on_select)

        self.refresh()

    def refresh(self):
        try:
            for r in self.tree.get_children():
                self.tree.delete(r)
            rows = safe_query('SELECT kode_buku, judul, pengarang, penerbit, tahun_terbit, stok FROM buku ORDER BY created_at DESC', fetch=True)
            for row in rows:
                self.tree.insert('', 'end', values=(row['kode_buku'], row['judul'], row['pengarang'], row['penerbit'], row['tahun_terbit'], row['stok']))
        except Error as e:
            messagebox.showerror('Database Error', f'Gagal mengambil data buku.\n{e}')

    def clear_form(self):
        self.kode_var.set('')
        self.judul_var.set('')
        self.pengarang_var.set('')
        self.penerbit_var.set('')
        self.tahun_var.set('')
        self.stok_var.set('')

    def on_select(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        vals = self.tree.item(sel[0])['values']
        self.kode_var.set(vals[0])
        self.judul_var.set(vals[1])
        self.pengarang_var.set(vals[2])
        self.penerbit_var.set(vals[3])
        self.tahun_var.set(vals[4])
        self.stok_var.set(vals[5])

    def add_buku(self):
        kode = self.kode_var.get().strip()
        judul = self.judul_var.get().strip()
        pengarang = self.pengarang_var.get().strip()
        penerbit = self.penerbit_var.get().strip()
        tahun = self.tahun_var.get().strip()
        stok = self.stok_var.get().strip()

        if not kode or not judul or not pengarang or not penerbit or not tahun:
            messagebox.showwarning('Input Error', 'Semua field kecuali stok harus diisi.')
            return
        if not tahun.isdigit():
            messagebox.showwarning('Input Error', 'Tahun terbit harus angka.')
            return
        if not is_positive_int(stok):
            messagebox.showwarning('Input Error', 'Stok harus angka >= 0.')
            return

        try:
            # check unique kode
            rows = safe_query('SELECT id FROM buku WHERE kode_buku=%s', (kode,), fetch=True)
            if rows:
                messagebox.showerror('Duplicate', 'Kode buku sudah terdaftar.')
                return

            safe_query('INSERT INTO buku (kode_buku, judul, pengarang, penerbit, tahun_terbit, stok) VALUES (%s,%s,%s,%s,%s,%s)',
                       (kode, judul, pengarang, penerbit, int(tahun), int(stok) if stok!='' else 0))
            messagebox.showinfo('Sukses', 'Buku berhasil ditambahkan.')
            self.refresh()
            self.clear_form()
        except Error as e:
            messagebox.showerror('Database Error', f'Gagal menambah buku.\n{e}')

    def update_buku(self):
        kode = self.kode_var.get().strip()
        if not kode:
            messagebox.showwarning('Input Error', 'Pilih buku untuk diupdate (kode tidak boleh kosong).')
            return
        judul = self.judul_var.get().strip()
        pengarang = self.pengarang_var.get().strip()
        penerbit = self.penerbit_var.get().strip()
        tahun = self.tahun_var.get().strip()
        stok = self.stok_var.get().strip()

        if not judul or not pengarang or not penerbit or not tahun:
            messagebox.showwarning('Input Error', 'Semua field kecuali stok harus diisi.')
            return
        if not tahun.isdigit():
            messagebox.showwarning('Input Error', 'Tahun terbit harus angka.')
            return
        if not is_positive_int(stok):
            messagebox.showwarning('Input Error', 'Stok harus angka >= 0.')
            return

        try:
            safe_query('UPDATE buku SET judul=%s, pengarang=%s, penerbit=%s, tahun_terbit=%s, stok=%s WHERE kode_buku=%s',
                       (judul, pengarang, penerbit, int(tahun), int(stok) if stok!='' else 0, kode))
            messagebox.showinfo('Sukses', 'Buku berhasil diupdate.')
            self.refresh()
            self.clear_form()
        except Error as e:
            messagebox.showerror('Database Error', f'Gagal update buku.\n{e}')

    def delete_buku(self):
        kode = self.kode_var.get().strip()
        if not kode:
            messagebox.showwarning('Input Error', 'Pilih buku untuk dihapus.')
            return
        confirm = messagebox.askyesno('Konfirmasi', f'Yakin ingin menghapus buku dengan kode {kode}?')
        if not confirm:
            return
        try:
            safe_query('DELETE FROM buku WHERE kode_buku=%s', (kode,))
            messagebox.showinfo('Sukses', 'Buku berhasil dihapus.')
            self.refresh()
            self.clear_form()
        except Error as e:
            messagebox.showerror('Database Error', f'Gagal hapus buku.\n{e}')

    def search_buku(self):
        q = self.search_var.get().strip()
        try:
            for r in self.tree.get_children():
                self.tree.delete(r)
            if not q:
                self.refresh()
                return
            like = f"%{q}%"
            rows = safe_query('SELECT kode_buku, judul, pengarang, penerbit, tahun_terbit, stok FROM buku WHERE judul LIKE %s OR pengarang LIKE %s', (like, like), fetch=True)
            for row in rows:
                self.tree.insert('', 'end', values=(row['kode_buku'], row['judul'], row['pengarang'], row['penerbit'], row['tahun_terbit'], row['stok']))
        except Error as e:
            messagebox.showerror('Database Error', f'Gagal mencari buku.\n{e}')


class AnggotaFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        header = ttk.Frame(self)
        header.pack(fill='x')
        ttk.Label(header, text='Manajemen Anggota', font=('Segoe UI', 14)).pack(side='left')

        form = ttk.LabelFrame(self, text='Form Anggota', padding=10)
        form.pack(fill='x', pady=10)

        self.kode_var = tk.StringVar()
        self.nama_var = tk.StringVar()
        self.alamat_var = tk.StringVar()
        self.telepon_var = tk.StringVar()
        self.email_var = tk.StringVar()

        labels = ['Kode Anggota', 'Nama', 'Alamat', 'Telepon', 'Email']
        vars = [self.kode_var, self.nama_var, self.alamat_var, self.telepon_var, self.email_var]

        for i, (lab, var) in enumerate(zip(labels, vars)):
            ttk.Label(form, text=lab+':').grid(row=i, column=0, sticky='w', pady=2)
            ttk.Entry(form, textvariable=var, width=50).grid(row=i, column=1, pady=2, sticky='w')

        btn_frame = ttk.Frame(form)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=8)
        ttk.Button(btn_frame, text='Tambah', command=self.add_anggota).pack(side='left', padx=4)
        ttk.Button(btn_frame, text='Update', command=self.update_anggota).pack(side='left', padx=4)
        ttk.Button(btn_frame, text='Hapus', command=self.delete_anggota).pack(side='left', padx=4)
        ttk.Button(btn_frame, text='Clear', command=self.clear_form).pack(side='left', padx=4)

        # treeview
        cols = ('kode_anggota', 'nama', 'alamat', 'telepon', 'email')
        self.tree = ttk.Treeview(self, columns=cols, show='headings', selectmode='browse')
        for c in cols:
            self.tree.heading(c, text=c.replace('_', ' ').title())
            self.tree.column(c, anchor='w')
        self.tree.pack(fill='both', expand=True, pady=5)
        self.tree.bind('<<TreeviewSelect>>', self.on_select)

        self.refresh()

    def refresh(self):
        try:
            for r in self.tree.get_children():
                self.tree.delete(r)
            rows = safe_query('SELECT kode_anggota, nama, alamat, telepon, email FROM anggota ORDER BY created_at DESC', fetch=True)
            for row in rows:
                self.tree.insert('', 'end', values=(row['kode_anggota'], row['nama'], row['alamat'], row['telepon'], row['email']))
        except Error as e:
            messagebox.showerror('Database Error', f'Gagal mengambil data anggota.\n{e}')

    def clear_form(self):
        self.kode_var.set('')
        self.nama_var.set('')
        self.alamat_var.set('')
        self.telepon_var.set('')
        self.email_var.set('')

    def on_select(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        vals = self.tree.item(sel[0])['values']
        self.kode_var.set(vals[0])
        self.nama_var.set(vals[1])
        self.alamat_var.set(vals[2])
        self.telepon_var.set(vals[3])
        self.email_var.set(vals[4])

    def add_anggota(self):
        kode = self.kode_var.get().strip()
        nama = self.nama_var.get().strip()
        alamat = self.alamat_var.get().strip()
        telepon = self.telepon_var.get().strip()
        email = self.email_var.get().strip()

        if not kode or not nama or not alamat or not telepon:
            messagebox.showwarning('Input Error', 'Kode, Nama, Alamat, dan Telepon harus diisi.')
            return
        if not telepon.isdigit():
            messagebox.showwarning('Input Error', 'Telepon harus berisi angka saja.')
            return
        if not is_valid_email(email):
            messagebox.showwarning('Input Error', 'Format email tidak valid.')
            return

        try:
            rows = safe_query('SELECT id FROM anggota WHERE kode_anggota=%s', (kode,), fetch=True)
            if rows:
                messagebox.showerror('Duplicate', 'Kode anggota sudah terdaftar.')
                return
            safe_query('INSERT INTO anggota (kode_anggota, nama, alamat, telepon, email) VALUES (%s,%s,%s,%s,%s)',
                       (kode, nama, alamat, telepon, email if email else None))
            messagebox.showinfo('Sukses', 'Anggota berhasil ditambahkan.')
            self.refresh()
            self.clear_form()
        except Error as e:
            messagebox.showerror('Database Error', f'Gagal menambah anggota.\n{e}')

    def update_anggota(self):
        kode = self.kode_var.get().strip()
        if not kode:
            messagebox.showwarning('Input Error', 'Pilih anggota untuk diupdate (kode tidak boleh kosong).')
            return
        nama = self.nama_var.get().strip()
        alamat = self.alamat_var.get().strip()
        telepon = self.telepon_var.get().strip()
        email = self.email_var.get().strip()

        if not nama or not alamat or not telepon:
            messagebox.showwarning('Input Error', 'Nama, Alamat, dan Telepon harus diisi.')
            return
        if not telepon.isdigit():
            messagebox.showwarning('Input Error', 'Telepon harus berisi angka saja.')
            return
        if not is_valid_email(email):
            messagebox.showwarning('Input Error', 'Format email tidak valid.')
            return

        try:
            safe_query('UPDATE anggota SET nama=%s, alamat=%s, telepon=%s, email=%s WHERE kode_anggota=%s',
                       (nama, alamat, telepon, email if email else None, kode))
            messagebox.showinfo('Sukses', 'Anggota berhasil diupdate.')
            self.refresh()
            self.clear_form()
        except Error as e:
            messagebox.showerror('Database Error', f'Gagal update anggota.\n{e}')

    def delete_anggota(self):
        kode = self.kode_var.get().strip()
        if not kode:
            messagebox.showwarning('Input Error', 'Pilih anggota untuk dihapus.')
            return
        confirm = messagebox.askyesno('Konfirmasi', f'Yakin ingin menghapus anggota dengan kode {kode}?')
        if not confirm:
            return
        try:
            safe_query('DELETE FROM anggota WHERE kode_anggota=%s', (kode,))
            messagebox.showinfo('Sukses', 'Anggota berhasil dihapus.')
            self.refresh()
            self.clear_form()
        except Error as e:
            messagebox.showerror('Database Error', f'Gagal hapus anggota.\n{e}')


# -------------------- RUN --------------------
if __name__ == '__main__':
    # quick connection test
    try:
        conn = get_db_connection()
        conn.close()
    except Error as e:
        tk.Tk().withdraw()
        messagebox.showerror('Database Error', f'Tidak bisa terhubung ke database dengan konfigurasi saat ini.\n{e}')
        raise SystemExit(1)

    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()
