import cv2
import numpy as np
import os, os.path
import re
from matplotlib import pyplot as plt
from shutil import copyfile
import shutil

#take amount of files in folder frames
list = os.listdir('./frames') # dir is your directory path
number_files = len(list)

distant_match = []
import os
import shutil
import ColorExtract
candidate_frames = ColorExtract.ColorExtract()

candidate_index = []
def ReadCandidate():
 for i in range(0, len(candidate_frames)):
    name = candidate_frames[i]
    index_frame = re.findall('[0-9]+', name)
    a = index_frame[0]
    a = int(a)
    candidate_index.append(a)
 return candidate_index
# detect cut transition
def DetectShot(front, behind, count):
    ReadCandidate()
    if front == 0:
      dstroot = './shots/'
      dstdir1 = os.path.join(dstroot, "shot0")
      print("make dir shot0")
      os.makedirs(dstdir1)
      name_shot = "shot" + str(behind)
      dstdir2 = os.path.join(dstroot, name_shot)
      print("make dir shot1")
      os.makedirs(dstdir2)
      #    shutil.copy(srcfile, dstdir)
      for i in range(0,candidate_index[0] + 1):# create all directories, raise an error if it already exists
          srcfile = "./frames/" + "frame" + str(i) + ".jpg"
          assert not os.path.isabs(srcfile)
          shutil.copy(srcfile, dstdir1)
          print("copy frame", i )
      for i in range(candidate_index[1],candidate_index[2] + 1):
          srcfile = "./frames/" + "frame" + str(i) + ".jpg"
          assert not os.path.isabs(srcfile)
          shutil.copy(srcfile, dstdir2)
          print("copy frame", i)

    else:
      dstroot = './shots/'
      if count != 0:
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
candidate_index = ReadCandidate()
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

dstroot = './shots/'
#name_shot_last = "shot" + str(count)
#dstdir2 = os.path.join(dstroot, name_shot_last)
print("make dir last shot", count )
print("hahaha")
for i in range(candidate_index[-1], number_files):
     srcfile = "./frames/" + "frame" + str(i) + ".jpg"
     assert not os.path.isabs(srcfile)
     des = "./shots/" + "shot" + str(count -1)
     shutil.copy(srcfile,des )
     print("copy frame", i)
