#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

#
# Memoize decorator
#
def memoize(f):
    cache ={}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorated_function

#
# Now to test
#
@memoize
def custom_pow(number):
    return "%d ** 10000 = %d" % (number, number ** 10000)


if __name__ == '__main__':
    start = time.time()
    custom_pow(234)
    print "Time taken: ", time.time() - start
    
    start = time.time()
    custom_pow(427)
    print "Time taken: ", time.time() - start

    start = time.time()
    custom_pow(234)
    print "Time taken: ", time.time() - start
