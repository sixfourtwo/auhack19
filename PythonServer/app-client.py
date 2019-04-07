# importing the requests library 
import requests 
import json
  
# api-endpoint 
URL = "http://127.0.0.1:80/water_mark"
  
  
# defining a params dict for the parameters to be sent to the API 
# data is picture data
# tagString is the text to embed into picture.
data = { 
	"data":"This is the original text",
	"tagString":" Yesyesyes"
 }
PARAMS = json.dumps(data)

rPost = requests.post(url = URL, data = PARAMS) # kør det med JSON

data1 = json.loads(rPost.text)

#print("waterMarked data: " + rPost.text )
print("DATA: \n" + data1["data"])
