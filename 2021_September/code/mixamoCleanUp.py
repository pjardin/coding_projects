import os

import json

import shutil

saveTo = "/Users/pascaljardin/Documents/GitHub/coding_projects/2021_September/Mixamo"
downlaods_folder = "/Users/pascaljardin/Downloads"


saved_folders = os.listdir(saveTo)

for i in range(0,2531):
    path = os.path.join(saveTo, str(i))

    contents = os.listdir(path)

    if (len(contents) != 3):
        
        print(path)
        print(len(contents))
        print(contents)

