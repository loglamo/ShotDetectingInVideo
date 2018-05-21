import cv2
import numpy as np
import os, os.path

#take amount of files in folder frames
list = os.listdir('./frames') # dir is your directory path
number_files = len(list)


# read one by one image
count = 0
#while (count < number_files):
#     file_name = 'frame' + str(count) +'.jpg'
#      full_file_name = './frames/' + file_name
#     img = cv2.imread(full_file_name)
 #    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 #    sift = cv2.xfeatures2d.SIFT_create()
 #    kp = sift.detect(gray, None)
 #    cv2.drawKeypoints(gray, kp, img)
 #    dir = './keypoints/' + file_name
 #    cv2.imwrite(dir, img)
 #    print(count)
 #    count += 1

img = cv2.imread('frame229.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray, None)
img=cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
kp,des = sift.compute(gray,kp) #tim descriptor

#cv2.drawKeypoints(gray, kp, img)
dir = 'hihi' + 'frame13.jpg'
cv2.imwrite(dir, img)