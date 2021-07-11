import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640) # putini ayarla
cap.set(4,480) # yükseklik ayarla
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, +1) # Gamera Çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    
    k = cv2.waitKey(30)
    if k == 27: # cıkmak için ESC bas
        break
cap.release()
cv2.destroyAllWindows()
