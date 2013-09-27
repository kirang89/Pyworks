#!/usr/bin/python
#
# Convert a number to the corresponding ip address
#

number = int(raw_input("Enter a number: "))
oc1 = str((number/16777216) % 256)
oc2 = str((number/65536) % 256)
oc3 = str((number/256) % 256)
oc4 = str(number % 256)

print "IP address: %s" % '.'.join([oc1,oc2,oc3,oc4])