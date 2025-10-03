# Template awal untuk Tugas 3
class Perusahaan:
    def __init__(self, nama):
        # Implementasi: inisialisasi perusahaan dengan proyek dan tim
        self.nama = nama
        self.daftar_proyek = [] # agreagtion
        self.daftar_tim = [] # composition
    def buat_proyek(self, nama_proyek, deskripsi):
        # Implementasi: buat proyek baru
        proyek_baru = Proyek(nama_proyek, deskripsi)
        self.daftar_proyek.append(proyek_baru)
        print(f"proyek '{nama_proyek}' telah dibuat di {self.nama}")
        return proyek_baru
    def buat_tim(self, nama_tim):
        # Implementasi: buat tim baru
        tim_baru = Tim(nama_tim)
        self.daftar_tim.append(tim_baru)
        return tim_baru
class Proyek:
    def __init__(self, nama, deskripsi):
    # Implementasi: inisialisasi proyek dengan tugas
        self.nama = nama
        self.deskripsi = deskripsi
        self.tugas_list = [] # composition
    def tambah_tugas(self, deskripsi_tugas):
    # Implementasi: tambahkan tugas ke proyek
        tugas = Tugas(deskripsi_tugas)
        self.tugas_list.append(tugas)
        print(f"Tugas '{deskripsi_tugas}' telah ditambahkan ke proyek '{self.nama}'")
        return tugas
class Tim:
    def __init__(self, nama):
    # Implementasi: inisialisasi tim dengan developer
        self.nama = nama
        self.developers = [] # aggregation
    def tambah_developer(self, developer):
    # Implementasi: tambahkan developer ke tim
        self.developers.append(developer)
class Developer:
    def __init__(self, nama, keahlian):
    # Implementasi: inisialisasi developer
        self.nama = nama
        self.keahlian = keahlian
class Tugas:
    def __init__(self, deskripsi):
    # Implementasi: inisialisasi tugas
        self.deskripsi = deskripsi
        self.developer = [] # ascociation
        pass
    def tugaskan_ke(self, developer):
    # Implementasi: tugaskan tugas ke developer
        self.developer = developer
        print(f"Tugas '{self.deskripsi}' ditugaskan ke '{developer.nama}'")
        
# 1. Buat perusahaan
perusahaan = Perusahaan("Tech Solutions")

# 2. Buat proyek (Aggregation)
proyek1 = perusahaan.buat_proyek("Website E-Commerce", "Membangun toko online")

# 3. Buat tim (Composition)
tim1 = perusahaan.buat_tim("Tim Frontend")

# 4. Tambah developer ke tim (Aggregation)
dev1 = Developer("Budi", "Frontend Developer")
dev2 = Developer("Ani", "Backend Developer")
tim1.tambah_developer(dev1)
tim1.tambah_developer(dev2)

# 5. Tambah tugas ke proyek (Composition)
tugas1 = proyek1.tambah_tugas("Membuat halaman utama")
tugas2 = proyek1.tambah_tugas("Membuat sistem login")

# 6. Tugaskan tugas ke developer (Association)
tugas1.tugaskan_ke(dev1)
tugas2.tugaskan_ke(dev2)