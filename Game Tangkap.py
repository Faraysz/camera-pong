import cv2
import numpy as np

# Buka kamera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Balik kamera biar kayak cermin
    frame = cv2.flip(frame, 1)

    # Konversi ke HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Range warna merah (bisa ganti sesuai objek)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Cari kontur objek merah
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        area = cv2.contourArea(c)
        if area > 1000:  # biar ga nangkep noise kecil
            x, y, w, h = cv2.boundingRect(c)
            # Gambar kotak di objek
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

            # “Game”: gambar lingkaran sebagai player
            cv2.circle(frame, (x + w//2, y + h//2), 30, (255, 0, 0), -1)

    # Tampilkan hasil
    cv2.imshow("Game Vision", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # tekan ESC buat keluar
        break

cap.release()
cv2.destroyAllWindows()
