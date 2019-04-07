# importing the requests library 
import requests 
import json

# api-endpoint 
URL = "https://quantum-spring-236900.appspot.com/water_mark"
  
  
# defining a params dict for the parameters to be sent to the API 
# data is picture data
# tagString is the text to embed into picture.
data = { 
    "data":"This is the original text",
    "tagString":" Yesyesyes"
 }

#f= open("../Images/lego_porche.png","r")

#with open("../Images/lego_porche.png", "rb") as binaryfile :
#    myArr = bytearray(binaryfile.read())

#strArr = str(myArr)

allData = { "data" : data["data"], 
            "tagString" : data["tagString"] }
data.update(allData)

PARAMS = json.dumps(data)

rPost = requests.post(url = URL, data = PARAMS) # kør det med JSON

data1 = json.loads(rPost.text)

#print("waterMarked data: " + rPost.text )
print("DATA: \n" + data1["data"])

#finalArr1 = bytes(data1["data"], "utf8")
#finalArr = bytearray(strArr, "utf8")

#with open("readfile.png", "wb+") as newFile:
#	newFile.write(finalArr)
