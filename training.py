import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import segmentation, feature, future
from sklearn.ensemble import RandomForestClassifier
from functools import partial
import joblib
import os

path_color = 'E:/Bill-Codes/14NOV2022/slide1/_color2/'
path_masks = 'E:/Bill-Codes/14NOV2022/mask2/'


listimg = [item for item in os.listdir(path_color) if item.endswith('.png')]
#listmask = [item for item in os.listdir(path_masks) if item.endswith('.png')]

A = []
B = []

for i in range(len(listimg)):

    image = skimage.io.imread(path_color+listimg[i])
    mask1 = skimage.io.imread(path_masks+listimg[i].replace('.png','')+'_1.png')
    mask2 = skimage.io.imread(path_masks+listimg[i].replace('.png','')+'_2.png')
    mask3 = skimage.io.imread(path_masks+listimg[i].replace('.png','')+'_3.png')
    mask4 = skimage.io.imread(path_masks+listimg[i].replace('.png','')+'_4.png')
    training_labels = np.zeros(image.shape[:2], dtype=np.uint8)

    indices = np.where(mask1 == [255])
    print(len(indices[0]))
    for j in range(len(indices[0])):
        training_labels[indices[0][j], indices[1][i]] = 1
    
    indices = np.where(mask2 == [255])
    print(len(indices[0]))
    for j in range(len(indices[0])):
        training_labels[indices[0][j], indices[1][i]] = 2

    indices = np.where(mask3 == [255])
    print(len(indices[0]))
    for j in range(len(indices[0])):
        training_labels[indices[0][j], indices[1][i]] = 3
    
    indices = np.where(mask4 == [255])
    print(len(indices[0]))
    for j in range(len(indices[0])):
        training_labels[indices[0][j], indices[1][i]] = 4

    sigma_min = 1
    sigma_max = 16
    features_func = partial(feature.multiscale_basic_features,
                        intensity=True, edges=True, texture=True,
                        sigma_min=sigma_min, sigma_max=sigma_max,
                        channel_axis=-1)
    features = features_func(image)
    A.append(features)
    B.append(training_labels)

features = np.vstack(A)
training_labels = np.vstack(B)

clf = RandomForestClassifier(n_estimators=50, n_jobs=-1,
                             max_depth=10, max_samples=0.05)

clf = future.fit_segmenter(training_labels, features, clf)

print(clf)
joblib.dump(clf, "./random_forest.joblib")

