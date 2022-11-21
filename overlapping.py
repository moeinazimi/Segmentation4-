import os
import cv2

path = 'E:/Bill-Codes/17NOV2022/slide2/_color/_maks2/'
x = [item for item in os.listdir(path) if item.endswith('.png')]
os.mkdir(path+'_final/')


A = []
for i in range(len(x)):
    if i%2 == 0:
        A.append(x[i].split('_')[0])

for i in range(len(A)):

    yellow = cv2.imread(path+A[i]+'_1.png')
    red_merged = cv2.imread(path+A[i]+'_3.png')

    #blue 
    red_merged1 = cv2.bitwise_and(red_merged, yellow)
    red_merged2 = cv2.bitwise_xor(red_merged1, red_merged)
    cv2.imwrite(path+'_final/'+A[i]+'_M.png', red_merged2)
    #yellow
    cv2.imwrite(path+'_final/'+A[i]+'_2.png', yellow)
