from tifffile import imread, imwrite
import numpy as np
import cv2
import os

path_normal = 'E:/Bill-Codes/17NOV2022/slide3/_normal/'

x = [item for item in os.listdir(path_normal) if item.endswith('.tiff')]

path_color = 'E:/Bill-Codes/17NOV2022/slide3/_color/'

A = []
for i in range(len(x)):
    if i%4 == 0:
        A.append(x[i].split('$')[0])

print(A)  
  

for i in range(len(A)):
    r_np = np.array(cv2.imread(path_normal+A[i]+'$red.tiff', 0))
    r_np = cv2.equalizeHist(r_np)

    b_np = np.array(cv2.imread(path_normal+A[i]+'$blue.tiff', 0))
    b_np = cv2.equalizeHist(b_np)

    g_np = np.array(cv2.imread(path_normal+A[i]+'$yellow.tiff', 0))
    g_np = cv2.equalizeHist(g_np)

    final_img = (np.dstack([b_np, g_np, r_np])).astype(np.uint8)
    
    cv2.imwrite(path_color+A[i]+'.png', final_img)
