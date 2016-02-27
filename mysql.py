#Sarath Kumar Siva Kumar
#1001108398
#AWS Amazon
#CSE6331-002
#Assignment-2

import boto.rds
from time import sleep
import MySQLdb
import time
from random import randint


USERNAME = 'sarath'
PASSWORD = 'Sancdev24'
DB_Nmae = 'earthquake'

print "Connecting to RDS instance"

#Rds connection
conn =  MySQLdb.connect( host =
	"sarath.cg0xxbvyoyws.us-west-2.rds.amazonaws.com",
	user=USERNAME,
	passwd=PASSWORD,
	db=DB_Nmae,
	port=3306)

print "Connected to RDS instance"

cursor = conn.cursor()
cursor1 = conn.cursor()

#Query to find Time-magnitude relationship
starttime = time.time();

query1="SELECT count(*) FROM earthquakescloud WHERE `datetime` >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH) and mag > 5;"
cursor.execute(query1)
mag5= cursor.fetchone()

query2="SELECT count(*) FROM earthquakescloud WHERE `datetime` >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH) and (mag between 4 and 5);"
cursor.execute(query2)
mag4= cursor.fetchone()

query3="SELECT count(*) FROM earthquakescloud WHERE `datetime` >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH) and (mag between 3 and 4);"
cursor.execute(query3)
mag3= cursor.fetchone()

query4="SELECT count(*) FROM earthquakescloud WHERE `datetime` >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH) and (mag between 2 and 3);"
cursor.execute(query4)
mag2= cursor.fetchone()

if mag5 > mag4 and mag5 > mag3 and mag5 > mag2:
   print "The most frequent is magnitude greater than 5", mag5
elif mag4 > mag3 and mag4 > mag2:
   print "The most frequent is magnitude greater than 4", mag4
elif mag3 > mag2:
   print "The most frequent is magnitude greater than 3", mag3
else:
   print "The most frequent is magnitude greater than 2", mag2

if mag5 < mag4 and mag5 < mag3 and mag5 < mag2:
   print "The least frequent is magnitude greater than 5", mag5
elif mag4 < mag3 and mag4 < mag2:
   print "The least frequent is magnitude greater than 4", mag4
elif mag3 < mag2:
   print "The least frequent is magnitude greater than 3", mag3
else:
   print "The least frequent is magnitude greater than 2", mag5
   
endtime = time.time();
totaltimetorun=endtime-starttime
 
print "Time to run the time-magnitude relation is %f" %totaltimetorun

#Queries for random
starttime = time.time(); 
query5="select count(*) from earthquakescloud where depth > 5 and `datetime` >= DATE_SUB(CURDATE(), INTERVAL 1 WEEK);"
query6="select count(*) from earthquakescloud where rms > 1 and `datetime` >= DATE_SUB(CURDATE(), INTERVAL 1 WEEK);"
query7="select count(*) from earthquakescloud where dmin > 5 and `datetime` >= DATE_SUB(CURDATE(), INTERVAL 1 WEEK);"
query8="select count(*) from earthquakescloud where gap > 15 and `datetime` >= DATE_SUB(CURDATE(), INTERVAL 1 WEEK);"
query9="select count(*) from earthquakescloud where depth < 5 and `datetime` >= DATE_SUB(CURDATE(), INTERVAL 1 WEEK);"

queriesarray=(query5,query6,query7,query8,query9)

for row in range(1,2000):
	ran=randint(0,4)	
	cursor.execute(queriesarray[ran])

endtime = time.time();
totaltimetorunrandom =endtime-starttime
print "Time to run the 2000 random queries is %f" %totaltimetorunrandom

cursor.close()

#Queries for random with limited scope
starttime = time.time();
query10="select * from earthquakescloud where depth > 5 limit 1,2000;"
query11="select * from earthquakescloud where rms > 1 limit 1,2000;"
query12="select * from earthquakescloud where dmin > 5 limit 1,2000;"
query13="select * from earthquakescloud where gap > 15 limit 1,2000;"
query14="select * from earthquakescloud where depth < 5 limit 1,2000;"

queryarray=(query5,query6,query7,query8,query9)

for row in range(1,2000):
	ran=randint(0,4)	
	cursor1.execute(queryarray[ran])

endtime = time.time();
totaltimetorunrandomlimited =endtime-starttime

print "Time to run the 2000 random queries  limited scope is %f" %totaltimetorunrandomlimited
  
print "Good bye!"