import cv2
import numpy as np
import os, os.path
# luoc bo nhg chuoi anh giong nhau, chi giu lai nhg cap anh , ma tai do co kha nang la shot boundary


#take amount of files in folder frames
def TakeNumberFrames():
  list = os.listdir('./frames') # dir is your directory path
  number_files = len(list)
  return number_files


# read one by one image
count = 0
candidate_frames = []

def ColorExtract():
   number_files = TakeNumberFrames()
   for i in range(1, number_files):
    imgi_name = "frame" + str(i) + ".jpg"
    full_imgi_name = './frames/' + imgi_name
    imgi_1_name = "frame" + str(i-1) + ".jpg"
    full_imgi_1_name = './frames/' + imgi_1_name
    imgi = cv2.imread(full_imgi_name)
    hsvi = cv2.cvtColor(imgi,cv2.COLOR_BGR2HSV)
    imgi_1 = cv2.imread(full_imgi_1_name)
    hsvi_1 = cv2.cvtColor(imgi_1, cv2.COLOR_BGR2HSV)
    histi = cv2.calcHist([hsvi], [0, 1], None, [180, 256], [0, 180, 0, 256])
    histi_1 = cv2.calcHist([hsvi_1], [0, 1], None, [180, 256], [0, 180, 0, 256])
    a = cv2.compareHist(histi, histi_1, cv2.HISTCMP_BHATTACHARYYA)
    if a > 0.4:
        candidate_frames.append(full_imgi_1_name)
        candidate_frames.append(full_imgi_name)
        print(full_imgi_1_name)
        print(full_imgi_name)

    else:
        continue
   return candidate_frames








