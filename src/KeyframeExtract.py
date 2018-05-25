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

"""list_shots = os.listdir('./shots') # dir is your directory path
number_files_shots = len(list_shots)
print(number_files_shots)

print("___________________________+++++++++++++++++")
print(number_files_shots)
last_shot = "shot" + str(number_files_shots - 1)
print(last_shot)
print("key_frame of " + last_shot + "is: ")
last_shot_dir = "./shots/" + last_shot
list_shots = os.listdir(last_shot_dir)  # dir is your directory path
number_files_shots = len(list_shots)

key_frame = list_shots[0]
key_frame_dir = last_shot_dir + "/" + key_frame
print(key_frame)
dstroot = './keyframes/'
dstdir1 = os.path.join(dstroot, last_shot)
print("making dir" + " " + dstdir1)
os.makedirs(dstdir1)
assert not os.path.isabs(key_frame_dir)
shutil.copy(key_frame_dir, dstdir1)
print("copy frame ", key_frame)
print("_____________________________")


for i in range(0,number_files_shots - 3,1):
    if i == 0:
        print("key_frame of shot0 is: ")
        list_shots = os.listdir('./shots/shot0')  # dir is your directory path
        number_files_shots = len(list_shots)
        key_frame = list_shots[0]
        key_frame_dir = "./shots/shot0/" + key_frame
        print(key_frame)
        dstroot = './keyframes/'
        dstdir1 = os.path.join(dstroot, 'shot0')
        print("making dir" + " " + dstdir1)
        os.makedirs(dstdir1)
        assert not os.path.isabs(key_frame_dir)
        shutil.copy(key_frame_dir, dstdir1)
        print("copy frame ", key_frame)
        print("_____________________________")
    else:
        input = "shot" + str(i)
        KeyframeExtract(input)"""

# keyframes for last shot
