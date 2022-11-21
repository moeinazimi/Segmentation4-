import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import os 
path = 'E:/Bill-Codes/17NOV2022/slide2/_color/'

#os.mkdir(path+'_maks2/')


x = [item for item in os.listdir(path+'_masks/') if item.endswith('.png')]
print(x)
l = 256
n = 20

for i in range(len(x)):
    im = cv2.imread(path+'_masks/'+x[i], cv2.IMREAD_UNCHANGED)
    im = ndimage.gaussian_filter(im, sigma=l/(4.*n))
    mask = (im > im.mean()).astype(np.float)
    img = mask + 0.3*np.random.randn(*mask.shape)
    binary_img = img > 0.5
    open_img = ndimage.binary_opening(binary_img)
    close_img = ndimage.binary_closing(open_img)
    im = Image.fromarray(close_img)
    im.save(path+'_maks2/'+x[i])


