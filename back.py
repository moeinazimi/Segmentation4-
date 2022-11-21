import cv2
import os
import numpy as np

path_mask = 'E:/Bill-Codes/14NOV2022/mask/'

x = [item for item in os.listdir(path_mask) if item.endswith('.png')]
print(x)

A = []

for i in range(len(x)):
    if i%3 ==0:
        A.append(x[i].split('_')[0])
        
for i in range(len(A)):
    im1 = cv2.imread(path_mask+A[i]+'_1.png',0)
    im2 = cv2.imread(path_mask+A[i]+'_2.png',0)
    im3 = cv2.imread(path_mask+A[i]+'_3.png',0)
    im4 = cv2.bitwise_or(im1, im2)
    im5 = cv2.bitwise_or(im4, im3)
    im6 = cv2.bitwise_not(im5)
    cv2.imwrite(path_mask+A[i]+'_4.png',im6)