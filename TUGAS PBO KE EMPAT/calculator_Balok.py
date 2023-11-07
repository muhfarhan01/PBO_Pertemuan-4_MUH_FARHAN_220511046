import tkinter as tk

def hitung_volume():
    try:
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        tinggi = float(entry_tinggi.get())
        volume = panjang * lebar * tinggi
        label_hasil_volume.config(text=f"Volume: {volume:.2f} (unit kubik)")
        label_keterangan_volume.config(text="Hasil perhitungan volume balok:")
    except ValueError:
        label_hasil_volume.config(text="Masukkan angka yang valid")
        label_keterangan_volume.config(text="")

def hitung_luas_permukaan():
    try:
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        tinggi = float(entry_tinggi.get())
        luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
        label_hasil_luas_permukaan.config(text=f"Luas Permukaan: {luas_permukaan:.2f} (unit persegi)")
        label_keterangan_luas_permukaan.config(text="Hasil perhitungan luas permukaan balok:")
    except ValueError:
        label_hasil_luas_permukaan.config(text="Masukkan angka yang valid")
        label_keterangan_luas_permukaan.config(text="")

# Membuat jendela utama
window = tk.Tk()
window.title("Menghitung Luas dan Volume Balok")
window.configure(bg='lightblue')  # Mengatur warna latar belakang menjadi biru muda

# Membuat label untuk panjang, lebar, dan tinggi balok
label_panjang = tk.Label(window, text="Muhamad Farhan 220511046")
label_panjang.pack()
label_panjang = tk.Label(window, text="Panjang Balok:")
label_panjang.pack()
entry_panjang = tk.Entry(window)
entry_panjang.pack()

label_lebar = tk.Label(window, text="Lebar Balok:")
label_lebar.pack()
entry_lebar = tk.Entry(window)
entry_lebar.pack()

label_tinggi = tk.Label(window, text="Tinggi Balok:")
label_tinggi.pack()
entry_tinggi = tk.Entry(window)
entry_tinggi.pack()

# Tombol untuk menghitung volume
btn_volume = tk.Button(window, text="Hitung Volume", command=hitung_volume)
btn_volume.pack()

# Label untuk menampilkan hasil volume
label_hasil_volume = tk.Label(window, text="")
label_hasil_volume.pack()

# Label keterangan hasil volume
label_keterangan_volume = tk.Label(window, text="", font=("Arial", 12, "italic"), bg="green", fg="white")
label_keterangan_volume.pack()

# Tombol untuk menghitung luas permukaan
btn_luas_permukaan = tk.Button(window, text="Hitung Luas Permukaan", command=hitung_luas_permukaan)
btn_luas_permukaan.pack()

# Label untuk menampilkan hasil luas permukaan
label_hasil_luas_permukaan = tk.Label(window, text="")
label_hasil_luas_permukaan.pack()

# Label keterangan hasil luas permukaan
label_keterangan_luas_permukaan = tk.Label(window, text="", font=("Arial", 12, "italic"), bg="green", fg="white")
label_keterangan_luas_permukaan.pack()

# Memulai aplikasi
window.mainloop()
