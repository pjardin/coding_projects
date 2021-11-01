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

predictor_path = "/Users/pascaljardin/Documents/greenScreenCap/monkey_test/monkeyPredictor.dat"
predictor = dlib.shape_predictor(predictor_path)

# Opening JSON file
f = open('/Users/pascaljardin/Documents/greenScreenCap/monkey_test/track.json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)

fb = open("/Users/pascaljardin/Documents/greenScreenCap/monkey_test/monkeyBox.json" ,)

box_data = json.load(fb)

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
    
    #create bouding box
    (x, y, w, h) = box_data[i]
    #cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    #remove alpha
    #make mask of where the transparent bits are
    trans_mask = im[:,:,3] == 0

    #replace areas of transparency with white and not transparent
    im[trans_mask] = [0, 0, 0, 255]

    #new image without alpha channel...
    new_img = cv2.cvtColor(im, cv2.COLOR_BGRA2BGR)
    
    #get box of object
    box_image = new_img[y:y+h,x:x+w]
    
    #shape = predictor(new_img, d)
    
    time.sleep(1)
    
    #predicted tracked points
    left = x
    top = y
    right = x + w
    bottom = top + h
    
    d_rect = dlib.rectangle(int(left), int(top), int(right), int(bottom))

    shape = predictor(new_img, d_rect)
    for i in range(4):
        cv2.circle(new_img, (shape.part(i).x, shape.part(i).y), 5, (0, 0, 255), -1)
    
    time.sleep(1)
    cv2.imshow("new_image", new_img)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
