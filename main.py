import cv2
import numpy as np
import random

# Setup kamera
cap = cv2.VideoCapture(0)
width, height = 640, 480

# Bola
ball_x, ball_y = width // 2, height // 2
ball_dx, ball_dy = 5, 5
ball_radius = 15

# Paddle
paddle_x, paddle_y = 50, height // 2
paddle_w, paddle_h = 20, 100
score = 0

# Rentang warna untuk deteksi paddle (misalnya biru)
lower_color = np.array([100, 150, 0])   # HSV lower
upper_color = np.array([140, 255, 255]) # HSV upper

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Masking warna biru
    mask = cv2.inRange(hsv, lower_color, upper_color)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Deteksi paddle berdasarkan objek warna
    if contours:
        c = max(contours, key=cv2.contourArea)
        (x, y, w, h) = cv2.boundingRect(c)
        paddle_y = y + h//2 - paddle_h//2
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  # kotak deteksi

    # Update posisi bola
    ball_x += ball_dx
    ball_y += ball_dy

    # Pantulan atas bawah
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= height:
        ball_dy *= -1

    # Pantulan paddle
    if (paddle_x < ball_x - ball_radius < paddle_x + paddle_w) and \
       (paddle_y < ball_y < paddle_y + paddle_h):
        ball_dx *= -1
        score += 1

    # Reset jika bola keluar kiri
    if ball_x - ball_radius <= 0:
        score = 0
        ball_x, ball_y = width // 2, height // 2
        ball_dx = random.choice([5, -5])
        ball_dy = random.choice([5, -5])

    # Pantulan kanan
    if ball_x + ball_radius >= width:
        ball_dx *= -1

    # Gambar paddle
    cv2.rectangle(frame, (paddle_x, paddle_y),
                  (paddle_x + paddle_w, paddle_y + paddle_h),
                  (0, 255, 0), -1)

    # Gambar bola
    cv2.circle(frame, (ball_x, ball_y), ball_radius, (0, 0, 255), -1)

    # Gambar skor
    cv2.putText(frame, f"Score: {score}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Camera Pong", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC untuk keluar
        break

cap.release()
cv2.destroyAllWindows()
