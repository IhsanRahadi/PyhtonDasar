import tkinter as tk

def hitung_total():
    harga = float(entry_harga.get())
    kuantitas = int(entry_kuantitas.get())
    total = harga * kuantitas
    label_total.config(text=f"Total: Rp {total}")

root = tk.Tk()
root.title("Program Kasir")

label_harga = tk.Label(root, text="Harga:")
label_harga.pack()
entry_harga = tk.Entry(root)
entry_harga.pack()

label_kuantitas = tk.Label(root, text="Kuantitas:")
label_kuantitas.pack()
entry_kuantitas = tk.Entry(root)
entry_kuantitas.pack()

tombol_hitung = tk.Button(root, text="Hitung Total", command=hitung_total)
tombol_hitung.pack()

label_total = tk.Label(root, text="")
label_total.pack()

root.mainloop()