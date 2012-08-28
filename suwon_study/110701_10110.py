#!/usr/bin/env python
import sys
import math

while 1:
    n = int(raw_input())
    if n == 0:
        sys.exit()
    if n == math.sqrt(n) ** 2:
        print "yes"
    else:
        print "no"
