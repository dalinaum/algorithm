#!/usr/bin/env python
import math
for i in range(int(raw_input())):
    n = int(raw_input())
    if n <= 1 or n >= 500000:
        continue
    d = [1]
    sqrted = int(math.sqrt(n))
    for x in range(2, sqrted):
        if n % x == 0: 
            d.append(x)
            d.append(n/x)
    if sqrted ** 2 == n:
            d.append(sqrted)
    if sum(d) > n:
        max = 2 ** len(d) - 1
        x = 2
        while x < max + 1:
            total = 0
            for y in range(len(d)):
                if ((2 ** y) & x != 0):
                    total += d[y]
                    if total > n:
                        break
            if total == n:
                break  
            x += 1
        if total == n:
            print "not weird"
        else:
            print "weird" 
    else:
        print "not weird"
