import cv2
import cvzone
import numpy as np
from cvzone.ColorModule import ColorFinder
import pickle


video=cv2.VideoCapture(0)

cornerPoints=[[35,25],[61,45],[50,35],[48,50]]
#
#
colorFinder= ColorFinder(True)
HsvVals={'hmin':59,  'smin':42,  'vmin':0, 'hmax':119,  'smax':166,  'vmax':101}
def getBoard(img):

    width, height=int(400*1.5),int(380*1.5)
    pts1=np.float32(cornerPoints)
    pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix=cv2.getPerspectiveTransform(pts1,pts2)
    imgOutput =cv2.warpPerspective(img,matrix,(width,height))
    return imgOutput



while True:
    # success, img=video.read()
    img=cv2.imread('pantolanlu.jpeg')
    # getBoard(img)
    imgColor, mask = colorFinder.update(img)

    cv2.imshow("image",img)
    cv2.imshow("image color",imgColor)
    cv2.waitKey(1)
