import turtle

# Membuat objek turtle
pen = turtle.Turtle()

# Fungsi untuk menggambar cabang pohon
def cabang_pohon(panjang_cabang, turtle_obj):
    if panjang_cabang > 5:
        # Gambar batang pohon
        turtle_obj.forward(panjang_cabang)
        
        # Gambar cabang kanan
        turtle_obj.right(20)
        cabang_pohon(panjang_cabang - 15, turtle_obj)
        
        # Kembali ke posisi awal
        turtle_obj.left(40)
        cabang_pohon(panjang_cabang - 15, turtle_obj)
        
        # Kembali ke posisi awal
        turtle_obj.right(20)
        turtle_obj.backward(panjang_cabang)

# Inisialisasi posisi awal turtle
pen.left(90)
pen.up()
pen.backward(100)
pen.down()

# Panggil fungsi untuk menggambar pohon dengan panjang awal 80
cabang_pohon(80, pen)

# Menutup jendela jika diklik
turtle.exitonclick()
