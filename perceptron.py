import matplotlib.pyplot as plt

# Fungsi aktivasi
def activation_function(y_in):
    """Fungsi aktivasi tiga nilai."""
    if y_in > 0:
        return 1
    elif 0 <= y_in <= 1:
        return 0
    else:
        return -1

# Fungsi training perceptron
def train_perceptron(data, learning_rate, epochs):
    """Melatih perceptron dengan data training."""
    weights = [0, 0]   # w1, w2
    bias = 0

    for epoch in range(epochs):
        print(f"\nEpoch {epoch + 1}")
        for x1, x2, target in data:
            # Hitung input net
            y_in = bias + (weights[0] * x1 + weights[1] * x2)
            # Hitung output
            output = activation_function(y_in)

            # Update bobot dan bias jika terjadi error
            if output != target:
                weights[0] += learning_rate * target * x1
                weights[1] += learning_rate * target * x2
                bias += learning_rate * target
                print(f"Update -> weights: {weights}, bias: {bias}")
            else:
                print("No update")

    return weights, bias

# Fungsi menghitung akurasi
def calculate_accuracy(data, weights, bias):
    """Menghitung akurasi model."""
    correct_predictions = 0
    total_predictions = len(data)

    for x1, x2, target in data:
        y_in = bias + (weights[0] * x1 + weights[1] * x2)
        output = activation_function(y_in)
        if output == target:
            correct_predictions += 1

    accuracy = (correct_predictions / total_predictions) * 100
    return accuracy

# Fungsi prediksi data uji
def predict(weights, bias, test_data):
    """Melakukan prediksi untuk data uji."""
    predictions = []
    for x1, x2 in test_data:
        y_in = bias + (weights[0] * x1 + weights[1] * x2)
        output = activation_function(y_in)
        predictions.append(output)
    return predictions

# Fungsi visualisasi decision boundary
def plot_decision_boundary(data, weights, bias):
    """Visualisasi data dan decision boundary."""
    plt.figure(figsize=(6, 6))
    for x1, x2, target in data:
        if target == 1:
            plt.scatter(x1, x2, color='green', label='Class 1 (1)' if 'Class 1 (1)' not in plt.gca().get_legend_handles_labels()[1] else "")
        else:
            plt.scatter(x1, x2, color='red', label='Class -1 (-1)' if 'Class -1 (-1)' not in plt.gca().get_legend_handles_labels()[1] else "")

    # Garis pemisah (decision boundary)
    x = [-0.5, 1.5]
    if weights[1] != 0:  # hindari pembagian nol
        y = [-(weights[0] * xi + bias) / weights[1] for xi in x]
        plt.plot(x, y, label='Decision Boundary', color='blue')

    # Setting plot
    plt.xlim(-0.5, 1.5)
    plt.ylim(-0.5, 1.5)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('Perceptron Decision Boundary')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.show()

# ==============================
# Main Program
# ==============================

# Data training
data = [
    [0, 0, -1],
    [0, 1, -1],
    [1, 0, -1],
    [1, 1,  1]
]

# Parameter pelatihan
learning_rate = 1
epochs = 3   # sesuai soal

# Melatih perceptron
final_weights, final_bias = train_perceptron(data, learning_rate, epochs)

# Menampilkan bobot dan bias akhir
print(f"\nFinal weights: {final_weights}, Final bias: {final_bias}")

# Menghitung akurasi training
accuracy = calculate_accuracy(data, final_weights, final_bias)
print(f"Akurasi Training: {accuracy:.2f}%")

# Visualisasi hasil
plot_decision_boundary(data, final_weights, final_bias)

# Data uji
test_data = [
    [0, 1],
    [1, 0],
    [1, 1],
    [0, 0]
]

# Prediksi data uji
predictions = predict(final_weights, final_bias, test_data)
print("\nHasil Prediksi Data Uji:")
for i, (x1, x2) in enumerate(test_data):
    print(f"Input ({x1}, {x2}) -> Prediksi: {predictions[i]}")
