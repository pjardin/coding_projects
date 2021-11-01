from sys import argv
import os.path
import numpy
import json

allData_save_to = "/Users/pascaljardin/Documents/greenScreenCap/monkey_test/allData.json"

# Opening JSON file
f = open('/Users/pascaljardin/Documents/greenScreenCap/monkey_test/track.json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)

fb = open("/Users/pascaljardin/Documents/greenScreenCap/monkey_test/monkeyBox.json" ,)

box_data = json.load(fb)

frame_folder = "/Users/pascaljardin/Documents/greenScreenCap/monkey_test/images_with_background"


frames_loc = os.listdir(frame_folder)

frames_loc.sort(key=lambda x: '{0:0>8}'.format(x))

allData = []

# loop over the frames of the video
for i, f in enumerate(frames_loc):
    
    if (".DS_Store" == f):
        print("found .DS_Store")
        continue
    
    image_loc = os.path.join(frame_folder, f)
    allData.append([image_loc, box_data[i], data[i]])
    
    
with open(allData_save_to, 'w') as outfile:
    json.dump(allData, outfile)


