import os
import cv2
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import os 
'''
path = 'E:/Bill-Codes/17NOV2022/slide1/_color/_maks2/_final/'
x = [item for item in os.listdir(path) if item.endswith('.png')]

A = []
for i in range(len(x)):
    if i%3 == 0:
        A.append(x[i].split('_')[0])

for i in range(len(A)):
    blue = cv2.imread(path+A[i]+'_1.png')
    red = cv2.imread(path+A[i]+'_3.png')
    merge = cv2.bitwise_or(red, blue)

    cv2.imwrite(path+A[i]+'_M.png', merge)
'''

im = cv2.imread('005_3.png', 0)
im2 = cv2.imread('_M.png', 0)

'''
im = ndimage.gaussian_filter(yellow, sigma=l/(4.*n))
mask = (im > im.mean()).astype(np.float)
img = mask + 0.3*np.random.randn(*mask.shape)
binary_img = img > 0.5
open_img = ndimage.binary_opening(binary_img)
close_img = ndimage.binary_closing(open_img)
im = Image.fromarray(close_img)
im.save(path+'005_3.png')
'''

merge2 = cv2.bitwise_and(im, im2)
merge3 = cv2.bitwise_xor(im2, merge2)
cv2.imwrite('005_L.png', merge3)