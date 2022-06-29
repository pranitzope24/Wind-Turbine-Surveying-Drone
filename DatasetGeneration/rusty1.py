import numpy as np
import cv2
img=cv2.imread('rust1.png',cv2.IMREAD_UNCHANGED)
img2=cv2.resize(img,(300,300))
print(img2)