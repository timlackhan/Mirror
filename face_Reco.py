from __future__ import print_function
import urllib2
import urllib
import ssl
import time
import requests
#import cv2
import json
import sys
import os

http_url='https://api-cn.faceplusplus.com/facepp/v3/compare'
key="GfkqJQ5dIt1nQ9OeHUkzu3Y2_4apboCb"
secret="hvT7I3R_2RbHNkdrBtDQbQD4zlrBbvBk"
filepath1=r"/home/pi/image1.jpg"
filepath2=r"/home/pi/image2.jpg"
# face_token = 0


# boundary = '----------%s' % hex(int(time.time() * 1000))
# data = []
# data.append('--%s' % boundary)
# data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
# data.append(key)
# data.append('--%s' % boundary)
# data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
# data.append(secret)
# data.append('--%s' % boundary)
# fr1=open(filepath2,'rb')
# data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
# data.append('Content-Type: %s\r\n' % 'application/octet-stream')
# data.append(fr1.read())
# fr1.close()
# data.append('--%s--\r\n' % boundary)

# http_body='\r\n'.join(data)
# req=urllib2.Request(http_url)
# req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
# req.add_data(http_body)

# try:
# 	context = ssl._create_unverified_context()
# 	resp = urllib2.urlopen(req, timeout=5, context=context)
# 	qrcont = resp.read()
# 	#print(qrcont)
# 	face_token = str(json.loads(qrcont)['faces'][0]['face_token'])
# 	#print(face_token)
# except urllib2.HTTPError as e:
# 	print(e.read())


# http_urlGetSets='https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail'


# data = {'api_key':key,
# 		'api_secret':secret,
# 		'faceset_token':'36c1125e15132b0014d9c46b5aba3b0e'
# 		}

# r = requests.post(http_urlGetSets,data=data)  
# print(r.text)

boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
data.append('--%s' % boundary)
fr1=open(filepath1,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file1')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr1.read())
fr1.close()
data.append('--%s' % boundary)
fr2=open(filepath2,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file2')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr2.read())
fr2.close()
data.append('--%s--\r\n' % boundary)

http_body='\r\n'.join(data)
req=urllib2.Request(http_url)
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
req.add_data(http_body)

try:
	context = ssl._create_unverified_context()
	resp = urllib2.urlopen(req, timeout=5, context=context)
	qrcont = resp.read()
	confidence = json.loads(qrcont)['confidence']
	threshold = json.loads(qrcont)['thresholds']['1e-5']
	print(confidence,threshold)
	if confidence > threshold:
        	sys.exit(1)
        else:
		sys.exit(0)
except urllib2.HTTPError as e:
	print(e.read())
	sys.exit(0)
