import cv2
import numpy
from PIL import Image
from util import get_limits

yellow =[0,255,255] #yellow in BGR colorspace

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsvimage=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerlimit , upperlimit = get_limits(color=yellow)
    mask =cv2.inRange(hsvimage,lowerlimit , upperlimit)
    mask_ =Image.fromarray(mask)

    bbox = mask_.getbbox()
    print(bbox)
    cv2.imshow("frame",mask)

    if cv2.waitKey(1)&0xFF == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()
