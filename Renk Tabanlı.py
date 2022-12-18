import cv2
import cvzone
import numpy as np
from cvzone.ColorModule import ColorFinder
import pickle
from skimage.measure import label, regionprops

colorFinder= ColorFinder(False)
hmin=78
smin=18
vmin=0
hmax=119
smax=168
vmax=132

HsvVals={'hmin':hmin,  'smin':smin,  'vmin':vmin, 'hmax':hmax,  'smax':smax,  'vmax':vmax}

while True:

    img=cv2.imread('pantolanlu.jpeg')


    imgBlur = cv2.GaussianBlur(img, (7, 7), 2)
    imgColor, mask = colorFinder.update(imgBlur,HsvVals)
    kernel = np.ones((5, 5), np.uint8)
    mask_2 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask_3= cv2.medianBlur(mask_2, 9)
    mask_4= cv2.medianBlur(mask_3, 9)
    mask_5= cv2.medianBlur(mask_4, 9)
    mask_6 = cv2.dilate(mask_5, kernel, iterations=1)
    kernel = np.ones((9, 9), np.uint8)
    mask_7 = cv2.morphologyEx(mask_6, cv2.MORPH_CLOSE, kernel)
    ret, th1 = cv2.threshold(mask_7, 200, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    imgContours, conFound = cvzone.findContours(img, th1, 3500)
    print(conFound)
    bbox=conFound[0]['bbox']


    a = cv2.rectangle(img,bbox, (255, 0, 0), 2)

    print(bbox)

    cv2.imshow('orjisss abi',img)
    cv2.imshow('mask abi',mask)
    cv2.imshow('2 abi',mask_2)
    cv2.imshow('3 abi',mask_3)
    cv2.imshow('4 abi',mask_4)
    cv2.imshow('5 abi',mask_5)
    cv2.imshow('6 abi',mask_6)
    cv2.imshow('7 abi',mask_7)

    cv2.imshow('th1 abi',th1)

    cv2.imshow('orjissssss abi',imgContours)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    cv2.destroyAllWindows()