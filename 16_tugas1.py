# Fungsi untuk menghitung luas dan keliling persegi
def hitung_persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling

# Fungsi untuk menghitung luas dan keliling persegi panjang
def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

# Fungsi untuk menghitung luas dan keliling trapesium
def hitung_trapesium(alas_atas, alas_bawah, tinggi, sisi_miring):
    luas = 0.5 * (alas_atas + alas_bawah) * tinggi
    keliling = alas_atas + alas_bawah + (2 * sisi_miring)
    return luas, keliling

# Input dari pengguna
pilihan = input("Pilih bangun datar (persegi, persegi panjang, atau trapesium): ")

# Proses sesuai pilihan
if pilihan == "persegi":
    sisi = float(input("Masukkan panjang sisi persegi: "))
    luas, keliling = hitung_persegi(sisi)
elif pilihan == "persegi panjang":
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    luas, keliling = hitung_persegi_panjang(panjang, lebar)
elif pilihan == "trapesium":
    alas_atas = float(input("Masukkan panjang alas atas trapesium: "))
    alas_bawah = float(input("Masukkan panjang alas bawah trapesium: "))
    tinggi = float(input("Masukkan tinggi trapesium: "))
    sisi_miring = float(input("Masukkan panjang sisi miring trapesium: "))
    luas, keliling = hitung_trapesium(alas_atas, alas_bawah, tinggi, sisi_miring)
else:
    print("Pilihan tidak valid")

# Cetak hasil
if pilihan in ["persegi", "persegi panjang", "trapesium"]:
    print(f"Luas {pilihan}: {luas}")
    print(f"Keliling {pilihan}: {keliling}")