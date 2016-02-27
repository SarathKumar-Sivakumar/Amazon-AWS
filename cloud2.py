#Sarath Kumar Siva Kumar
#1001108398
#AWS Amazon
#CSE6331-002
#Assignment-2

import boto 
import boto.s3
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import sys
import time

#User credentials
aws_access_key_id = raw_input("Enter your access key")
aws_secret_access_key= raw_input("Enter your secret key")

#Bucket creation
s3 = boto.connect_s3(aws_access_key_id,aws_secret_access_key)
bucket = s3.create_bucket('sarathawss3',location=boto.s3.connection.Location.DEFAULT)

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

k = Key(bucket)
k.key = 'cloud\earthquake.csv'
print "Uploading..\n"

#File Uploading
starttime = time.time();
k.set_contents_from_filename('C:/Users/WELCOME/Desktop/cloud2/all_month.csv',cb=percent_cb, num_cb=10)
endtime = time.time();
totaltimetoupload=endtime-starttime

print "File Uploaded"
print "Time taken to upload file ",totaltimetoupload
