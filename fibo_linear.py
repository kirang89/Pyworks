#!/usr/bin/env python
#
# Using a memoization decorator hack to compute fibonacci sequence in near
# linear time
#

import sys
#Hack to increase the recursion limit
sys.setrecursionlimit(5000)


def memo(fn):
    cache = {}
    miss = object()

    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result
    return wrapper


@memo
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print fib(1000)
