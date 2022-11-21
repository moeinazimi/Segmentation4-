import cv2
import os
import numpy as np

path_color = 'E:/Bill-Codes/14NOV2022/slide1/_color/'
path_normal2 = 'E:/Bill-Codes/14NOV2022/slide1/_color2/'

x = [item for item in os.listdir(path_color) if item.endswith('.png')]
print(x)


for i in range(len(x)):
    img = cv2.imread(path_color+x[i])
    h,w = img.shape[:2]
    row = int(h/400)
    col = int(w/400)
    print(row, col)
    for j in range(row):
        print(h*j)
        for k in range(col):
                print(k*w)
                blank_image = np.zeros((400,400,3), np.uint8)
                blank_image.fill(255)
                blank_image[0:400,0:400] = img[400*j:400*(j+1),400*k:400*(k+1)] 
                cv2.imwrite(path_normal2+x[i].replace('.png','')+'_'+str(j)+'_'+str(k)+'.png',blank_image)
