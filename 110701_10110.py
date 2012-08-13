#!/usr/bin/env python
import sys
import math

while 1:
    n = int(raw_input())
    if n == 0:
        sys.exit()
    sqrted = math.sqrt(n) 
    if n == sqrted * sqrted:
        print "yes"
    else:
        print "no"
