
import cv2
import numpy as np

# Read the original image
img = cv2.imread('/home/akshat/Downloads/Nordtank 2018/DJI_0421.JPG')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
# Sobel Edge Detection
#sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis

#sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis

#sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection

# Display Sobel Edge Detection Images
#cv2.imshow('Sobel X', sobelx)
#cv2.waitKey(0)
#cv2.imshow('Sobel Y', sobely)
#cv2.waitKey(0)
#cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
#cv2.waitKey(0)
# Canny Edge Detection
edges = cv2.Canny(image=img, threshold1=100, threshold2=200) # Canny Edge Detection
# Display Canny Edge Detection Image
cv2.imwrite('/home/akshat/Downloads/Extractions/1.jpg',edges)
cv2.destroyAllWindows()
