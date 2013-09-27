#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from dateutil import tz

from_zone = tz.tzutc()
to_zone = tz.tzlocal()

#Get a naive datetime
utc = datetime.utcnow()

#Represent it as UTC time
utc = utc.replace(tzinfo=from_zone)

#Convert to local timezone
local = utc.astimezone(to_zone)

print "UTC: ", utc
print "LOCAL: ", local