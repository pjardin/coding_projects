from sys import argv
import os.path
import numpy
import json
import numpy as np

#this is to write xml
from xml.etree.ElementTree import fromstring, ElementTree


#prep and get data
# Opening JSON file
f = open('/Users/pascaljardin/Documents/greenScreenCap/monkey_test/allData.json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)

#now we have data, we need to randimize it
np.random.shuffle(data)

#set size of data, may be comented out
#data = data[:1000]

#with it randmize we need to split into train and test data!
size = len(data)
train_ratio = 0.7

split = int(train_ratio * size)

train_data = data[:split]
test_data = data[split:]

save_to = '/Users/pascaljardin/Documents/greenScreenCap/monkey_test'

#since this is ment to be used for blender
#we will assume that the width and height is fixed
#blender defulat is 1920 × 1080

def generatXML(save_to, name, data):
    xmlStuff = "<dataset>\n<name>"+name+"</name>\n<images>"

    for d in data:

        print(d[0])
        xmlStuff += "\n\t<image file='"+ d[0] + "' width='1920' height='1080'>\n\t\t<box top='"+str(d[1][1])+ "' left='"+str(d[1][0])+ "' width='"+str(d[1][2])+ "' height='"+str(d[1][3])+"'>"
 
        for i, p in enumerate(d[2]):
            xmlStuff += "\n\t\t\t<part name='"+str(i)+"' x='"+ str(p[0]) + "' y='" +str(p[1])+  "'/>"
        
        xmlStuff += "\n\t\t</box>\n\t</image>"
            
    xmlStuff +="\n</images>\n</dataset>"

    tree = ElementTree(fromstring(xmlStuff))

    tree.write(save_to + "/"+name + '.xml', xml_declaration=True, encoding='utf-8')

generatXML(save_to, "train_data", train_data)
generatXML(save_to, "test_data", test_data)
