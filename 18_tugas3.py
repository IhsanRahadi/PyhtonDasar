# Input daftar bilangan dari pengguna
bilangan = input("Masukkan sejumlah bilangan (pisahkan dengan spasi): ")

# Membagi daftar bilangan menjadi bilangan-bilangan terpisah
bilangan_list = bilangan.split()

# Inisialisasi hitungan bilangan ganjil dan genap
bilangan_ganjil = 0
bilangan_genap = 0

# Loop melalui setiap bilangan dalam daftar
for bil in bilangan_list:
    bil = int(bil)
    if bil % 2 == 0:
        bilangan_genap += 1
    else:
        bilangan_ganjil += 1

# Cetak hasil
print(f"Jumlah bilangan ganjil: {bilangan_ganjil}")
print(f"Jumlah bilangan genap: {bilangan_genap}")