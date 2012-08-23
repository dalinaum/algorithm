#!/usr/bin/env python
for i in range(int(raw_input())):
    n = int(raw_input())
    d = filter(lambda x: n % x == 0, range(1, n))
    if sum(d) > n:
        max = 2 ** len(d) - 1
        for x in xrange(2, max + 1):
            total = 0
            for y in xrange(len(d)):
                if ((2 ** y) & x != 0):
                    total += d[y]
            if total == n:
                break
        if total == n:
            print "not weird"
        else:
            print "weird"
    else:
        print "not weird"
