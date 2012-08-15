#!/usr/bin/env python
import math

n = int(raw_input())

while 1:
    n = int(math.ceil(n / 9.0));
    if n == 1:
        print "Stan wins."
        break
    n = int(math.ceil(n / 2.0));
    if n == 1:
        print "Ollie wins."
        break
