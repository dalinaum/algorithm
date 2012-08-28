#!/usr/bin/env python
for i in range(int(raw_input())):
    n, unit = raw_input().split()
    n = float(n)
    if unit == 'kg':
        print "%d %.4f lb" % (i + 1, (n * 2.2046))
    elif unit == 'lb':
        print "%d %.4f kg" % (i + 1, (n * 0.4536))
    elif unit == 'l':
        print "%d %.4f g" % (i + 1, (n * 0.2642))
    elif unit == 'g':
        print "%d %.4f l" % (i + 1, (n * 3.7854))

