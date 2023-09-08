# Mengimpor modul math untuk penggunaan nilai pi
import math

# Fungsi untuk menghitung volume tabung
def hitung_volume_tabung(radius, tinggi):
    volume = math.pi * radius**2 * tinggi
    return volume

# Fungsi untuk menghitung volume balok
def hitung_volume_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume

# Input data dari pengguna
radius_tabung = float(input("Masukkan jari-jari tabung: "))
tinggi_tabung = float(input("Masukkan tinggi tabung: "))

panjang_balok = float(input("Masukkan panjang balok: "))
lebar_balok = float(input("Masukkan lebar balok: "))
tinggi_balok = float(input("Masukkan tinggi balok: "))

# Hitung volume tabung dan balok
volume_tabung = hitung_volume_tabung(radius_tabung, tinggi_tabung)
volume_balok = hitung_volume_balok(panjang_balok, lebar_balok, tinggi_balok)

# Cetak hasil
print(f"Volume tabung adalah: {volume_tabung:.2f}")
print(f"Volume balok adalah: {volume_balok:.2f}")