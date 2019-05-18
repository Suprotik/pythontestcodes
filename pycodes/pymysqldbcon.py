#!/usr/bin/python3

import pymysql

# Open database connection
#db = pymysql.connect("localhost","root","root@MySQL","homedb" )
db = pymysql.connect("192.168.0.104","Devuser","Dev@mysql","homedb")


# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
#cursor.execute("SELECT VERSION()")
cursor.execute("SELECT bRid from hbillrectab")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()