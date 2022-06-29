import os
import cv2 
k=1
for filename in os.listdir('/home/akshat/Downloads/Nordtank 2018/'):
    name1='/home/akshat/Downloads/Nordtank 2018/'+filename
    img=cv2.imread(name1)
    cv2.resize(img,(512,512))
    st=str(k)
    cv2.imwrite('/home/akshat/Downloads/Dump/'+st+'.jpg',img)
    k+=1