import tkinter as tk

def hitung_volume():
    try:
        alas_segitiga = float(entry_alas_segitiga.get())
        tinggi_segitiga = float(entry_tinggi_segitiga.get())
        tinggi_limas = float(entry_tinggi_limas.get())
        volume = (1/3) * 0.5 * alas_segitiga * tinggi_segitiga * tinggi_limas
        label_hasil_volume.config(text=f"Volume: {volume:.2f} (unit kubik)")
        label_keterangan_volume.config(text="Hasil perhitungan volume limas segitiga:")
    except ValueError:
        label_hasil_volume.config(text="Masukkan angka yang valid")
        label_keterangan_volume.config(text="")

def hitung_luas_permukaan():
    try:
        alas_segitiga = float(entry_alas_segitiga.get())
        tinggi_segitiga = float(entry_tinggi_segitiga.get())
        tinggi_limas = float(entry_tinggi_limas.get())
        luas_permukaan = (0.5 * alas_segitiga * tinggi_segitiga) + (3 * 0.5 * alas_segitiga * tinggi_limas)
        label_hasil_luas_permukaan.config(text=f"Luas Permukaan: {luas_permukaan:.2f} (unit persegi)")
        label_keterangan_luas_permukaan.config(text="Hasil perhitungan luas permukaan limas segitiga:")
    except ValueError:
        label_hasil_luas_permukaan.config(text="Masukkan angka yang valid")
        label_keterangan_luas_permukaan.config(text="")

# Membuat jendela utama
window = tk.Tk()
window.title("Menghitung Luas dan Volume Limas Segitiga")
window.configure(bg='chocolate')  # Mengatur warna latar belakang menjadi biru

# Membuat label untuk alas segitiga, tinggi segitiga, dan tinggi limas segitiga
label_alas_segitiga = tk.Label(window, text="Muhamad Farhan 220511046")
label_alas_segitiga.pack()
label_alas_segitiga = tk.Label(window, text="Alas Segitiga:")
label_alas_segitiga.pack()
entry_alas_segitiga = tk.Entry(window)
entry_alas_segitiga.pack()

label_tinggi_segitiga = tk.Label(window, text="Tinggi Segitiga:")
label_tinggi_segitiga.pack()
entry_tinggi_segitiga = tk.Entry(window)
entry_tinggi_segitiga.pack()

label_tinggi_limas = tk.Label(window, text="Tinggi Limas Segitiga:")
label_tinggi_limas.pack()
entry_tinggi_limas = tk.Entry(window)
entry_tinggi_limas.pack()

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
