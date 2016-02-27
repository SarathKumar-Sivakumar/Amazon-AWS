#Sarath Kumar Siva Kumar
#1001108398
#AWS Amazon
#CSE6331-002
#Assignment-2

import memcache
from time import sleep
import MySQLdb
import time
import sys
from random import randint


USERNAME = "sarath"
PASSWORD = "Sancdev24"
DB_PORT = 3306
DB_NAME = 'earthquake'

#Connecting to RDS Instance

conn = MySQLdb.connect(host="sarath.cg0xxbvyoyws.us-west-2.rds.amazonaws.com",user=USERNAME,passwd=PASSWORD,db=DB_NAME,port=DB_PORT)
print "Connected to RDS Instance"

memc =memcache.Client(["127.0.0.1:11211"])

query1="select count(*) from earthquakescloud where depth > 5 and `datetime` >= DATE_SUB(CURDATE(), INTERVAL 1 WEEK);"
query2="select location,datetime,mag,dmin from earthquakescloud where rms > 1 and `datetime` >= DATE_SUB(CURDATE(), INTERVAL 1 WEEK);"
query3="select count(*) from earthquakescloud where dmin > 5 and `datetime` >= DATE_SUB(CURDATE(), INTERVAL 1 WEEK);"

memc.flush_all()

starttime=time.time()
for x in range(1,2000):
        random_number=randint(0,2)
        if random_number==0:
                query_one=memc.get('query_one')
                if not query_one:
                        cursor=conn.cursor()
                        cursor.execute(query1)
                        rows=cursor.fetchall()
                        memc.set('query_one',rows,2000)
                        print "Updated Memcached with Query 1 Result"
                else:
                        print "Loaded Query 1 Results from Memcached"
                        for row in query_one:
                                print "%s" %(row[0])
        elif random_number==1:
                query_two=memc.get('query_two')
                if not query_two:
		                 cursor=conn.cursor()
                        cursor.execute(query2)
                        rows=cursor.fetchall()
                        memc.set('query_two',rows,2000)
                        print "Updated Memcached with Query 2 results"
                else:
                        print "Loaded Query 2 results from Memcached"
                        for row in query_two:
                                print "%s%s%s%s" %(row[0],row[1],row[2],row[3])
        elif random_number==2:
                query_three=memc.get('query_three')
                if not query_three:
                        cursor=conn.cursor()
                        cursor.execute(query3)
                        rows=cursor.fetchall()
                        memc.set('query_three',rows,2000)
                        print "Updated Memcached with Query 3 Results"
                else:
                        print "Loaded Query 3 results from Memcached"
                        for row in query_three:
                                print "%s"%(row[0])

endtime=time.time()
print 'The time taken to run 2000 random queries is',endtime-starttime

query4="select rms,id,gap from earthquakescloud limit 2000;"
query5="select location,datetime,mag,dmin from earthquakescloud limit 2000;"
query6="select depth,mag,dmin,rms from earthquakescloud limit 2000;"

memc.flush_all()

starttime=time.time()
for x in range(1,2000):
        random_number=randint(0,2)
        if random_number==0:
                query_four=memc.get('query_four')
                if not query_four:
                        cursor=conn.cursor()
                        cursor.execute(query4)
                        rows=cursor.fetchall()
                        memc.set('query_four',rows,2000)
                        print "Updated Memcached with Query 4 Result"
                else:
                        print "Loaded Query 4 Results from Memcached"
                        for row in query_four:
                                print "%s%s%s" %(row[0],row[1],row[2])
        elif random_number==1:
                query_five=memc.get('query_five')
                if not query_five:
                        cursor=conn.cursor()
                        cursor.execute(query5)
                        rows=cursor.fetchall()
                        memc.set('query_five',rows,2000)
                        print "Updated Memcached with Query 5 results"
                else:
                        print "Loaded Query 5 results from Memcached"
                        for row in query_five:
                                print "%s%s%s%s" %(row[0],row[1],row[2],row[3])
        elif random_number==2:
                query_six=memc.get('query_six')
                if not query_six:
                        cursor=conn.cursor()
                        cursor.execute(query6)
                        rows=cursor.fetchall()
                        memc.set('query_six',rows,2000)
                        print "Updated Memcached with Query 6 Results"
                else:
                        print "Loaded Query 6 results from Memcached"
                        for row in query_six:
                                print "%s%s%s%s" %(row[0],row[1],row[2],row[3])

endtime=time.time()
print 'The time taken to run 2000 random queries with limited scope is',endtime-starttime   
        