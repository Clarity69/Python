# Parent Class
class Karyawan:
    def __init__(self, nama, id_karyawan, gaji_pokok):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.gaji_pokok = gaji_pokok

    def hitung_gaji(self):
        return self.gaji_pokok

    def info(self):
        return f"Karyawan : {self.nama}, ID: {self.id_karyawan}, Gaji: {self.hitung_gaji()}"


# Subclass Manager (Inheritance dari Karyawan)
class Manager(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok, tunjangan):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.tunjangan = tunjangan

    # Polymorphism: Override method hitung_gaji()
    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan

    # Polymorphism: Override method info()
    def info(self):
        return f"Manager : {self.nama}, ID: {self.id_karyawan}, Gaji: {self.hitung_gaji()}"


# Subclass Programmer (Inheritance dari Karyawan)
class Programmer(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok, bonus):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.bonus = bonus

    # Polymorphism: Override method hitung_gaji()
    def hitung_gaji(self):
        return self.gaji_pokok + self.bonus

    # Polymorphism: Override method info()
    def info(self):
        return f"Programmer : {self.nama}, ID: {self.id_karyawan}, Gaji: {self.hitung_gaji()}"


# --- Contoh Penggunaan ---
if __name__ == "__main__":
    manager1 = Manager("Taro", "M001", 12000000, 3000000.0)
    programmer1 = Programmer("Nabil", "P001", 10000000, 2000000.0)

    # Polymorphism in action
    daftar_karyawan = [manager1, programmer1]

    for karyawan in daftar_karyawan:
        print(karyawan.info())
