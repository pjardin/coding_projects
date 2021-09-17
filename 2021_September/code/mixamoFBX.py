import time

import os

import json

import urllib.request

import shutil

saveTo = "/Users/pascaljardin/Documents/Mixamo_data/web_scraped/fbx"
saveToGif = "/Users/pascaljardin/Documents/Mixamo_data/web_scraped/gif"

animation_folder = "/Users/pascaljardin/Documents/Mixamo_data/web_scraped/Mixamo_Animations"

animation_folders = os.listdir(animation_folder)

for folder in animation_folders:

    if folder == ".DS_Store":
        continue

    #print(folder)
    path = os.path.join(animation_folder, folder)
    
    animation_folder_contents = os.listdir(path)
    
    f = open(os.path.join(path, "data.json"))
 
    data = json.load(f)
    #print(data["description"])
    
    fbx = ""

    for file in animation_folder_contents:
        if file.endswith(".fbx"):
            fbx = os.path.join(path, file)
            break
    if file == "":
        print(error)
        break
    
    gif = os.path.join(path, "image.gif")
    
    fbx_new = os.path.join(saveTo, data["tittle"] + "; "+ data["description"] + ".fbx")
    gif_new = os.path.join(saveToGif, data["tittle"] + "; "+ data["description"] + ".gif")

    shutil.copyfile(fbx, fbx_new)
    shutil.copyfile(gif, gif_new)

    
