import cv2
import time
import cvzone
import random
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=1)

timer=0
stateResult=False
startGame = False
scores=[0,0]
flag=0
x=-1
cap = cv2.VideoCapture(0)
while True:
    imgBG = cv2.imread("Resources/BG.png")
    success, img = cap.read()
    imgsized = cv2.resize(img, (396, 420))

    hands, img = detector.findHands(imgsized)
    if startGame:
        if stateResult is False:
            timer=time.time()-initialtime
            cv2.putText(imgBG, str(int(timer)), (600,435),cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
            if timer>2:
                stateResult=True
                if hands:
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    if fingers==[0,1,0,0,0]:
                        playermove=1
                    if fingers==[0,1,1,0,0]:
                        playermove=2
                    if fingers==[1,0,1,1,1]:
                        playermove=3
                    if fingers==[0,1,1,1,1]:
                        playermove=4
                    if fingers==[1,1,1,1,1]:
                        playermove=5
                    print(playermove)
                    randomNum=random.randint(1,5)
                    imgAI = cv2.imread(f'Resources/{randomNum}.jpg')
                    imgBG[234:654,92:488]=imgAI

                    if(flag==0):
                        if ((playermove == 1 and randomNum == 1) or (playermove == 2 and randomNum == 2) or (playermove == 3 and randomNum == 3) or (playermove == 4 and randomNum == 4) or (playermove == 5 and randomNum == 5)):
                            target=scores[0]
                            flag=1
                        else:
                            scores[0]+=playermove
                    elif(flag==1):
                        if ((playermove == 1 and randomNum == 1) or (playermove == 2 and randomNum == 2) or (playermove == 3 and randomNum == 3) or (playermove == 4 and randomNum == 4) or (playermove == 5 and randomNum == 5)):
                            x=0
                        else:
                            scores[1]+=randomNum
                            if(scores[1]>target):
                                x=1


    imgBG[233:653, 796:1192] = imgsized
    if stateResult:
        imgBG[234:654,92:488]=imgAI
    if(flag==1):
        cv2.putText(imgBG, "Target="+str(target+1), (560, 173), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 4)
    cv2.putText(imgBG, str(scores[1]), (400, 213), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(scores[0]), (1108, 213), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    if(x==1):
        cv2.putText(imgBG, "AI wins" , (140, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 4)
    if(x==0):
        cv2.putText(imgBG, "Player wins by " + str((target + 1)-scores[1]-1)+" runs", (840, 90), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 4)


    cv2.imshow('Bg',imgBG)
    key=cv2.waitKey(1)
    if(key==ord('s')):
        initialtime=time.time()
        startGame=True
        stateResult=False