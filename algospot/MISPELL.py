#!/usr/bin/env python
for i in range(int(raw_input())):
    position, text = raw_input().split()
    position = int(position)
    print "%d %s" % (i + 1, text[0:position - 1] + text[position:])
