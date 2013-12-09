#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
#                                                          #
# Simple script to connect to a remote mysql database      #
#                                                          #
#                                                          #
# Install MySQLdb package by running:                      #
#                                                          #
#                       pip install MySQL-python           #
#                                                          #
############################################################


import MySQLdb as db

HOST = "remote host"
PORT = 3306
USER = "username of remote mysql instance"
PASSWORD = "password of remote mysql instance"
DB = "database name"

try:
    connection = db.Connection(host=HOST, port=PORT,
                               user=USER, passwd=PASSWORD, db=DB)

    dbhandler = connection.cursor()
    dbhandler.execute("SELECT * from your_table")
    result = dbhandler.fetchall()
    for item in result:
        print item

except Exception as e:
    print e

finally:
    connection.close()

