import cv2
import os
import numpy as np

path_mask = 'E:/Bill-Codes/14NOV2022/mask/'
path_masks2 = 'E:/Bill-Codes/14NOV2022/mask2/'

x = [item for item in os.listdir(path_mask) if item.endswith('.png')]
print(x)

for i in range(len(x)):
    if x[i].replace('.png','').endswith('_1'):
        img = cv2.imread(path_mask+x[i],cv2.IMREAD_GRAYSCALE)
        h,w = img.shape[:2]
        row = int(h/400)
        col = int(w/400)
        print(row, col)
        for j in range(row):
            print(h*j)
            for k in range(col):
                print(k*w)
                blank_image = np.zeros((400,400), np.uint8)
                blank_image.fill(255)
                blank_image[0:400,0:400] = img[400*j:400*(j+1),400*k:400*(k+1)] 
                cv2.imwrite(path_masks2+x[i].split('_')[0]+'_'+str(j)+'_'+str(k)+'_1.png',blank_image)

for i in range(len(x)):
    if x[i].replace('.png','').endswith('_2'):
        img = cv2.imread(path_mask+x[i],cv2.IMREAD_GRAYSCALE)
        h,w = img.shape[:2]
        row = int(h/400)
        col = int(w/400)
        print(row, col)
        for j in range(row):
            print(h*j)
            for k in range(col):
                print(k*w)
                blank_image = np.zeros((400,400), np.uint8)
                blank_image[0:400,0:400] = img[400*j:400*(j+1),400*k:400*(k+1)] 
                cv2.imwrite(path_masks2+x[i].split('_')[0]+'_'+str(j)+'_'+str(k)+'_2.png',blank_image)
                
                
                
for i in range(len(x)):
    if x[i].replace('.png','').endswith('_3'):
        img = cv2.imread(path_mask+x[i],cv2.IMREAD_GRAYSCALE)
        h,w = img.shape[:2]
        row = int(h/400)
        col = int(w/400)
        print(row, col)
        for j in range(row):
            print(h*j)
            for k in range(col):
                print(k*w)
                blank_image = np.zeros((400,400), np.uint8)
                blank_image[0:400,0:400] = img[400*j:400*(j+1),400*k:400*(k+1)] 
                cv2.imwrite(path_masks2+x[i].split('_')[0]+'_'+str(j)+'_'+str(k)+'_3.png',blank_image)
                
                
                
for i in range(len(x)):
    if x[i].replace('.png','').endswith('_4'):
        img = cv2.imread(path_mask+x[i],cv2.IMREAD_GRAYSCALE)
        h,w = img.shape[:2]
        row = int(h/400)
        col = int(w/400)
        print(row, col)
        for j in range(row):
            print(h*j)
            for k in range(col):
                print(k*w)
                blank_image = np.zeros((400,400), np.uint8)
                blank_image[0:400,0:400] = img[400*j:400*(j+1),400*k:400*(k+1)] 
                cv2.imwrite(path_masks2+x[i].split('_')[0]+'_'+str(j)+'_'+str(k)+'_4.png',blank_image)