#!/usr/bin/env python
import sys

def calculate(l, r):
    maxLength = 0
    for i in range(l, r + 1):
        thisN = i
        thisLength = 1
        while 1:
            if thisN == 1:
                break
            elif thisN % 2 == 0:
                thisN /= 2
            else:
                thisN = thisN * 3 + 1
            thisLength += 1
        maxLength = max(maxLength, thisLength)
    print l, r, maxLength

while 1:
    try:
        n = raw_input()
        splited = n.split()
        maxLength = 0

        if len(splited) != 2:
            sys.exit()

        l = int(splited[0])
        r = int(splited[1])

        minN = min(l, r)
        maxN = max(l, r)

        if (minN < 0) or (maxN > 1000000):
            sys.exit()

        calculate(l, r)
#        for i in range(l, r + 1):
#            thisN = i
#            thisLength = 1
#            while 1:
#                if thisN == 1:
#                    break
#                elif thisN % 2 == 0:
#                    thisN /= 2
#                else:
#                    thisN = thisN * 3 + 1
#                thisLength += 1
#            maxLength = max(maxLength, thisLength)
#        print l, r, maxLength
    except (EOFError):
        break


