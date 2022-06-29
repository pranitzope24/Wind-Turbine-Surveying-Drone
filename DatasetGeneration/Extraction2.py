import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import sys
import os
from  PIL  import Image
def pngs():
  k=1
  for filename in os.listdir('/home/akshat/Downloads/Nordtank 2018'):
    name='/home/akshat/Downloads/Nordtank 2018/'+filename
    strin=str(k)
    name1='/home/akshat/Downloads/Extractions/'+strin+'.png'
    img = cv.imread(name, cv.IMREAD_UNCHANGED)
    original = img.copy()
    l = int(max(5, 6))
    u = int(min(6, 6))
    ed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.GaussianBlur(img, (21, 51), 3)
    edges = cv.cvtColor(edges, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(edges, l, u)
    _, thresh = cv.threshold(edges, 0, 255, cv.THRESH_BINARY  + cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    mask = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, iterations=4)
    data = mask.tolist()
    sys.setrecursionlimit(10**8)
    for i in  range(len(data)):
        for j in  range(len(data[i])):
            if data[i][j] !=  255:
                data[i][j] =  -1
            else:
                break
        for j in  range(len(data[i])-1, -1, -1):
            if data[i][j] !=  255:
                data[i][j] =  -1
            else:
                break
    image = np.array(data)
    image[image !=  -1] =  255
    image[image ==  -1] =  0
    mask = np.array(image, np.uint8)
    result = cv.bitwise_and(original, original, mask=mask)
    result[mask ==  0] =  255
    img = result
    img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] ==  255  and item[1] ==  255  and item[2] ==  255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save(name1, "PNG")
    k+=1
def test():
  k=1
  name='/home/akshat/Downloads/Nordtank 2018/'+'DJI_0004.JPG'
  strin=str(k)
  name1='/home/akshat/Downloads/Extractions-2/'+strin+'.png'
  img = cv.imread(name, cv.IMREAD_UNCHANGED)
  original = img.copy()
  l = int(max(5, 6))
  u = int(min(6, 6))
  ed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  edges = cv.GaussianBlurAkshat2002*
  (img, (21, 51), 3)
  edges = cv.cvtColor(edges, cv.COLOR_BGR2GRAY)
  edges = cv.Canny(edges, l, u)
  _, thresh = cv.threshold(edges, 0, 255, cv.THRESH_BINARY  + cv.THRESH_OTSU)
  kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
  mask = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, iterations=4)
  data = mask.tolist()
  sys.setrecursionlimit(10**8)
  for i in  range(len(data)):
      for j in  range(len(data[i])):
          if data[i][j] !=  255:
              data[i][j] =  -1
          else:
              break
      for j in  range(len(data[i])-1, -1, -1):
          if data[i][j] !=  255:
              data[i][j] =  -1
          else:
              break
  image = np.array(data)
  image[image !=  -1] =  255
  image[image ==  -1] =  0
  mask = np.array(image, np.uint8)
  result = cv.bitwise_and(original, original, mask=mask)
  result[mask ==  0] =  255
  img = result
  img=Image.fromarray(img)
  img.convert("RGBA")
  datas = img.getdata()
  newData = []
  for item in datas:
      if item[0] ==  255  and item[1] ==  255  and item[2] ==  255:
          newData.append((255, 255, 255, 0))
      else:
          newData.append(item)
  img.putdata(newData)
  img.save(name1, "PNG")
  k+=1
test()