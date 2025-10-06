import tkinter as tk
from tkinter import messagebox

# ===============================
# KNOWLEDGE BASE
# ===============================
knowledge_base = [
    {
        "id": 1,
        "gejala": ["demam", "batuk", "sakit tenggorokan", "letih"],
        "diagnosa": "Flu"
    },
    {
        "id": 2,
        "gejala": ["demam", "sakit kepala", "nyeri otot", "ruam"],
        "diagnosa": "Demam Berdarah"
    },
    {
        "id": 3,
        "gejala": ["demam", "menggigil", "berkeringat", "mual"],
        "diagnosa": "Malaria"
    },
    {
        "id": 4,
        "gejala": ["demam", "mual", "mata kuning", "pusing"],
        "diagnosa": "Hepatitis"
    }
]

# ===============================
# FUNGSI PERHITUNGAN SIMILARITY
# ===============================
def calculate_similarity(gejala_baru, gejala_kasus):
    return len(set(gejala_baru).intersection(set(gejala_kasus)))

# ===============================
# MESIN INFERENSI CBR
# ===============================
def diagnose_disease(gejala_baru):
    best_match = None
    highest_similarity = 0

    for case in knowledge_base:
        similarity = calculate_similarity(gejala_baru, case["gejala"])
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = case

    if best_match:
        return best_match["diagnosa"]
    else:
        return "Tidak ditemukan kasus yang cocok"

# ===============================
# FUNGSI SAAT TOMBOL DIKLIK
# ===============================
def proses_diagnosa():
    gejala_baru = []
    for nama_gejala, var in daftar_gejala.items():
        if var.get() == 1:
            gejala_baru.append(nama_gejala)

    if not gejala_baru:
        messagebox.showwarning("Peringatan", "Silakan pilih minimal satu gejala!")
        return

    hasil = diagnose_disease(gejala_baru)
    result_label.config(text=f"Hasil Diagnosa: {hasil}")

# ===============================
# MEMBUAT GUI TKINTER
# ===============================
window = tk.Tk()
window.title("Sistem Pakar CBR Diagnosis Penyakit")
window.geometry("400x600")
window.configure(bg="#e6e6e6")

judul = tk.Label(window, text="Pilih Gejala yang Dialami:", bg="#e6e6e6", font=("Arial", 12, "bold"))
judul.pack(pady=10)

# Daftar gejala yang bisa dipilih (checkbox)
daftar_gejala = {}
nama_gejala_list = [
    "demam", "batuk", "sakit tenggorokan", "letih",
    "sakit kepala", "nyeri otot", "ruam",
    "menggigil", "berkeringat", "mual",
    "mata kuning", "pusing"
]

for gejala in nama_gejala_list:
    var = tk.IntVar()
    daftar_gejala[gejala] = var
    cb = tk.Checkbutton(window, text=gejala.capitalize(), variable=var, bg="#e6e6e6", anchor="w")
    cb.pack(padx=20, anchor="w")

# Tombol Diagnosa
btn_diagnosa = tk.Button(window, text="Diagnosa", command=proses_diagnosa, bg="#4CAF50", fg="white", width=20)
btn_diagnosa.pack(pady=15)

# Label hasil
result_label = tk.Label(window, text="Hasil Diagnosa akan muncul di sini", bg="#ffffff", width=40, height=3)
result_label.pack(pady=15)

# Jalankan aplikasi
window.mainloop()
