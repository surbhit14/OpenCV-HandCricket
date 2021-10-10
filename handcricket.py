import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import cv2
import random

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector =HandDetector(detectionCon=0.8, maxHands=1)
score=0
x=0
txt=0
while True:
    # Get image frame
    success, img = cap.read()

    # Find the hand and its landmarks
    
    k = cv2.waitKey(33)
    print(k)
    if k==27:
        break    # Esc key to stop
        
    elif k==-1:
        cv2.putText(img,str(txt), (200,200),cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
        cv2.putText(img,str(x), (400,200),cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
        if(x==txt and x!=0):
            cv2.putText(img,'Out', (600,400), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
            cv2.putText(img,str(score), (800,600),cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)       
            score=0
        else:
            cv2.putText(img,str(score), (800,600),cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
         
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        continue

    else:
        img = detector.findHands(img)
        lmList, bboxInfo = detector.findPosition(img)
        if lmList:
            bbox = bboxInfo['bbox']
            fingers=detector.fingersUp()

            if fingers==[0,1,0,0,0]:
                txt=1
            if fingers==[0,1,1,0,0]:
                txt=2
            if fingers==[0,1,1,1,0]:
                txt=3
            if fingers==[0,1,1,1,1]:
                txt=4
            if fingers==[1,1,1,1,1]:
                txt=5
            if fingers==[1,0,0,0,0]:
                txt=6
            x=random.randint(1,6)
            score=score+txt
   

    cv2.imshow("Image", img)    
    cv2.waitKey(1)



    
cap.release()
cv2.destroyAllWindows()

