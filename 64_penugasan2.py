import tkinter as tk
from datetime import datetime

# Fungsi untuk menghitung biaya parkir
def hitung_biaya():
    waktu_masuk = entry_masuk.get()
    waktu_keluar = entry_keluar.get()

    # Parsing waktu masuk dan keluar
    try:
        waktu_masuk = datetime.strptime(waktu_masuk, "%H:%M")
        waktu_keluar = datetime.strptime(waktu_keluar, "%H:%M")

        # Menghitung selisih waktu
        selisih = waktu_keluar - waktu_masuk

        # Menghitung biaya parkir (misalnya, Rp 5.000 per jam)
        tarif_per_jam = 5000
        biaya_parkir = (selisih.total_seconds() / 3600) * tarif_per_jam

        # Menampilkan biaya parkir pada label
        label_biaya.config(text=f"Biaya Parkir: Rp {biaya_parkir:.2f}")

        # Menambahkan informasi parkir ke daftar pelanggan
        nopol = entry_nopol.get()
        informasi_parkir = f"Nomor Plat: {nopol}, Masuk: {waktu_masuk.strftime('%H:%M')}, Keluar: {waktu_keluar.strftime('%H:%M')}, Biaya: Rp {biaya_parkir:.2f}"
        tambah_pelanggan(informasi_parkir)
    except ValueError:
        label_biaya.config(text="Format waktu salah")

# Fungsi untuk mencari nomor plat polisi
def cari_nopol():
    nopol_dicari = entry_nopol.get()
    # Implementasikan logika pencarian nopol di sini, misalnya mencari dalam database
    # Jika ditemukan, tampilkan informasi parkir atau biaya parkir jika tersedia
    # Jika tidak ditemukan, tampilkan pesan "Nomor Plat Tidak Ditemukan"
    # Contoh:
    hasil_pencarian.config(text=f"Hasil Pencarian untuk {nopol_dicari}: Informasi Parkir")

# Fungsi untuk menambahkan pelanggan ke daftar
def tambah_pelanggan(info_parkir):
    daftar_pelanggan.insert(tk.END, info_parkir)

# Membuat window utama
root = tk.Tk()
root.title("Program Parkir")

# Judul Program Parkir
label_judul = tk.Label(root, text="PROGRAM PARKIR", font=("Arial", 18, "bold"))
label_judul.pack()

# Membuat label dan entry untuk waktu masuk
label_masuk = tk.Label(root, text="Waktu Masuk (HH:MM):")
label_masuk.pack()
entry_masuk = tk.Entry(root)
entry_masuk.pack()

# Membuat label dan entry untuk waktu keluar
label_keluar = tk.Label(root, text="Waktu Keluar (HH:MM):")
label_keluar.pack()
entry_keluar = tk.Entry(root)
entry_keluar.pack()

# Tombol untuk menghitung biaya parkir
button_hitung = tk.Button(root, text="Hitung Biaya Parkir", command=hitung_biaya)
button_hitung.pack()

# Label untuk menampilkan biaya parkir
label_biaya = tk.Label(root, text="Biaya Parkir: Rp 0.00")
label_biaya.pack()

# Label dan entry untuk mencari nomor plat polisi
label_nopol = tk.Label(root, text="Cari Nomor Plat Polisi:")
label_nopol.pack()
entry_nopol = tk.Entry(root)
entry_nopol.pack()

# Tombol untuk mencari nomor plat polisi
button_cari = tk.Button(root, text="Cari Nopol", command=cari_nopol)
button_cari.pack()

# Label untuk menampilkan hasil pencarian
hasil_pencarian = tk.Label(root, text="")
hasil_pencarian.pack()

# Listbox untuk menampilkan daftar pelanggan (dengan height diperbesar)
daftar_pelanggan = tk.Listbox(root, height=10, width=100)
daftar_pelanggan.pack()

# Tombol untuk menambahkan pelanggan ke daftar
button_tambah_pelanggan = tk.Button(root, text="Tambah Pelanggan", command=tambah_pelanggan)
button_tambah_pelanggan.pack()

# Menjalankan aplikasi
root.mainloop()