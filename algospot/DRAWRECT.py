#!/usr/bin/env python
import sys
for i in range(int(raw_input())):
    maxX = 0
    maxY = 0
    minX = sys.maxint
    minY = sys.maxint
    xs = []
    ys = []
    for j in range(3):
        x, y = raw_input().split()
        x = int(x)
        y = int(y)
        xs.append(x)
        ys.append(y)
        maxX = x if x > maxX else maxX
        maxY = y if y > maxY else maxY
        minX = x if x < minX else minX
        minY = y if y < minY else minY
    tl = False
    tr = False
    bl = False
    br = False
    for j in range(3):
        if xs[j] == minX and ys[j] == minY:
            bl = True
        elif xs[j] == minX and ys[j] == maxY:
            tl = True
        elif xs[j] == maxX and ys[j] == maxY:
            tr = True
        else:
            br = True
    if tl == False:
        print "%d %d" % (minX, maxY)
    elif tr == False:
        print "%d %d" % (maxX, maxY)
    elif bl == False:
        print "%d %d" % (minX, minY)
    else:
        print "%d %d" % (maxX, minY)
 
