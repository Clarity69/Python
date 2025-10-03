class Perusahaan:
    # Menyimpan daftar proyek dan tim
    def __init__(self, nama):
        # Inisialisasi perusahaan dengan nama, daftar proyek, dan daftar tim
        self.nama = nama
        self.daftar_proyek = [] # aggregation
        self.daftar_tim = []    # composition

    def buat_proyek(self, nama_proyek, deskripsi):
        # Membuat proyek baru dan menambahkannya ke daftar_proyek
        proyek_baru = Proyek(nama_proyek, deskripsi)
        self.daftar_proyek.append(proyek_baru)
        print(f"proyek '{nama_proyek}' telah dibuat di {self.nama}")
        return proyek_baru

    def buat_tim(self, nama_tim):
        # Membuat tim baru dan menambahkannya ke daftar_tim
        tim_baru = Tim(nama_tim)
        self.daftar_tim.append(tim_baru)
        return tim_baru

class Proyek:
    # Menyimpan nama, deskripsi, dan daftar tugas
    def __init__(self, nama, deskripsi):
        # Inisialisasi proyek dengan nama, deskripsi, dan daftar tugas
        self.nama = nama
        self.deskripsi = deskripsi
        self.tugas_list = [] # composition

    def tambah_tugas(self, deskripsi_tugas):
        # Membuat tugas baru dan menambahkannya ke tugas_list
        tugas = Tugas(deskripsi_tugas)
        self.tugas_list.append(tugas)
        print(f"Tugas '{deskripsi_tugas}' telah ditambahkan ke proyek '{self.nama}'")
        return tugas

class Tim:
    # Menyimpan nama dan daftar developer
    def __init__(self, nama):
        # Inisialisasi tim dengan nama dan daftar developer
        self.nama = nama
        self.developers = [] # aggregation

    def tambah_developer(self, developer):
        # Menambah developer ke dalam tim
        self.developers.append(developer)

class Developer:
    # Menyimpan nama dan keahlian developer
    def __init__(self, nama, keahlian):
        # Inisialisasi developer dengan nama dan keahlian
        self.nama = nama
        self.keahlian = keahlian

class Tugas:
    # Menyimpan deskripsi tugas dan developer yang ditugaskan
    def __init__(self, deskripsi):
        # Inisialisasi tugas dengan deskripsi dan developer (kosong)
        self.deskripsi = deskripsi
        self.developer = None # association

    def tugaskan_ke(self, developer):
        # Menugaskan tugas ke developer tertentu
        self.developer = developer
        print(f"Tugas '{self.deskripsi}' ditugaskan ke '{developer.nama}'")