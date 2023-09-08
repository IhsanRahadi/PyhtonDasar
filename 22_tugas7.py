nama = input("Masukkan Nama : ")
gaji = int(input("Masukan Gaji Pokok :"))

tunjangan = 20/100 * gaji
pajak = 15/100 * (gaji+tunjangan)
gajiBersih = int(gaji + tunjangan - pajak)

print("_ _ _ _ _ _ _ _ _ _ _ _ ")
print("Nama : ", nama)
print("Gaji Pokok : ", gaji)
print("Gaji Bersih : ", gajiBersih)