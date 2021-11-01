# import the necessary packages
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2
import os
import json
import dlib

detector_path = "/Users/pascaljardin/Documents/greenScreenCap/monkey_test/monkeyDetector.svm"
detector = dlib.simple_object_detector(detector_path)

frame_folder = "/Users/pascaljardin/Documents/greenScreenCap/monkey_test/images"

frames_loc = os.listdir(frame_folder)

frames_loc.sort(key=lambda x: '{0:0>8}'.format(x))

# loop over the frames of the video
for i, f in enumerate(frames_loc):
    
    if (".DS_Store" == f):
        print("found .DS_Store")
        continue
    
    #get image
    image_loc = os.path.join(frame_folder, f)
    print(image_loc)
    
    im = cv2.imread(image_loc, cv2.IMREAD_UNCHANGED)
    
    #remove alpha
    #make mask of where the transparent bits are
    trans_mask = im[:,:,3] == 0

    #replace areas of transparency with white and not transparent
    im[trans_mask] = [0, 0, 0, 255]

    #new image without alpha channel...
    new_img = cv2.cvtColor(im, cv2.COLOR_BGRA2BGR)
    
    
    dets = detector(new_img)
    
    for d in dets:
        
        cv2.rectangle(new_img, (d.left(), d.top()), (d.left() + d.width(), d.top() + d.height()), (0, 255, 0), 2)
        
    time.sleep(1)
    cv2.imshow("new_image", new_img)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
