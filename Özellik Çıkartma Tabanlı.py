import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb

x=0
y=0
r=0
t=0
video=cv2.VideoCapture(0)


while (True):
    # ret, video_2 = video.read()
    video_2=cv2.imread('pantolanlu.jpeg')

    hsv=cv2.cvtColor(video_2,cv2.COLOR_BGR2HSV)
    up_color=np.array([120,120,120])
    down_color=np.array([50,50,50])
    mask_1=cv2.inRange(hsv,down_color,up_color)

    im_floodfill = mask_1.copy()
    h, w = video_2.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    cv2.floodFill(im_floodfill, mask, (5,5), 255);
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    im_out = mask_1 | im_floodfill_inv

    cleared = clear_border(im_out)

    ret,th1 = cv2.threshold(cleared,200,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    label_image = label(th1)
    # image_label_overlay = label2rgb(label_image, image=video_2, bg_label=0)
    #    fig, ax = plt.subplots(figsize=(10, 6))
    #ax.imshow(image_label_overlay)
    for region in regionprops(label_image):
        if region.area >= 1500:
        # draw rectangle around segmented coins
            x, y, w, h = region.bbox
            a = cv2.rectangle(video_2, (x, y), (x+r,y+t), (255, 0, 0), 2)
    print('x abi',x)
    print("y abi",y)
    print("x+w abi",x+r)
    print("y+h abi",y+t)
    for region in regionprops(label_image):
        if region.area <1500 :
            x = 0
            y = 0
            w = 0
            h = 0


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow('orji abi',video_2)
    cv2.imshow('uyuy abi',mask_1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
# After the loop release the cap object
video.release()
# Destroy all the windows
cv2.destroyAllWindows()