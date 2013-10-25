
import sys

if hasattr(sys, 'real_prefix'):
    print "Inside virtualenv"
else:
    print "Outside virtualenv"
