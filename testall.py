import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import segmentation, feature, future
from sklearn.ensemble import RandomForestClassifier
from functools import partial
import joblib
import os
import cv2

path = 'E:/Bill-Codes/17NOV2022/slide3/_color/'
os.mkdir(path+'_masks/')
path2 = path+'_masks/'
x = [item for item in os.listdir(path) if item.endswith('.png')]

sigma_min = 1
sigma_max = 16
features_func = partial(feature.multiscale_basic_features,
                        intensity=True, edges=True, texture=True,
                        sigma_min=sigma_min, sigma_max=sigma_max,
                        channel_axis=-1)
loaded_rf = joblib.load("./random_forest.joblib")

for i in range(len(x)):
    image = skimage.io.imread(path+x[i])
    features = features_func(image)
    result = future.predict_segmenter(features,loaded_rf)

    img = np.zeros(result.shape[:2], dtype=np.uint8)

    indices = np.where(result == [1])
    print(len(indices[0]))
    for j in range(len(indices[0])):
        img[indices[0][j], indices[1][j]] = 255

    cv2.imwrite(path2+x[i].replace('.png','')+'_2.png',img)

    img = np.zeros(result.shape[:2], dtype=np.uint8)

    indices = np.where(result == [2])
    print(len(indices[0]))
    for j in range(len(indices[0])):
        img[indices[0][j], indices[1][j]] = 255

    cv2.imwrite(path2+x[i].replace('.png','')+'_M.png',img)