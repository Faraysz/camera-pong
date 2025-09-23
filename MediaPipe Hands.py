# import cv2
# # import mediapipe as mp

# # Inisialisasi MediaPipe
# # mp_hands = mp.solutions.hands
# # mp_draw = mp.solutions.drawing_utils

# # hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# # Buka kamera
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     frame = cv2.flip(frame, 1)  # biar kayak cermin
#     rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Deteksi tangan
#     result = hands.process(rgb)

#     if result.multi_hand_landmarks:
#         for hand_landmarks in result.multi_hand_landmarks:
#             # Gambar titik-titik dan garis tangan
#             mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#             # Ambil koordinat ujung jari telunjuk (landmark 8)
#             h, w, c = frame.shape
#             x = int(hand_landmarks.landmark[8].x * w)
#             y = int(hand_landmarks.landmark[8].y * h)

#             # Gambar lingkaran "player" mengikuti ujung jari
#             cv2.circle(frame, (x, y), 20, (255, 0, 0), -1)

#     cv2.imshow("Hand Tracking Game", frame)

#     if cv2.waitKey(1) & 0xFF == 27:  # ESC keluar
#         break

# cap.release()
# cv2.destroyAllWindows()