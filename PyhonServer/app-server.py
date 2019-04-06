from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
import json
import socket

app = Flask(__name__)
api = Api(app)

# test Data
dataJson = [
	{
		"data" : "YodaPicData",
		"tagString" : " no1"
	},
	{
		"data":"carPicData",
		"tagString" : " no2"
	}
]

waterMarkTxt = " pyServ(R) "

class WaterMark(Resource):

	def post(self):
		#print(json.loads(request.data))
		#getting the data in json, load into python object
		dataIn = json.loads(request.data)

		#Check if data is already present.
		for myData in dataJson:
			if( dataIn["data"] == myData["data"] ):
				return "same data already exists", 400 #Bad request

		dataJson[0].update(dataIn)
		print("Data to be water marked was submitted")

		#CALL WATERMARKING FUNCTION(s) HERE!
		WaterMarkedData = dataJson[0]["data"] + dataJson[0]["tagString"]
		myNewData = { "data" : WaterMarkedData }
		dataJson[0].update(myNewData)

		print("Returning WaterMarked Data")

		#Return the altered data.
		return jsonify(dataJson[0])#, 201 #Created - HTTP status code, not working with jsonify..

	#Don't really need these - just here for the view.
	def get(self):
		return 0

	def put(self):
		return 0

	def delete(self):
		return 0

api.add_resource(WaterMark, "/water_mark")

app.run(debug=True, host="0.0.0.0", port=80)