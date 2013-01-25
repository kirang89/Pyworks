#
# Script to write to and read data from Unix DBM
#

import anydbm
import whichdb

db = anydbm.open("my_database", "c")
result = whichdb.whichdb("my_database")
print result

db["one"] = "number one"
db["two"] = "number two"
db["three"] = "number three"
db.close()

db = anydbm.open("my_database", "r")
for key in db.keys():
    print repr(key), repr(db[key])
db.close()
