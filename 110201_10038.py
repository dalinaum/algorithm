#!/usr/bin/env python

import sys

while 1:
    try:
        data = raw_input()
    except (EOFError):
        break 

    ns = data.split()
    length = len(ns)          
    first = int(ns.pop(0))
    prev = first
    failure = False

    for n in ns:
        n = int(n)
        absValue = abs(n - prev)
        if absValue >= length:
            failure = True
            break
        prev = n

    if failure == True:
        print "Not Jolly"
    else:
        print "Jolly"

