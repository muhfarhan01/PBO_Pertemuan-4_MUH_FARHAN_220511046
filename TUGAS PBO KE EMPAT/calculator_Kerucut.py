import tkinter as tk
import math

def hitung_volume():
    try:
        jari_jari = float(entry_jari_jari.get())
        tinggi = float(entry_tinggi.get())
        volume = (1/3) * math.pi * jari_jari**2 * tinggi
        label_hasil_volume.config(text=f"Volume: {volume:.2f} (unit kubik)")
        label_keterangan_volume.config(text="Hasil perhitungan volume kerucut:")
    except ValueError:
        label_hasil_volume.config(text="Masukkan angka yang valid")
        label_keterangan_volume.config(text="")

def hitung_luas_permukaan():
    try:
        jari_jari = float(entry_jari_jari.get())
        tinggi = float(entry_tinggi.get())
        sisi_miring = math.sqrt(jari_jari**2 + tinggi**2)
        luas_permukaan = math.pi * jari_jari * (jari_jari + sisi_miring)
        label_hasil_luas_permukaan.config(text=f"Luas Permukaan: {luas_permukaan:.2f} (unit persegi)")
        label_keterangan_luas_permukaan.config(text="Hasil perhitungan luas permukaan kerucut:")
    except ValueError:
        label_hasil_luas_permukaan.config(text="Masukkan angka yang valid")
        label_keterangan_luas_permukaan.config(text="")

# Membuat jendela utama
window = tk.Tk()
window.title("Menghitung Luas dan Volume Kerucut")
window.configure(bg='yellow')  # Mengatur warna latar belakang menjadi biru muda

# Membuat label untuk jari-jari kerucut dan tinggi kerucut
label_jari_jari = tk.Label(window, text="Muhamad Farhan 220511046")
label_jari_jari.pack()
label_jari_jari = tk.Label(window, text="Jari-Jari Kerucut:")
label_jari_jari.pack()

# Membuat entry (input) untuk jari-jari kerucut
entry_jari_jari = tk.Entry(window)
entry_jari_jari.pack()

label_tinggi = tk.Label(window, text="Tinggi Kerucut:")
label_tinggi.pack()

# Membuat entry (input) untuk tinggi kerucut
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
