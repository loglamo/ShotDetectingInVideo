import numpy as np
import cv2
from matplotlib import pyplot as plt
import ColorExtract
import re

number_files = ColorExtract.TakeNumberFrames()
candidate_frames = ColorExtract.ColorExtract()
#candidate_number = len(candidate_frames)/2
candidate_index = []
def ReadCandidate():
 for i in range(0, len(candidate_frames)):
    name = candidate_frames[i]
    index_frame = re.findall('[0-9]+', name)
    a = index_frame[0]
    a = int(a)
    print(a)
    candidate_index.append(a)
 return candidate_index

img1 = cv2.imread('frame198.jpg',0)          # queryImage
img2 = cv2.imread('frame199.jpg',0) # trainImage

# Initiate SIFT detector
distant_match = []
def MatchWithBF(a ,b ):
    img1_name = "frame" + str(a) + ".jpg"
    img2_name = "frame" + str(b) + ".jpg"
    print(img1_name)
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
    distant_match.append(good)
    #img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good,None, flags=2)
    return len(good)
# cv2.drawMatchesKnn expects list of lists as matches.
#img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)

#plt.imshow(img3),plt.show()
def Detect_cut_transition(front, behind):
#   for i in range(0, len(candidate_frames)):
      ReadCandidate()
      first_index_candidate = candidate_index[front]
      second_index_candidate = candidate_index[behind]
      first_index_sub_front = first_index_candidate - 1
      second_index_sub_front  = first_index_candidate - 2
      third_index_sub_front  = first_index_candidate - 3
      fourth_index_sub_front  = first_index_candidate - 4
      print("here")

      first_index_sub_behind = second_index_candidate + 1
      second_index_sub_behind = second_index_candidate + 2
      third_index_sub_behind = second_index_candidate + 3
      fourth_index_sub_behind = second_index_candidate + 4
      print("there")

      match_1_1 = MatchWithBF(first_index_candidate,first_index_sub_front )
      match_1_2 = MatchWithBF(first_index_sub_front,second_index_sub_front)
      match_1_3 = MatchWithBF(second_index_sub_front,third_index_sub_front)
      match_1_4 = MatchWithBF(third_index_sub_front,fourth_index_sub_front)

      match_2_1 = MatchWithBF(second_index_candidate,first_index_sub_behind)
      match_2_2 = MatchWithBF(first_index_sub_behind,second_index_sub_behind )
      match_2_3 = MatchWithBF(second_index_sub_behind,third_index_sub_behind )
      match_2_4 = MatchWithBF(third_index_sub_behind,fourth_index_sub_behind )

      match_main = MatchWithBF(first_index_candidate,second_index_candidate)
      if (match_main <= match_1_1) & (match_main <= match_1_2) & (match_main <= match_1_3) & (match_main <= match_1_4) & (match_main <= match_2_1) & (match_main <= match_2_2) & (match_main <= match_2_3) & (match_main <= match_2_4):
          print("this is cut transition" )
      else:
          print("this is another transition  ")

Detect_cut_transition(6,7)