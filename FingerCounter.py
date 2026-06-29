import cv2
import mediapipe as mp
import time
import os
import HandTrackingModule as htm

wCam,hCam=640,480

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

overlayList=[]
myList=os.listdir("Fingers")

for imPath in myList:
    image=cv2.imread(f"Fingers/{imPath}")
    image=cv2.resize(image,(150,150))
    overlayList.append(image)

pTime=0
detector=htm.HandDetector()
tipIds=[4,8,12,16,20]

while True:
    success,img=cap.read()
    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)

    if len(lmList)!=0:
        fingers=[]

        if lmList[3][1]<lmList[20][1]:
            if lmList[tipIds[0]][1]>lmList[tipIds[0]-1][1]:
                fingers.append(0)
            else:
                fingers.append(1)
        else :
            if lmList[tipIds[0]][1]>lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        for id in range(1,5):
            if lmList[tipIds[id]][2]<lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalFingers=fingers.count(1)

        h,w,c=overlayList[totalFingers].shape
        img[0:h,0:w]=overlayList[totalFingers]

        cv2.rectangle(img,(20,225),(170,425),(0,255,0),cv2.FILLED)
        cv2.putText(img,str(totalFingers),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(25,45,0),20)

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,f'FPS:{int(fps)}',(450,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

    cv2.imshow("Finger Counter",img)

    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()