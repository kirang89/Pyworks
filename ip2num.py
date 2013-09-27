#!/usr/bin/python
#
# Convert ip address to a number
#

ip_addr = raw_input("Enter an ip address: ")
oc1,oc2,oc3,oc4 = ip_addr.split('.')
number = 16777216 * int(oc1) + 65536 * int(oc2) + 256 * int(oc3) + int(oc4)
print "The number:%d" % number

