# Template awal untuk Tugas 1
class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.koleksi_buku = []  # Implementasi: atribut untuk koleksi buku
        self.daftar_anggota = []  # Implementasi: atribut untuk daftar anggota
        self.peminjaman = []  # Implementasi: atribut untuk transaksi peminjaman
    # Implementasi: tambahkan atribut untuk koleksi buku dan daftar anggota
    def tambah_buku(self, buku):
        self.koleksi_buku.append(buku)
        print(f"'{buku.judul}' berhasil ditambahkan ke koleksi '{self.nama}'")
    def daftar_anggota(self, anggota):
        self.daftar_anggota.append(anggota)
        print(f"Anggota '{anggota.nama}' telah terdaftar di {self.nama}.")
    def pinjam_buku(self, anggota, buku, tanggal_pinjam):
        if buku in self.koleksi_buku:
            peminjaman_baru = Peminjaman(anggota, buku, tanggal_pinjam)
            self.peminjaman.append(peminjaman_baru)
            print(f"'{anggota.nama}' telah meminjam buku '{buku.judul}' pada {tanggal_pinjam}.")
        else:
            print(f"Buku '{buku.judul}' tidak tersedia di {self.nama}.")
    def tampilkan_status_peminjaman(self):
        # Menampilkan semua data peminjaman
        print("\n=== Status Peminjaman Buku ===")
        if not self.peminjaman:
            print("Belum ada buku yang dipinjam.")
        else:
            for p in self.peminjaman:
                print(f"- {p.anggota.nama} meminjam '{p.buku.judul}' pada {p.tanggal_pinjam}")


class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
class Anggota:
    def __init__(self, nama):
        self.nama = nama
class Peminjaman:
    def __init__(self, anggota, buku, tanggal_pinjam):
        self.anggota = anggota
        self.buku = buku
        self.tanggal_pinjam = tanggal_pinjam

# objek perpustakaan, buku, dan anggota
perpus = Perpustakaan("Perpustakaan Kota")
Buku1 =  Buku("negeri para bedebah","Tere liye")
Buku2 = Buku("laskar pelangi","Andrea Hirata")
Anggota1 = Anggota("Budi Pekerti")

# menabah buku ke perpustakaan
perpus.tambah_buku(Buku1)
perpus.tambah_buku(Buku2)

# menambah anggota ke perpustakaan
perpus.daftar_anggota(Anggota1)

# peminjaman buku
perpus.pinjam_buku(Anggota1, Buku1, "2024-06-10")

#status peminjaman
perpus.tampilkan_status_peminjaman()