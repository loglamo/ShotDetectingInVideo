import numpy as np
import cv2
from matplotlib import pyplot as plt
import re
import ColorExtract
import os
from shutil import copyfile


number_files = ColorExtract.TakeNumberFrames()
candidate_frames = ColorExtract.ColorExtract()
#candidate_number = len(candidate_frames)/2
candidate_index = []
#lay index candidate
def ReadCandidate():
 for i in range(0, len(candidate_frames)):
    name = candidate_frames[i]
    index_frame = re.findall('[0-9]+', name)
    a = index_frame[0]
    a = int(a)
    candidate_index.append(a)
 return candidate_index
# detect cut transition
# front = behind -1, index
# phats hien cut vaf fade
def Detect_cut_transition(front, behind):
#   for i in range(0, len(candidate_frames)):
      ReadCandidate()
      first_index_candidate = candidate_index[front]
      second_index_candidate = candidate_index[behind]
      first_index_sub_front = first_index_candidate - 1
      second_index_sub_front  = first_index_candidate - 2
      third_index_sub_front  = first_index_candidate - 3


      first_index_sub_behind = second_index_candidate + 1
      second_index_sub_behind = second_index_candidate + 2
      third_index_sub_behind = second_index_candidate + 3


      print("calculating Match")
      match_1_1 = MatchWithBF(first_index_candidate,first_index_sub_front )
      match_1_2 = MatchWithBF(first_index_sub_front,second_index_sub_front)
      match_1_3 = MatchWithBF(second_index_sub_front,third_index_sub_front)


      match_2_1 = MatchWithBF(second_index_candidate,first_index_sub_behind)
      match_2_2 = MatchWithBF(first_index_sub_behind,second_index_sub_behind )
      match_2_3 = MatchWithBF(second_index_sub_behind,third_index_sub_behind )


      match_main = MatchWithBF(first_index_candidate,second_index_candidate)
      if (match_main <= match_1_1) & (match_main <= match_1_2) & (match_main <= match_1_3) & (match_main <= match_2_1) & (match_main <= match_2_2) & (match_main <= match_2_3):
          print("this is cut transition" )
      elif (match_1_3 >= match_1_2) & (match_1_2 >= match_1_1) & (match_1_1 >= match_main) & (match_main <= match_2_1) & (match_2_1 <= match_2_2) & (match_2_2 <= match_2_3):
          print("this is fade transition")
      else:
          print("Another type transition")

# ham tinh khoang cach giua cac frame keypoint
def MatchWithBF(a ,b ):
    img1_name = "frame" + str(a) + ".jpg"
    img2_name = "frame" + str(b) + ".jpg"
    full_img1_name = './frames/' + img1_name
    full_img2_name = './frames/' + img2_name
    img1 = cv2.imread(full_img1_name, 0)  # queryImage
    img2 = cv2.imread(full_img2_name, 0)
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
# BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
    good = []
    for m,n in matches:
      if m.distance < 0.75*n.distance:
        good.append([m])
    #img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good,None, flags=2)
    print(len(good))
    return len(good)

def DetectShot(front, behind):
    if front == 0:
        dir_frame1 = "./frames/" + "frame" +str(candidate_index[0]) + ".jpg"
        name_shot = "shot" + str(front)
        pathOut = "./shots/" + name_shot
        os.mkdir(pathOut)
        copyfile(dir_frame1, pathOut)


ReadCandidate()
#print(candidate_index)
#print(len(candidate_index))

for i in range(0,len(candidate_index),2):
 Detect_cut_transition(i,i+1)
 print("next ", i)
#for i in range(0,len(candidate_index)):
 #  print("detecting frame ")
  # print(i)
  # print(i+1)
  # Detect_cut_transition(i,i+1)
   #i += 2
#   print("next, will detect frame ")