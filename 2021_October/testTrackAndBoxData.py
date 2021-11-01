# import the necessary packages
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2
import os
import json

# Opening JSON file
f = open('/Users/pascaljardin/Documents/greenScreenCap/monkey_test/allData.json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)

# loop over the frames of the video
for d in data:
    
    
    #get image
    image_loc = d[0]
    
    im = cv2.imread(image_loc, cv2.IMREAD_UNCHANGED)
    
    #create bouding box
    (x, y, w, h) = d[1]
    cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    #link tracked points
    for t in d[2]:
        im = cv2.circle(im, (t[0],t[1]), 4, (0, 0, 255), -1)
    
    cv2.imshow("alphaObjectDetecion", im)
    time.sleep(1)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
