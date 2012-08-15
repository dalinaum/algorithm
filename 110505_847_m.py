#!/usr/bin/env python
n = int(raw_input())
m = 1

while 1:
    m *= 9
    if m >= n:
        print "Stan wins."
        break
    m *= 2
    if m >= n:
        print "Ollie wins."
        break

