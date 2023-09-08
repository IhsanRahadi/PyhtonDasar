import tkinter as tk
from tkinter import ttk

def tambah_siswa():
    nama = entry_nama.get()
    usia = entry_usia.get()
    kelas = entry_kelas.get()
    
    # Memasukkan data siswa ke dalam tabel
    tree.insert("", "end", values=(nama, usia, kelas))
    
    entry_nama.delete(0, tk.END)
    entry_usia.delete(0, tk.END)
    entry_kelas.delete(0, tk.END)

# Membuat GUI
root = tk.Tk()
root.title("Data Siswa")

frame_input = ttk.Frame(root)
frame_input.pack(padx=20, pady=20)

label_nama = ttk.Label(frame_input, text="Nama Siswa:")
label_nama.grid(row=0, column=0)
entry_nama = ttk.Entry(frame_input)
entry_nama.grid(row=0, column=1)

label_usia = ttk.Label(frame_input, text="Usia Siswa:")
label_usia.grid(row=1, column=0)
entry_usia = ttk.Entry(frame_input)
entry_usia.grid(row=1, column=1)

label_kelas = ttk.Label(frame_input, text="Kelas Siswa:")
label_kelas.grid(row=2, column=0)
entry_kelas = ttk.Entry(frame_input)
entry_kelas.grid(row=2, column=1)

button_tambah = ttk.Button(frame_input, text="Tambah Siswa", command=tambah_siswa)
button_tambah.grid(row=3, columnspan=2)

# Membuat tabel untuk menampilkan data siswa
frame_tabel = ttk.Frame(root)
frame_tabel.pack(padx=20, pady=20)

columns = ("Nama", "Usia", "Kelas")
tree = ttk.Treeview(frame_tabel, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack()

root.mainloop()                                                                                                             