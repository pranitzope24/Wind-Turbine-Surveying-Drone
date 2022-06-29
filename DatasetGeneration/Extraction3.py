import cv2
import numpy as np
import os
def make_edges():
  K=1
  for filename in os.listdir('/home/akshat/Downloads/Nordtank 2018'):
    name='/home/akshat/Downloads/Nordtank 2018/'+filename
    STRIN=str(K)
    name1='/home/akshat/Downloads/Extractions/'+STRIN+'.jpg'
    img=cv2.imread(name)
    edges = cv2.Canny(image=img, threshold1=100, threshold2=200)
    cv2.imwrite(name1,edges)
    K+=1
make_edges()