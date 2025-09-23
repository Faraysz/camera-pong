# Implementasi Perceptron dari perhitungan manual

# Fungsi aktivasi step
def activation_function(y_in):
    return 1 if y_in >= 0 else -1

# Fungsi training perceptron
def train_perceptron(data, learning_rate, epochs):
    w1, w2, b = 0, 0, 0  # bobot dan bias awal
    for epoch in range(epochs):
        print(f"\nEpoch {epoch+1}")
        for x1, x2, target in data:
            y_in = w1*x1 + w2*x2 + b
            output = activation_function(y_in)

            # update jika salah
            if output != target:
                w1 = w1 + learning_rate * target * x1
                w2 = w2 + learning_rate * target * x2
                b  = b + learning_rate * target
                print(f"Update -> w1={w1}, w2={w2}, b={b}")
            else:
                print("No update")

    return w1, w2, b

# Fungsi menghitung akurasi
def calculate_accuracy(data, w1, w2, b):
    correct = 0
    for x1, x2, target in data:
        y_in = w1*x1 + w2*x2 + b
        output = activation_function(y_in)
        if output == target:
            correct += 1
    return correct / len(data) * 100

# Data training (dari soal)
train_data = [
    (0, 0, -1),
    (0, 1, -1),
    (1, 0, -1),
    (1, 1,  1)
]

# Data uji (dari soal)
test_data = [
    (0, 1, -1),
    (1, 0, -1),
    (1, 1,  1),
    (0, 0, -1)
]

# Training
final_w1, final_w2, final_b = train_perceptron(train_data, learning_rate=1, epochs=3)

# Hasil akhir
print(f"\nBobot akhir: w1={final_w1}, w2={final_w2}, bias={final_b}")

# Akurasi training
train_acc = calculate_accuracy(train_data, final_w1, final_w2, final_b)
print(f"Akurasi Data Training: {train_acc:.2f}%")

# Akurasi testing
test_acc = calculate_accuracy(test_data, final_w1, final_w2, final_b)
print(f"Akurasi Data Uji: {test_acc:.2f}%")
