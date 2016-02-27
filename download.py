#Sarath Kumar Siva Kumar
#1001108398
#AWS Amazon
#CSE6331-002
#Sarath Kumar Siva Kumar
#1001108398
#AWS Amazon
#CSE6331-002
#Assignment-2

import boto
import boto.s3
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import sys,os
import time

LOCAL_PATH = 'C:\Users\WELCOME\Desktop\cloud2\s3'
AWS_ACCESS_KEY_ID = raw_input("Enter your access key")
AWS_SECRET_ACCESS_KEY= raw_input("Enter your secret key")
bucket_name = 'sarathawss3'

# connect to the bucket
conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
bucket = conn.get_bucket(bucket_name)

# go through the list of files
bucket_list = bucket.list()

k = Key(bucket)
k.key = 'earthquake.csv'
print "Downloading..\n"

if not os.path.exists('earthquake.csv'):
	starttime = time.time();
	k.get_contents_to_filename(k.key)
	endtime = time.time();

totaltimetodownload=endtime-starttime
print "Successfully Downloaded"
print "Download time taken is : ", totaltimetodownload