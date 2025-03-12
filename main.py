import cv2
import pyautogui
import math
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

webcam = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while webcam.isOpened():
        success, img = webcam.read()
        if not success:
            break

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                index_finger = hand_landmarks.landmark[8]
                thumb = hand_landmarks.landmark[4]

                height, width, _ = img.shape
                indexfin_x = int(index_finger.x * width)
                indexfin_y = int(index_finger.y * height)

                thumb_x = int(thumb.x * width)
                thumb_y = int(thumb.y * height)

                cv2.putText(img, f"Index Finger: ({indexfin_x}, {indexfin_y})", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                cv2.circle(img, (indexfin_x, indexfin_y), 10, (255, 0, 0), -1)
                cv2.circle(img, (thumb_x, thumb_y), 10, (255, 0, 0), -1)

                pyautogui.moveTo(1920 - ((1920 / 600) * thumb_x), (1080 / 300) * thumb_y)

                distance_for_click = math.sqrt((indexfin_x - thumb_x)**2 + (indexfin_y - thumb_y)**2)

                if distance_for_click < 35:
                    pyautogui.leftClick()


        cv2.imshow('Hand Tracking', img)
        if cv2.waitKey(5) & 0xFF == ord("q"):
            break

webcam.release()
cv2.destroyAllWindows()
