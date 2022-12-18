import cv2
import numpy as np
import os

path = 'ImagesQuery'
orb = cv2.ORB_create(nfeatures=1000)

#### Import Images
images = []
classNames = []
myList = os.listdir(path)
print('Total Classes Detected', len(myList))
for cl in myList:
    imgCur = cv2.imread(f'{path}/{cl}', 0)
    images.append(imgCur)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findDes(images):
    desList = []
    for img in images:
        kp, des = orb.detectAndCompute(img, None)
        desList.append(des)
    return desList


def findID(img, desList, thres=15):
    kp2, des2 = orb.detectAndCompute(img, None)
    bf = cv2.BFMatcher()
    matchList = []
    finalVal = -1
    try:
        for des in desList:
            matches = bf.knnMatch(des, des2, k=2)
            good = []
            for m, n in matches:
                if m.distance < 0.75 * n.distance:
                    good.append([m])
            matchList.append(len(good))
    except:
        pass
    # print(matchList)
    if len(matchList) != 0:
        if max(matchList) > thres:
            finalVal = matchList.index(max(matchList))
    return finalVal


desList = findDes(images)
print(len(desList))

cap = cv2.VideoCapture(1)

while True:

    success, img2 = cap.read()
    imgOriginal = img2.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    id = findID(img2, desList)
    print(id)
    if -1< id < 200:
        #cv2.putText(imgOriginal, classNames[id], (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
        cv2.putText(imgOriginal,"yayalı",(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)
    elif 200< id <400:
        cv2.putText(imgOriginal, "30", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
    elif 400<id <600:
        cv2.putText(imgOriginal, "50", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
    elif 600 < id < 800:
        cv2.putText(imgOriginal, "demir yolu ", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
    elif 800<id <1000:
        cv2.putText(imgOriginal, "bisiklet", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
    cv2.imshow('img2', imgOriginal)
    cv2.waitKey(1)