# Amazon-AWS

1. Contains  python code for uploading into s3(cloud.py) 
2. Contains  python code for download from s3(download.py) 
3. Contains python code for rime-magnitude and random queries in ec2 (mysql.py)
4. Contains python code for rime-magnitude and random queries in memcache(memcached.py)

Steps to do:
1. Create aws account
2. Create ec2 instance
3. Create rds instance
4. Install aws cli package
5. Configure AWS
6. Upload to S3
	Run cloud2.py in local
	Time taken to upload file to S3 is 14.8809
7. Download from S3
	Run download.py in local
	Time taken to download file to S3 is 1.2829
8. Copy file to EC2 instance from S3:
Install Putty and puttygen 
Run cp command to copy from s3 to ec2 instance
	aws s3 cp s3://sarathawss3/cloud/earthquake.csv earthquke_ec2.csv
9. Rds
In putty install sudo apt-get mysql-client-5.5 and mysql-server-5.5
To run rds mysql 
sudo mysql -h sarath.cg0xxbvyoyws.us-west-2.rds.amazonaws.com -P 3306 -u sarath -p earthquake

Create table 
CREATE TABLE earthquakescloud ( datetime TIMESTAMP NOT NULL, latitude DECIMAL(10,8) NOT NULL, longitude DECIMAL(10,8) NOT NULL, depth DECIMAL(5,2) NOT NULL, mag DECIMAL(3,2) NOT NULL, magtype VARCHAR(10) NOT NULL, nst INTEGER(5), gap INTEGER(5), dmin DECIMAL(14,1), rms DECIMAL(3,2), net VARCHAR(3), id VARCHAR(15), updated TIMESTAMP NOT NULL, location VARCHAR(45) NOT NULL, type VARCHAR(10), PRIMARY KEY (id) );
Load data
load data local infile 'earthquke_ec2.csv' into table earthquakescloud fields terminated by ',' enclosed by '"' lines terminated by '\n' (datetime,latitude,longitude,depth,mag,magtype,nst,gap,dmin,rms,net,id,updated,location,type);
Import mysqldb connector
Run mysql.py in local
		The most frequent is magnitude greater than 2
		The lea	st frequent is magnitude greater than 5
		Time to run the time-magnitude relation is 0.267
		Time to run the 2000 random queries is 193.902
		Time to run the 2000 random queries limited scope is 213.036
10. MemoryCache
In putty install pip MySQL-python and sudo apt-get install python-memcache
Run memcached.py in putty
	Time to run the 2000 random queries is 153.094
	Time to run the 2000 random queries limited scope is 171.882


References
1. http://docs.aws.amazon.com/cli/latest/userguide/installing.html#install-msi-on-windows
2. http://stackoverflow.com/questions/14127529/mysql-import-data-from-csv-using-load-data-infile
3. http://stackoverflow.com/questions/10762239/mysql-enable-load-data-local-infile
4. http://stackoverflow.com/questions/1448429/how-to-install-mysqldb-python-data-access-library-to-mysql-on-mac-os-x
5. http://aws.amazon.com/python/
6. http://boto.readthedocs.org/en/latest/
7. http://boto.readthedocs.org/en/latest/s3_tut.html
8. https://books.google.com/books?id=JPKGBAAAQBAJ&pg=PA199&lpg=PA199&dq=complete+code+to+connect+to+rds+using+boto&source=bl&ots=8_zJ1e_KZi&sig=FBd01epofyHqw7vQTUVxFf_bPng&hl=en&sa=X&ei=_r3uVNiMLcS-ggSjs4CQAQ&ved=0CE4Q6AEwBw#v=onepage&q=complete%20code%20to%20connect%20to%20rds%20using%20boto&f=false
9. http://aws.amazon.com/developers/getting-started/python/
10. http://dev.mysql.com/doc/mysql-ha-scalability/en/ha-memcached-interfaces-python.html
11. http://stackoverflow.com/questions/2041575/mysql-query-records-between-today-and-last-30-days
12. http://davidwalsh.name/mysql-random


