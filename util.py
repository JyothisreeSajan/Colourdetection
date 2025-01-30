import numpy as np
import cv2


def get_limits(color):
    c =np.uint8([[color]])#here insert the bgr value which you want to convert to hsv
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerlimit = hsvC[0][0][0] - 5,135,135
    upperlimit = hsvC[0][0][0] + 5,255,255

    lowerlimit = np.array(lowerlimit, dtype=np.uint8)
    upperlimit = np.array(upperlimit, dtype=np.uint8)
    print(lowerlimit,upperlimit)

    return lowerlimit, upperlimit