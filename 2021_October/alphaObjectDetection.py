# import the necessary packages
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2
import os

frame_folder = "/Users/pascaljardin/Documents/greenScreenCap/parasonicFullBodyAlpha"


frames_loc = os.listdir(frame_folder)

frames_loc.sort(key=lambda x: '{0:0>8}'.format(x))
# loop over the frames of the video
for f in frames_loc:
    
    if (".DS_Store" == f):
        continue
    
    #get image
    image_loc = os.path.join(frame_folder, f)

    im = cv2.imread(image_loc, cv2.IMREAD_UNCHANGED)
    ret, mask = cv2.threshold(im[:, :, 3], 0, 255, cv2.THRESH_BINARY)

    #alpha mask
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(cnts)
    
    sorted_contours= sorted(contours, key=cv2.contourArea, reverse= False)
    
    (x, y, w, h) = cv2.boundingRect(sorted_contours[-1])
    cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow("alphaObjectDetecion", im)

    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

video.release()
