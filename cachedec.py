#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Example implementation of a cache decorator
#

try:
    import pylibmc
except ImportError:
    print "Install pylibmc first"
    import sys
    sys.exit(0)


def cache(func):
    def wrapper(a, b):
        mc = pylibmc.Client(["127.0.0.1"])
        key = a + b
        cached_res = mc.get(key)
        if cached_res:
            print "from cache"
            res = cached_res
        else:
            res = func(int(a), int(b))
            mc.set(key, str(res))
        return res
    return wrapper


@cache
def multiply(a, b):
    return a * b


if __name__ == '__main__':
    a = raw_input('Enter 2 numbers seperated by a comma: ')
    numbers = a.split(',')
    print multiply(*numbers)
