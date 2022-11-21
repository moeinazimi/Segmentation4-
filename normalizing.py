import numpy as np
import cv2
import os 
from tifffile import imread
from tifffile import imread
from PIL import Image, ImageOps
import os
from matplotlib import pyplot as plt



path_channel = 'E:/Bill-Codes/17NOV2022/slide3/_channel/'

x = [item for item in os.listdir(path_channel) if item.endswith('.tiff')]
path_normal = 'E:/Bill-Codes/17NOV2022/slide3/_normal/'


def normalizing(path1, path2):
    image = cv2.imread(path1, -1)
    #hist_full = cv2.calcHist([image],[0],None,[65535],[0,65535])
    #print(np.argmax(hist_full))
    image_norm = cv2.normalize(image, image, alpha=0,beta=65535, norm_type=cv2.NORM_MINMAX)
    
    return cv2.imwrite(path2+path1.split('/')[-1],image_norm)
    

for i in range(len(x)):
    normalizing(path_channel+x[i],path_normal)
