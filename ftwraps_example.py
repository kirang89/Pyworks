#!/usr/bin/python
#-*- coding:utf-8 -*-

# Simple program to illustrate use of functools wrapper
from functools import wraps


def logged(func):
    '''decorator to handle logging for any function'''
    @wraps(func)
    def logger(*args, **kwargs):
        print func.__name__, "called"
        return func(*args, **kwargs)

    return logger


@logged
def func1(a, b):
    '''Returns sum of a and b'''
    return a + b

if __name__ == '__main__':
    print func1(4, 3)

    # Though func1 is wrapped by logger, the functools.wraps() does a
    # nice job of copying over all the details like name, docs, arguments
    # list, etc so that the following two lines print exactly what
    # you'd think
    print func1.__name__    # prints func1
    print func1.__doc__     # prints "Returns sum of a and b"
