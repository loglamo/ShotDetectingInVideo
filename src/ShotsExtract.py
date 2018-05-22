import cv2
import numpy as np
import os, os.path
import re
import shutil
import ColorExtract

#take amount of files in folder frames
number_files = ColorExtract.TakeNumberFrames()
candidate_frames = ColorExtract.ColorExtract()
candidate_index = []
cut_transition = []

# doc so trong duong dan frame "frame123" extract 123, append vao mang candidate_index
def ReadCandidate():
 for i in range(0, len(candidate_frames)):
    name = candidate_frames[i]
    index_frame = re.findall('[0-9]+', name)
    a = index_frame[0]
    a = int(a)
    candidate_index.append(a)
 return candidate_index

candidate_index = ReadCandidate()


# ham duoi day de phat hien shot do la cut transition hay fade transition,...

def Detect_cut_fade_transition(front, behind):
     first_index_candidate = candidate_index[front]
     second_index_candidate = candidate_index[behind]
     first_index_sub_front = first_index_candidate - 1
     second_index_sub_front = first_index_candidate - 2
     third_index_sub_front = first_index_candidate - 3

     first_index_sub_behind = second_index_candidate + 1
     second_index_sub_behind = second_index_candidate + 2
     third_index_sub_behind = second_index_candidate + 3

     print("calculating Match between 2 frame ....", first_index_candidate,"and", second_index_candidate)
     match_1_1 = MatchWithBF(first_index_candidate, first_index_sub_front)
     match_1_2 = MatchWithBF(first_index_sub_front, second_index_sub_front)
     match_1_3 = MatchWithBF(second_index_sub_front, third_index_sub_front)

     match_2_1 = MatchWithBF(second_index_candidate, first_index_sub_behind)
     match_2_2 = MatchWithBF(first_index_sub_behind, second_index_sub_behind)
     match_2_3 = MatchWithBF(second_index_sub_behind, third_index_sub_behind)

     match_main = MatchWithBF(first_index_candidate, second_index_candidate)
     if (match_main <= match_1_1) & (match_main <= match_1_2) & (match_main <= match_1_3) & (
         match_main <= match_2_1) & (match_main <= match_2_2) & (match_main <= match_2_3):
         print("this is cut transition")
         print("...................................")
         cut_transition.append(first_index_candidate)
         cut_transition.append(second_index_candidate)

     elif (match_1_3 >= match_1_2) & (match_1_2 >= match_1_1) & (match_1_1 >= match_main) & (
         match_main <= match_2_1) & (match_2_1 <= match_2_2) & (match_2_2 <= match_2_3):
         print("this is fade transition")
         print("...................................")
         cut_transition.append(first_index_candidate)
         cut_transition.append(second_index_candidate)
     else:
         print("this is another type transition")
         print("...................................")
         cut_transition.append(first_index_candidate)
         cut_transition.append(second_index_candidate)


# ham tinh khoang cach giua cac frame keypoint
def MatchWithBF(a, b):
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
    matches = bf.knnMatch(des1, des2, k=2)

    # Apply ratio test
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append([m])
    # img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good,None, flags=2)
    print("the similarity is", len(good))
    return len(good)


print("the number of candidates is", len(candidate_index))
for i in range(0, len(candidate_index) - 2, 2):
    print("Detecting candidate couple", i)
    Detect_cut_fade_transition(i, i + 1)


# (front, behind) la bo index cap frame ma tai do co transition, [198,199,209,210,...], (front, behind) = (0,1) lay so thu tu (index) trong mang, count, bien thu tu tao folder chua cac frame trong 1 shot
# ham DetectShot tu cac cap index, tach cac frame cung shot vao 1 folder

def DetectShot(front, behind, count):
    if front == 0:
      dstroot = './shots/'
      dstdir1 = os.path.join(dstroot, "shot0")
      print("making dir shot0")
      os.makedirs(dstdir1)
      name_shot = "shot" + str(behind)
      dstdir2 = os.path.join(dstroot, name_shot)
      print("making dir shot1")
      os.makedirs(dstdir2)
      #    shutil.copy(srcfile, dstdir)
      for i in range(0,candidate_index[0] + 1):# create all directories, raise an error if it already exists
          srcfile = "./frames/" + "frame" + str(i) + ".jpg"
          assert not os.path.isabs(srcfile)
          shutil.copy(srcfile, dstdir1)
          print("copy frame ", i )
      for i in range(candidate_index[1],candidate_index[2] + 1):
          srcfile = "./frames/" + "frame" + str(i) + ".jpg"
          assert not os.path.isabs(srcfile)
          shutil.copy(srcfile, dstdir2)
          print("copy frame", i)


    else:
      dstroot = './shots/'
      name_shot2 = "shot" + str(count)
      dstdir2 = os.path.join(dstroot, name_shot2)
      print("make dir shot", count)
      os.makedirs(dstdir2)
      for i in range(candidate_index[behind], candidate_index[behind + 1] + 1):
            srcfile = "./frames/" + "frame" + str(i) + ".jpg"
            assert not os.path.isabs(srcfile)
            shutil.copy(srcfile, dstdir2)
            print("copy frame", i)






count = 0
for i in range(0,len(candidate_index),2):
    print(i)
    if i == 0:
        count = 2
    elif i < (len(candidate_index) -3):
      DetectShot(i,i+1,count)
      count += 1
      print(count)
    else:
       break
# tach shot cuoi cung
dstroot = './shots/'
name_shot_last = "shot" + str(count)
dstdir2 = os.path.join(dstroot, name_shot_last)
print("make dir last shot", count )
os.makedirs(dstdir2)
print("hahaha")
for i in range(candidate_index[-1], number_files):
     srcfile = "./frames/" + "frame" + str(i) + ".jpg"
     assert not os.path.isabs(srcfile)
     shutil.copy(srcfile,dstdir2)
     print("copy frame", i)
