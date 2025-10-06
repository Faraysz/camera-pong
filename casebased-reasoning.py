# Knowledge Base: Daftar kasus sebelumnya (masa lalu) dengan gejala dan diagnosa
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

# Fungsi untuk menghitung similarity antara gejala baru dan kasus di knowledge base
def calculate_similarity(gejala_baru, gejala_kasus):
    # Hitung berapa banyak gejala yang cocok antara kasus baru dan kasus yang sudah ada
    return len(set(gejala_baru).intersection(set(gejala_kasus)))


# Mesin Inferensi: Case-Based Reasoning
def diagnose_disease(gejala_baru):
    best_match = None
    highest_similarity = 0
    similarities = []

    # Cari kasus dengan gejala yang paling cocok
    for case in knowledge_base:
        similarity = calculate_similarity(gejala_baru, case["gejala"])
        similarities.append((case["diagnosa"], similarity))
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = case

    # Menampilkan nilai similarity
    print("Similarity values for each case:")
    for diagnosa, similarity in similarities:
        print(f"Diagnosa: {diagnosa}, Similarity: {similarity}")

    # Mengembalikan (return) diagnosa yang paling cocok
    if best_match:
        return best_match["diagnosa"]
    else:
        return "Tidak ditemukan kasus yang cocok"


# Input: Gejala kasus baru
gejala_baru = ["mual", "mata kuning", "letih", "pusing"]

# Menjalankan mesin inferensi
diagnosa = diagnose_disease(gejala_baru)

# Output: Mendiagnosis berdasarkan kasus yang paling cocok
print(f"Hasil Diagnosa: {diagnosa}")
