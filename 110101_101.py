#!/usr/bin/env python
while 1:
        try:
                n = raw_input()
                splited = n.split()
                maxLength = 0
                l = int(splited[0])
                r = int(splited[1])
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
        except (EOFError):
                break