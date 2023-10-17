class Pegawai:
    def __init__(self, nama_pegawai, gaji_pokok, bonus=0):
        self.nama_pegawai = nama_pegawai
        self.gaji_pokok = gaji_pokok
        self.bonus = bonus

    def hitung_gaji_total(self):
        return self.gaji_pokok

    def tampilkan_rincian_pegawai(self):
        return f"Nama Pegawai: {self.nama_pegawai} \nGaji Pokok: {self.gaji_pokok} \nBonus: {self.bonus}"


class PegawaiTetap(Pegawai):
    def __init__(self, nama_pegawai, gaji_pokok, bonus, lama_bergabung):
        super().__init__(nama_pegawai, gaji_pokok, bonus)
        self.lama_bergabung = lama_bergabung

    def hitung_gaji_total(self):
        if self.lama_bergabung >= 5:
            return super().hitung_gaji_total() + self.bonus
        else:
            print("Lama bergabung dengan perusahaan kurang dari 5 tahun. Bonus otomatis tidak dibeirkan")
            return super().hitung_gaji_total() 
    
    def tampilkan_rincian_pegawai(self):
        return super().tampilkan_rincian_pegawai() + f"\nLama bergabung dgn perusahaan (thn) : {self.lama_bergabung}"

class PegawaiHarian(Pegawai):
    def __init__(self, nama_pegawai, gaji_pokok, jam_kerja, bonus):
        super().__init__(nama_pegawai, gaji_pokok, bonus)
        self.jam_kerja = jam_kerja

    def hitung_gaji_total(self):
        if self.jam_kerja >= 8:
            return super().hitung_gaji_total() + self.bonus
        else:
            print("Jam kerja kurang dari 8 jam. Bonus otomatis tidak diberikan.")
            return super().hitung_gaji_total()

    def tampilkan_rincian_pegawai(self):
        return super().tampilkan_rincian_pegawai() + f"\nJam Kerja : {self.jam_kerja}"

class PegawaiKontrak(Pegawai):
    def __init__(self, nama_pegawai, gaji_pokok, durasi_kontrak, bonus):
        super().__init__(nama_pegawai, gaji_pokok, bonus)
        self.durasi_kontrak = durasi_kontrak

    def hitung_gaji_total(self):
        if self.durasi_kontrak >= 24:
            return super().hitung_gaji_total() + self.bonus
        else:
            print("Durasi kontrak kurang dari 24 bulan (2 tahun). Bonus otomatis tidak diberikan.")
            return super().hitung_gaji_total() 
    
    def tampilkan_rincian_pegawai(self):
        return super().tampilkan_rincian_pegawai() + f"\nDurasi Kontrak : {self.durasi_kontrak}"


# Fungsi untuk membuat pegawai berdasarkan input pengguna
def buat_pegawai():
    jenis_pegawai = input("Jenis Pegawai (Tetap/Harian/Kontrak): ").capitalize()
    nama_pegawai = input("Nama Pegawai: ")
    gaji_pokok = int(input("Gaji Pokok: "))
    bonus = int(input("Bonus: "))

    if jenis_pegawai == "Tetap":
        lama_bergabung = int(input("Lama bergabung dgn perusahaan (thn): "))
        return PegawaiTetap(nama_pegawai, gaji_pokok, bonus, lama_bergabung)
    elif jenis_pegawai == "Harian":
        jam_kerja = int(input("Jam Kerja: "))
        return PegawaiHarian(nama_pegawai, gaji_pokok, jam_kerja, bonus)
    elif jenis_pegawai == "Kontrak":
        durasi = int(input("Durasi Kontrak (bulan): "))
        return PegawaiKontrak(nama_pegawai, gaji_pokok, durasi, bonus)
    else:
        print("Jenis Pegawai tidak valid.")
        return None

pegawai = buat_pegawai()
if pegawai:
    print("\nInformasi Pegawai :")
    print(pegawai.tampilkan_rincian_pegawai())
    print("Total gaji :", pegawai.hitung_gaji_total())
