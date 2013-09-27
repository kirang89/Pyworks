#!/usr/bin/python
#
# Quick script to get details of a particular IP
#

import requests

URL = "http://ipinfo.io/{}/json"

ip = raw_input("Enter an ip address: ")
res = requests.get(URL.format(ip))
if res.status_code == 200:
    print "Details for {}".format(ip)
    print "----------------"
    for key, value in res.json().items():
        print "{}: {}".format(key,value)
else:
    print "Invalid response"