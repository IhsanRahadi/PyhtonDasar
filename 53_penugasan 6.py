import turtle

# Fungsi untuk menggambar logo sekolah
def draw_school_logo():
    # Membuat objek turtle
    t = turtle.Turtle()
    t.speed(2)

    # Menggambar bagian pertama logo
    t.color("orange")  # Warna sesuaikan dengan logo sebenarnya
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    
    t.write("SMK Prestasi Prima", align="center", font=("Arial", 12, "normal"))

    t.hideturtle()

    # Menutup jendela ketika di-klik
    turtle.exitonclick()

# Memanggil fungsi untuk menggambar logo sekolah
draw_school_logo()