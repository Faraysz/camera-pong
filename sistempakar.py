import tkinter as tk
from tkinter import messagebox

# Fungsi untuk mendiagnosis penyakit berdasarkan gejala yang dipilih
def diagnose():
    # Mengambil status dari checkbox gejala
    gejala_menguning = var_daun_menguning.get()
    gejala_bintik_coklat = var_bintik_coklat.get()
    gejala_berlubang = var_daun_berlubang.get()
    gejala_tepi_kering = var_tepi_kering.get()
    gejala_keriting = var_daun_keriting.get()
    gejala_kutu_putih = var_kutu_putih.get()
    gejala_batang_busuk = var_batang_busuk.get()
    gejala_layu = var_tanaman_layu.get()

    # Diagnosis berdasarkan gejala yang dipilih
    if gejala_menguning and gejala_bintik_coklat:
        hasil = "Kemungkinan penyakit: Hawar Daun"
    elif gejala_berlubang and gejala_tepi_kering:
        hasil = "Kemungkinan penyakit: Ulat Grayak"
    elif gejala_keriting and gejala_kutu_putih:
        hasil = "Kemungkinan penyakit: Kutu Daun"
    elif gejala_batang_busuk and gejala_layu:
        hasil = "Kemungkinan penyakit: Busuk Batang"
    else:
        hasil = "Gejala tidak sesuai dengan aturan yang ada."

    result_label.config(text=hasil)
    # messagebox.showinfo("Hasil Diagnosis", hasil)

# ==============================
# Membuat window utama
# ==============================
window = tk.Tk()
window.title("Sistem Pakar Diagnosis Penyakit Tanaman")
window.geometry("400x550")
window.configure(bg="#d3d3d3")

# Label petunjuk
label_gejala = tk.Label(window, text="Pilih Gejala:", bg="#c3c3c3")
label_gejala.pack(pady=10)

# Variabel untuk menyimpan status checkbox (0 atau 1)
var_daun_menguning = tk.IntVar()
var_bintik_coklat = tk.IntVar()
var_daun_berlubang = tk.IntVar()
var_tepi_kering = tk.IntVar()
var_daun_keriting = tk.IntVar()
var_kutu_putih = tk.IntVar()
var_batang_busuk = tk.IntVar()
var_tanaman_layu = tk.IntVar()

# Checkbox untuk setiap gejala
check_daun_menguning = tk.Checkbutton(window, text="Daun Menguning", variable=var_daun_menguning, bg="#c3c3c3")
check_daun_menguning.pack(padx=10, anchor='w')

check_bintik_coklat = tk.Checkbutton(window, text="Bintik Coklat", variable=var_bintik_coklat, bg="#c3c3c3")
check_bintik_coklat.pack(padx=10, anchor='w')

check_daun_berlubang = tk.Checkbutton(window, text="Daun Berlubang", variable=var_daun_berlubang, bg="#c3c3c3")
check_daun_berlubang.pack(padx=10, anchor='w')

check_tepi_kering = tk.Checkbutton(window, text="Tepi Daun Kering", variable=var_tepi_kering, bg="#c3c3c3")
check_tepi_kering.pack(padx=10, anchor='w')

check_daun_keriting = tk.Checkbutton(window, text="Daun Keriting", variable=var_daun_keriting, bg="#c3c3c3")
check_daun_keriting.pack(padx=10, anchor='w')

check_kutu_putih = tk.Checkbutton(window, text="Kutu Putih", variable=var_kutu_putih, bg="#c3c3c3")
check_kutu_putih.pack(padx=10, anchor='w')

check_batang_busuk = tk.Checkbutton(window, text="Batang Busuk", variable=var_batang_busuk, bg="#c3c3c3")
check_batang_busuk.pack(padx=10, anchor='w')

check_tanaman_layu = tk.Checkbutton(window, text="Tanaman Layu", variable=var_tanaman_layu, bg="#c3c3c3")
check_tanaman_layu.pack(padx=10, anchor='w')

# Label hasil diagnosis
result_label = tk.Label(window, text="Hasil Diagnosis", bg="#ffffff")
result_label.pack(pady=10)

# Tombol untuk mendiagnosis penyakit
btn_diagnose = tk.Button(window, text="Diagnosa", command=diagnose, bg="#ffffff")
btn_diagnose.pack(pady=10)

# Menjalankan aplikasi
window.mainloop()
