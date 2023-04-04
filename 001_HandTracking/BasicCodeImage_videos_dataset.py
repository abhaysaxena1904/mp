import cv2
import mediapipe as mp
import time


mpHands = mp.solutions.hands
hands = mpHands.Hands() # Default settings - False, 2, 0.5, 0. 5
mpDraw = mp.solutions.drawing_utils

path = "C:\Users\admin\Desktop\MSDS\Codes\20220812_081726.jpg"
img = cv2.imread(path)

imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = hands.process(imgRGB)
if results.multi_hand_landmarks:
    for handLms in results.multi_hand_landmarks:
        for id, lm in enumerate(handLms.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)
            if id == 4:
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
    
    mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

cv2.imshow("Image", img)
