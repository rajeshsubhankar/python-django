from django.shortcuts import render
from django.http import HttpResponse
import datetime
import math
import os
import hmac
from hashlib import sha1
import json
import smtplib

# Create your views here.

def index(request):
	return HttpResponse("I am at the correct page")
	
def get(request):
	#start of epoch
	T0 = 0
	#epoch interval as 30 seconds
	TS = 30

	#TC:Time Counter-->converted to encoded string
	TC = str(int(math.floor(( datetime.datetime.utcnow().timestamp() - T0 )/TS))).encode('utf-8')

	#kay: 20 bytes random shard key
	K = os.urandom(20)
	#K = b'\xff[\xf6\xad\x96\x8c\xdaB\xd4\xa7tg\xcd\xe85FT\xef\x88"'

	#Hash with HMAC with SHA1
	output = hmac.new(K,TC,sha1)
	hashed = bytes(output.digest())

	#Take LSB as offset. AND with maximum hexadecimal possible to get index value from 0 to 15 
	offset = hashed[19] & 0xf

	#Take 4 bytes starting from offset index as unsigned 32 bit integer
	digits = (hashed[offset] & 0x7f)<<24 | (hashed[offset+1] & 0xff)<<16 | (hashed[offset+2] & 0xff)<<8 | (hashed[offset+3] & 0xff)

	#Extract appropriate number of digits as OTP. Here it is 6
	TOTP = int(digits % math.pow(10,6))
	
	#return OTP
	return HttpResponse(TOTP)
	
def sendOtpEmail(request):
	#generate otp for this request
	otp = get(request).content.decode('UTF-8')
	
	#extract receiver email from request body	
	json_response = json.loads(request.body.decode('UTF-8'))
	for items in json_response:
		receiver_mail = json_response[items]
	
	#send otp through mail
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login("xxxx@gmail.com","PASSWORD")
	server.sendmail("xxxx@gmail.com",receiver_mail,otp)
	server.quit()
	
	
	return HttpResponse(otp)
