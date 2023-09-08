while True:
  nilai = int(input("masukkan nilai siswa : "))

  if nilai >= 75:
    print("tuntas")

  elif nilai <= 75:
    ulang = input("Input Mengulang (Ya/Tidak) : ")
    if ulang.lower() != 'ya':
      break

else:
    print('tidak tuntas')
    
