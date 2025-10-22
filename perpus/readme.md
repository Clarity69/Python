# 📚 Perpustakaan App

Aplikasi manajemen perpustakaan berbasis **Tkinter (Python GUI)** yang terhubung ke **MySQL Database**.

---

## 🧩 Fitur Utama

1. **Login** — validasi pengguna berdasarkan data di tabel `users`.
2. **Register** — membuat akun baru (role: `admin` atau `petugas`).
3. **Dashboard** — menampilkan data singkat pengguna setelah login.
4. **Manajemen Buku** (CRUD):

   * Tambah, ubah, hapus, dan cari buku berdasarkan judul/pengarang.
   * Validasi input (kode unik, tahun angka, stok ≥ 0).
5. **Manajemen Anggota** (CRUD):

   * Tambah, ubah, hapus, dan tampilkan data anggota.
   * Validasi format email dan nomor telepon.
6. **Error Handling** — semua interaksi database memiliki pesan error yang jelas.

---

## ⚙️ Konfigurasi Database

Sebelum menjalankan aplikasi, pastikan MySQL Server aktif dan database sudah dibuat.

### Struktur Database

Nama database default: **`perpustakaan_db`**

Tabel yang dibutuhkan:

* **users** → menyimpan akun login.
* **buku** → menyimpan data buku.
* **anggota** → menyimpan data anggota perpustakaan.

Edit konfigurasi koneksi pada bagian atas file `perpustakaan_app.py` jika diperlukan:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # ubah jika MySQL kamu memakai password
    'database': 'perpustakaan_db'
}
```

---

## 🚀 Cara Menjalankan Aplikasi

1. **Instal dependency:**

   ```bash
   pip install mysql-connector-python
   ```
2. **Pastikan database dan tabel sudah tersedia.**
   Jika belum, kamu bisa membuatnya manual atau minta file SQL pendukung.
3. **Jalankan program:**

   ```bash
   python perpustakaan_app.py
   ```
4. **Login atau Register akun baru.**

   * Default: belum ada akun → klik tombol **Register** di form login.
   * Setelah berhasil register, login menggunakan username & password baru.

---

## 🧠 Catatan Tambahan

* Jika koneksi database gagal, cek pengaturan host/user/password.
* Password masih disimpan dalam teks biasa (plain text). Untuk versi lebih aman, gunakan hashing (misalnya `bcrypt`).
* Dapat dikembangkan lebih lanjut dengan fitur peminjaman buku, laporan, dan hak akses berbasis role.

---

## 👨‍💻 Pembuat

Proyek ini dikembangkan sebagai tugas praktikum Python GUI & MySQL.

> Dibuat dengan ❤️ menggunakan Tkinter + MySQL
