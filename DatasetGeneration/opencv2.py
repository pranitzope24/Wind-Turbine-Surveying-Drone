import cv2 
import numpy as np
import os
import random
def Whiteness(pixel,specificity,brightness): #Interim
  if len(pixel)!=3:
    return False
  if pixel[0]>=brightness and pixel[1]>=brightness and pixel[2]>=brightness:
    avg=(pixel[1]+pixel[2]+pixel[0])/3
    k=0
    m=0
    while(k<3):
      if pixel[k]-avg>=specificity or avg-pixel[k]>=specificity:
        pass
      else:
        m+=1
      k+=1
    if(m<3):
      return False
    else:
      return True
  else:
    return False
def blackness(pixel,specificity,brightness): #Interim
  if len(pixel)!=3:
    return False
  if pixel[0]<=brightness and pixel[1]<=brightness and pixel[2]<=brightness:
    avg=(pixel[1]+pixel[2]+pixel[0])/3
    k=0
    m=0
    while(k<3):
      if pixel[k]-avg>=specificity or avg-pixel[k]>=specificity:
        pass
      else:
        m+=1
      k+=1
    if(m<3):
      return False
    else:
      return True
  else:
    return False
def rotate_image(image, angle):      #Tested
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result
def merge_image(uploaded,uploaded2,length,width,weight1,weight2):     #Tested
  #Weight has to lie between 0 and 1
  image2=cv2.resize(uploaded2,(length,width))
  image1=cv2.resize(uploaded,(length,width))
  result = cv2.addWeighted(image1, weight1, image2, weight2, 0)
  return result
def switch_colour(imageup,length_int,width_int,colour1_list,colour2_list):      #Tested
  image=cv2.resize(imageup,(length_int,width_int))
  for x in range(1,length_int):
    for y in range(1,width_int):
      px=image[x,y]
      if np.array_equiv(px,colour1_list): #You can use a different coordinate here. Insert the colour YOU WANT TO REPLACE
        image[x,y]=colour2_list   #Here, insert the colour YOU WANT TO REPLACE WITH
  return image
def merge_with_bg(image): #Merges the image with a random background    Tested
  image=cv2.resize(image,(256,256))
  imgs=[]
  for filename in os.listdir('/home/akshat/Downloads/uncracked'):
    if filename is not None:
      imgs.append(filename)
  number=len(imgs)
  n=random.randint(0,number-1)
  img_name='/home/akshat/Downloads/uncracked/'+imgs[n]
  img=cv2.imread(img_name)
  img=cv2.resize(img,(256,256))
  for x in range(1,256):
    for y in range(1,256):
      if Whiteness(image[x,y],15,170) or np.array_equiv(image[x,y],[0,0,0]) or blackness(image[x,y],40,50):
        image[x,y]=img[x,y]
  return image
def MakeData():
  decals=[]
  k=1
  for filename in os.listdir('/home/akshat/Downloads/Damage'):
    name1='/home/akshat/Downloads/Damage/'+filename
    img=cv2.imread(name1)
    #if img==None:
    #  print('No_Read')
    #  break
    
    for x in range(0,8):
      img=rotate_image(img,random.randint(0,360))
      img2=merge_with_bg(img)
      img3=cv2.resize(img,(256,256))
      img2=cv2.addWeighted(img2, 0.7, img3, 0.3, 0)
      strin=str(k)
      name='/home/akshat/Downloads/Corrosion_Damage/'+strin+'.jpg'
      cv2.imwrite(name,img2)
      k+=1
      #img2=merge_with_bg(img)
      #img3=cv2.resize(img,(256,256))
      #img2=cv2.addWeighted(img2, 0.7, img3, 0.3, 0)
      #strin=str(k)
      #name='/home/akshat/Downloads/Corrosion_Damage/'+strin+'.jpg'
      #cv2.imwrite(name,img2)
      #k+=1
MakeData()

