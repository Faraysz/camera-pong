import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data Alternatif dan Kriteria
alternatives = ['A1', 'A2', 'A3']
criteria = ['C1 (Benefit)', 'C2 (Cost)', 'C3 (Benefit)']
weights = np.array([0.4, 0.35, 0.25])   # bobot tiap kriteria

# Matriks Keputusan
X = np.array([
    [200, 300, 250],
    [100, 400, 150],
    [150, 350, 200]
])

# Fungsi Normalisasi
def normalize(X, benefit_criteria):
    R = np.zeros_like(X, dtype=float)
    for j in range(X.shape[1]):     # per kolom (kriteria)
        if benefit_criteria[j]:
            R[:, j] = X[:, j] / np.max(X[:, j])     # normalisasi benefit
        else:
            R[:, j] = np.min(X[:, j]) / X[:, j]     # normalisasi cost
    return R

# Normalisasi
benefit_criteria = [True, False, True]   # C1 benefit, C2 cost, C3 benefit
R = normalize(X, benefit_criteria)

# Menghitung nilai preferensi
V = np.dot(R, weights)

# Membuat DataFrame untuk menampilkan hasil
df = pd.DataFrame(R, index=alternatives, columns=criteria)
df['Preferensi'] = V

# Menampilkan tabel hasil
print("Matriks Normalisasi dan Nilai Preferensi:")
print(df)

# Visualisasi Hasil Preferensi
plt.bar(alternatives, V, color=['blue', 'green', 'red'])
plt.xlabel('Alternatif')
plt.ylabel('Nilai Preferensi')
plt.title('Hasil SAW (Simple Additive Weighting)')
plt.show()
