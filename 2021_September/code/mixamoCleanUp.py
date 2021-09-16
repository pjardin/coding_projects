import os

import json

import shutil

saveTo = "/Users/pascaljardin/Documents/Mixamo_data/web_scraped/Mixamo"

saved_folders = os.listdir(saveTo)
print("\n\n\n========\n\n")
for i in range(0,2441):
    #print(i)
    path = os.path.join(saveTo, str(i))

    contents = os.listdir(path)
    
    
    
    s = ""
    """
    try:
        os.remove(os.path.join(path, '.DS_Store'))
        print("remove")
    except:
        s = "s"
    """
    found = False;
    for file in contents:
        if file.endswith(".fbx"):
            found = True
            break
            
    if (found == True):
        
        print(path)
        print(len(contents))
        print(contents)

