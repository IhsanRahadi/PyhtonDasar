class Vahicle:
    def __init__(self, merk, tahun, warna):
        self.merk = merk
        self.tahun = tahun 
        self.warna = warna

    def tampilkan_info(self):
        print(f"Merk: {self.merk}")
        print(f"Tahun: {self.tahun}")
        print(f"Warna: {self.warna}")

class Car(Vahicle):
    def __init__(self, merk, tahun, warna, model):
        super().__init__(merk, tahun, warna)
        self.model = model
    
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"MOdel: {self.model}")

if __name__ == "__main__":
    car = Car("Toyota", 2022, "Merah", "Camry")

    print("Info kendaraan:")
    car.tampilkan_info()