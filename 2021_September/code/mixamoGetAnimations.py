

from selenium import webdriver
import webbrowser
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select

import time

import os

import json

import urllib.request

import shutil

email = "pjardin@me.com"
password = "4adogBlue"
saveTo = "/Users/pascaljardin/Documents/GitHub/coding_projects/2021_September/Mixamo"
downlaods_folder = "/Users/pascaljardin/Downloads"

driver = webdriver.Chrome(executable_path="/Users/pascaljardin/Documents/GitHub/coding_projects/2021_September/chromedriver")
driver.get("https://www.mixamo.com/")
#button = driver.find_element_by_id('idofbutton')

#click login button
button = driver.find_elements_by_class_name("spectrum-Button--overBackground")
button[0].click()
time.sleep(2)

#enter in email
emailTextBox = driver.find_elements_by_tag_name("input")
emailTextBox[0].send_keys(email);

button = driver.find_elements_by_class_name("SpinnerButton")
button[0].click()
time.sleep(2)
#enter in passowrd
passowrdTextBox = driver.find_element_by_id("PasswordPage-PasswordField")
passowrdTextBox.send_keys(password);
passowrdTextBox.send_keys(Keys.ENTER)

time.sleep(10)
#now we are in Mixamo!

animation_count = 0
        
page = 0;
        
while True:

    page += 1
    
    print("\ncurrent page:" + str(page))

    animations = driver.find_elements_by_class_name("product-animation")

    for a in animations:
        
        path = os.path.join(saveTo, str(animation_count))
        animation_count += 1
        
        #creates folder for animation
        os.mkdir(path)
        
        #select animation
        a.click()
        time.sleep(1)

        downloadButton = driver.find_elements_by_class_name("btn-primary")[0]

        downloadButton.click()
        time.sleep(2)
        form = driver.find_elements_by_xpath("//select[contains(@class, 'input-sm') and contains(@class, 'form-control')] ")
        
        form[2].find_element_by_xpath("//option[contains(@value, 'false')] ").click()

        time.sleep(3)

        form[3].find_elements_by_class_name("text-capitalize")[0].click()

        time.sleep(2)

        downloadButton = driver.find_elements_by_class_name("btn-primary")[1].click()

        time.sleep(10)

        download_files = os.listdir(downlaods_folder)

        for file_name in download_files:
            shutil.move(os.path.join(downlaods_folder, file_name), path)
        
        images = a.find_elements_by_tag_name('img')
        image_src = images[0].get_attribute('src')
        
        urllib.request.urlretrieve(image_src, path + "/image.gif")
        
        description = a.find_elements_by_tag_name('li')[0].get_attribute('innerHTML')
        description = description.split("-->")[-2][:-17]

        tittle = a.find_elements_by_class_name("text-capitalize")[0].get_attribute('innerHTML')
        
        data = {}
        
        data["image"] = image_src
        data["tittle"] = tittle
        data["description"] = description
        
        # Serializing json
        json_object = json.dumps(data, indent = 4)
        
        with open(path + '/data.json', 'w') as outfile:
            outfile.write(json_object)
        
        time.sleep(5)


    
    time.sleep(3)
    print("next page")

    bar = driver.find_elements_by_class_name("pagination-holder")[0]
    
    
    items = bar.find_elements_by_tag_name("a")
    

    for i in items:
        
        if (i.get_attribute('innerHTML') == '<span class="fa fa-angle-right"></span>'):
            i.click()
            print("click")
            break
            
    time.sleep(3)

driver.close()
