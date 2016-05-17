from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
import json
import pymongo
from pymongo import MongoClient

# Create your views here.
def index(request):
	return HttpResponse("I am at the correct page")
	
	
def getUserContactListByMobile(request):
	#extract mobile number from json request
	json_response = json.loads(request.body.decode('UTF-8'))
	for items in json_response:
			user_mobile = json_response[items]
	
	#connect to mongo db client
	client = MongoClient("mongodb://devTest1:1234@ds019950.mlab.com:19950/p2p_master") 
	#client = MongoClient()
	db = client.p2p_master
	collection = db.UserContactList
	response = collection.find_one({"primaryMobileNo":user_mobile},{"_id":False})
	
	#convert response into json response and postback
	json_httpResponse = json.dumps(response)
		
	return HttpResponse(json_httpResponse)
	
def getUserDetailsByUniqueId(request):
	#extract unique id from json request
	json_response = json.loads(request.body.decode('UTF-8'))
	for items in json_response:
			uniqueUserId = json_response[items]
			
	#connect to mongo db client
	client = MongoClient("mongodb://devTest1:1234@ds019950.mlab.com:19950/p2p_master") 
	#client = MongoClient()
	db = client.p2p_master
	collection = db.ContactListMaster
	response = collection.find_one({"uniqueUserId":uniqueUserId},{"_id":False})
	
	#convert response into json response and postback
	json_httpResponse = json.dumps(response)
		
	return HttpResponse(json_httpResponse)
	
def getUserDetailsByEmailAndPassword(request):
	#extract email id and password from json request
	json_response = json.loads(request.body.decode('UTF-8'))
	email = json_response["email"]
	password = json_response["password"]
	
	#connect to mongo db client
	client = MongoClient("mongodb://devTest1:1234@ds019950.mlab.com:19950/p2p_master") 
	#client = MongoClient()
	db = client.p2p_master
	collection = db.UserCredentials
	response = collection.find_one({"email":email,"password":password},{"_id":False})
	
	#extract usique user id
	uniqueUserId = response["uniqueUserId"]
	
	#get user details from unique user id
	#connect to mongo db client
	client = MongoClient("mongodb://devTest1:1234@ds019950.mlab.com:19950/p2p_master") 
	#client = MongoClient()
	db = client.p2p_master
	collection = db.ContactListMaster
	response = collection.find_one({"uniqueUserId":uniqueUserId},{"_id":False})
	
	#convert response into json response and postback
	json_httpResponse = json.dumps(response)
		
	return HttpResponse(json_httpResponse)
	
def setUserCredentials(request):
	#extract email id, password and unique user id from json request
	json_response = json.loads(request.body.decode('UTF-8'))
	email = json_response["email"]
	password = json_response["password"]
	uniqueUserId = json_response["uniqueUserId"]
	
	#create document to insert
	doc = {"email":email,"password":password,"uniqueUserId":uniqueUserId}
	
	#connect to mongo db client
	client = MongoClient("mongodb://devTest1:1234@ds019950.mlab.com:19950/p2p_master") 
	#client = MongoClient()
	db = client.p2p_master
	collection = db.UserCredentials
	collection.insert_one(doc)
	
	return HttpResponse("success")
	
	
	
	
	
	
	