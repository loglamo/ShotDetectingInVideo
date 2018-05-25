import cv2
import os
import shutil

def KeyframeExtract(Input):# ten shot
    input_path = "./shots/" + Input
    print(input_path)
    list = os.listdir(input_path)  # dir is your directory path
    key_point = 0
    key_frame_name = ''
    key_frame_name_dir = ''

    for file in list:
        file_full_name = input_path + "/" + file
        img = cv2.imread(file_full_name)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sift = cv2.xfeatures2d.SIFT_create()
        kp, des = sift.detectAndCompute(gray, None)
        print(len(des))
        if len(des) > key_point:
            key_point = len(des)
            key_frame_name = file
            key_frame_name_dir = file_full_name
        else:
            continue
    print("key_frame of " + Input + " is: ")
    print(key_frame_name)
    dstroot = './keyframes/'
    dstdir1 = os.path.join(dstroot, Input)
    print("making dir" + " " + dstdir1)
    os.makedirs(dstdir1)
    assert not os.path.isabs(key_frame_name_dir)
    shutil.copy(key_frame_name_dir, dstdir1)
    print("copy frame ", key_frame_name)
    print("_____________________________")
