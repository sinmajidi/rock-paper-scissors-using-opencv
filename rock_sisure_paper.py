import cv2
import HandTrackingModule as htm
wCam, hCam = 1280, 720

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(3, wCam)
cap.set(4, hCam)



pTime = 0

detector = htm.HandDetector(detectionCon=0.75)

tipIds = (4, 8, 12, 16, 20)

while True:

    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        fingers = []

        # Thumb
        if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
    #
    #     # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        totalFingers = fingers.count(1)
        if totalFingers==4 or totalFingers==5:
            cv2.putText(img, "paper", (45, 375), cv2.FONT_HERSHEY_PLAIN,
                        5, (0, 0, 255), 5)
        if totalFingers==2 or totalFingers==3 :
            cv2.putText(img, "scissor", (45, 375), cv2.FONT_HERSHEY_PLAIN,
                        5, (0, 0, 255), 5)
        if totalFingers==0 or totalFingers==1:
            cv2.putText(img, "rock", (45, 375), cv2.FONT_HERSHEY_PLAIN,
                        5, (0, 0, 255), 5)



    cv2.imshow("Image", img)
    cv2.waitKey(1)