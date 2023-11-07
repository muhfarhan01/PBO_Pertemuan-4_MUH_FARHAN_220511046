import tkinter as tk

def hitung_volume():
    try:
        panjang_alas = float(entry_panjang_alas.get())
        lebar_alas = float(entry_lebar_alas.get())
        tinggi = float(entry_tinggi.get())
        volume = (1/3) * panjang_alas * lebar_alas * tinggi
        label_hasil_volume.config(text=f"Volume: {volume:.2f} (unit kubik)")
        label_keterangan_volume.config(text="Hasil perhitungan volume limas segiempat:")
    except ValueError:
        label_hasil_volume.config(text="Masukkan angka yang valid")
        label_keterangan_volume.config(text="")

def hitung_luas_permukaan():
    try:
        panjang_alas = float(entry_panjang_alas.get())
        lebar_alas = float(entry_lebar_alas.get())
        tinggi = float(entry_tinggi.get())
        luas_permukaan = (panjang_alas * lebar_alas) + 2 * (panjang_alas * tinggi) + 2 * (lebar_alas * tinggi)
        label_hasil_luas_permukaan.config(text=f"Luas Permukaan: {luas_permukaan:.2f} (unit persegi)")
        label_keterangan_luas_permukaan.config(text="Hasil perhitungan luas permukaan limas segiempat:")
    except ValueError:
        label_hasil_luas_permukaan.config(text="Masukkan angka yang valid")
        label_keterangan_luas_permukaan.config(text="")

# Membuat jendela utama
window = tk.Tk()
window.title("Menghitung Luas dan Volume Limas Segiempat")
window.configure(bg='green')  # Mengatur warna latar belakang menjadi hijau

# Membuat label untuk panjang alas, lebar alas, dan tinggi limas segiempat
label_panjang_alas = tk.Label(window, text="Muhamad Farhan 220511046")
label_panjang_alas.pack()
label_panjang_alas = tk.Label(window, text="Panjang Alas:")
label_panjang_alas.pack()
entry_panjang_alas = tk.Entry(window)
entry_panjang_alas.pack()

label_lebar_alas = tk.Label(window, text="Lebar Alas:")
label_lebar_alas.pack()
entry_lebar_alas = tk.Entry(window)
entry_lebar_alas.pack()

label_tinggi = tk.Label(window, text="Tinggi Limas:")
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
label_keterangan_volume = tk.Label(window, text="", font=("Arial", 12, "italic"), bg="blue", fg="white")
label_keterangan_volume.pack()

# Tombol untuk menghitung luas permukaan
btn_luas_permukaan = tk.Button(window, text="Hitung Luas Permukaan", command=hitung_luas_permukaan)
btn_luas_permukaan.pack()

# Label untuk menampilkan hasil luas permukaan
label_hasil_luas_permukaan = tk.Label(window, text="")
label_hasil_luas_permukaan.pack()

# Label keterangan hasil luas permukaan
label_keterangan_luas_permukaan = tk.Label(window, text="", font=("Arial", 12, "italic"), bg="blue", fg="white")
label_keterangan_luas_permukaan.pack()

# Memulai aplikasi
window.mainloop()
