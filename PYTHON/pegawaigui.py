import tkinter as tk
from tkinter import ttk

# Import kelas-kelas yang diperlukan
# Sesuaikan path jika diperlukan
from pegawai import Pegawai, PegawaiTetap, PegawaiHarian, PegawaiKontrak

class Pegawai:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Informasi Pegawai")

        # Definisi atribut-atribut yang diperlukan
        self.entry_jenis = ttk.Entry(root)
        self.entry_nama_pegawai = ttk.Entry(root)
        self.entry_gaji_pokok = ttk.Entry(root)
        self.entry_bonus = ttk.Entry(root)
        self.entry_lama_bergabung = ttk.Entry(root)
        self.entry_jam_kerja = ttk.Entry(root)
        self.entry_durasi = ttk.Entry(root)
        
        # Definisi atribut label untuk keterangan
        self.label_jenis = ttk.Label(root, text="Jenis Pegawai:")
        self.label_nama_pegawai = ttk.Label(root, text="Nama Pegawai:")
        self.label_gaji_pokok = ttk.Label(root, text="Gaji Pokok:")
        self.label_bonus = ttk.Label(root, text="Bonus:")
        self.label_lama_bergabung = ttk.Label(root, text="Lama Bergabung (thn):")
        self.label_jam_kerja = ttk.Label(root, text="Jam Kerja:")
        self.label_durasi = ttk.Label(root, text="Durasi Kontrak (bulan):")

        # Definisi atribut tombol buat pegawai
        self.btn_buat_pegawai = ttk.Button(root, text="Create", command=self.buat_pegawai)
        # Definisi atribut tombol hapus
        self.btn_reset_form = ttk.Button(root, text="Reset", command=self.reset_form)

        # Definisi atribut teks untuk menampilkan hasil
        self.result_text = tk.Text(root, height=10, width=40)

        # Menyusun widget-widget di dalam grid
        self.label_jenis.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_jenis.grid(row=0, column=1, padx=10, pady=10)
        self.label_nama_pegawai.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_nama_pegawai.grid(row=1, column=1, padx=10, pady=10)
        self.label_gaji_pokok.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_gaji_pokok.grid(row=2, column=1, padx=10, pady=10)
        self.label_bonus.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_bonus.grid(row=3, column=1, padx=10, pady=10)
        self.label_lama_bergabung.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_lama_bergabung.grid(row=4, column=1, padx=10, pady=10)
        self.label_jam_kerja.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_jam_kerja.grid(row=5, column=1, padx=10, pady=10)
        self.label_durasi.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_durasi.grid(row=6, column=1, padx=10, pady=10)

        self.btn_buat_pegawai.grid(row=7, column=0, pady=10, padx=(0, 5), sticky=tk.E)
        self.btn_reset_form.grid(row=7, column=1, pady=10, padx=(5, 0), sticky=tk.W)

        self.result_text.grid(row=8, column=0, columnspan=2, pady=10)
        
        # Inisialisasi atribut elements
        self.elements_tetap = [self.label_lama_bergabung, self.entry_lama_bergabung]
        self.elements_harian = [self.label_jam_kerja, self.entry_jam_kerja]
        self.elements_kontrak = [self.label_durasi, self.entry_durasi]
        
        self.show_hide_elements("")

    def buat_pegawai(self):
        jenis_pegawai = self.entry_jenis.get().capitalize()
        nama = self.entry_nama_pegawai.get()
        gaji_pokok = self.entry_gaji_pokok.get()
        bonus = self.entry_bonus.get()

        # Memanggil metode untuk menampilkan atau menyembunyikan elemen-elemen
        self.show_hide_elements(jenis_pegawai)

        if not gaji_pokok or not bonus:
            self.result_text.insert(tk.END, "Gaji pokok dan bonus harus diisi.")
            return

        gaji_pokok = int(gaji_pokok)
        bonus = int(bonus)

        if jenis_pegawai == "Tetap":
            self.label_lama_bergabung.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
            self.entry_lama_bergabung.grid(row=4, column=1, padx=10, pady=10)
            lama_bergabung = self.entry_lama_bergabung.get()
            if not lama_bergabung:
                self.result_text.insert(tk.END, "Lama bergabung harus diisi.")
                return
            lama_bergabung = int(lama_bergabung)
            pegawai = PegawaiTetap(nama, gaji_pokok, bonus, lama_bergabung)
        elif jenis_pegawai == "Harian":
            self.label_jam_kerja.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)
            self.entry_jam_kerja.grid(row=5, column=1, padx=10, pady=10)
            jam_kerja = self.entry_jam_kerja.get()
            if not jam_kerja:
                self.result_text.insert(tk.END, "Jam kerja harus diisi.")
                return
            jam_kerja = int(jam_kerja)
            pegawai = PegawaiHarian(nama, gaji_pokok, jam_kerja, bonus)
        elif jenis_pegawai == "Kontrak":
            self.label_durasi.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)
            self.entry_durasi.grid(row=6, column=1, padx=10, pady=10)
            durasi = self.entry_durasi.get()
            if not durasi:
                self.result_text.insert(tk.END, "Durasi kontrak harus diisi.")
                return
            durasi = int(durasi)
            pegawai = PegawaiKontrak(nama, gaji_pokok, durasi, bonus)
        else:
            self.result_text.insert(tk.END, "Jenis Pegawai tidak valid.")
            return
        
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Informasi Pegawai:\n")
        self.result_text.insert(tk.END, pegawai.tampilkan_rincian_pegawai() + "\n")
        self.result_text.insert(tk.END, f"Total gaji: {pegawai.hitung_gaji_total()}")
        
    def show_hide_elements(self, jenis_pegawai):
        # Menyembunyikan semua elemen terlebih dahulu
        for elem in self.elements_tetap + self.elements_harian + self.elements_kontrak:
            elem.grid_remove()

        # Menampilkan elemen yang sesuai dengan jenis pegawai
        if jenis_pegawai == "Tetap":
            for elem in self.elements_tetap:
                elem.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
        elif jenis_pegawai == "Harian":
            for elem in self.elements_harian:
                elem.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)
        elif jenis_pegawai == "Kontrak":
            for elem in self.elements_kontrak:
                elem.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)
        
        # Tambahkan kondisi untuk menampilkan atau menyembunyikan elemen Jam Kerja dan Durasi Kontrak
        if jenis_pegawai == "Tetap" or jenis_pegawai == "Harian":
            self.label_durasi.grid_remove()
            self.entry_durasi.grid_remove()
        elif jenis_pegawai == "Kontrak":
            self.label_jam_kerja.grid_remove()
            self.entry_jam_kerja.grid_remove()
            
    def reset_form(self):
        # Mengatur nilai entri dan teks kembali ke nilai awal atau kosong
        self.entry_jenis.delete(0, tk.END)
        self.entry_nama_pegawai.delete(0, tk.END)
        self.entry_gaji_pokok.delete(0, tk.END)
        self.entry_bonus.delete(0, tk.END)
        self.entry_lama_bergabung.delete(0, tk.END)
        self.entry_jam_kerja.delete(0, tk.END)
        self.entry_durasi.delete(0, tk.END)

        # Memanggil metode untuk menampilkan atau menyembunyikan elemen-elemen
        self.show_hide_elements("")

        # Menghapus teks hasil
        self.result_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Pegawai(root)
    root.mainloop()

