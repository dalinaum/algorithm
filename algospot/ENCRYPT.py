#!/usr/bin/env python
for i in range(int(raw_input())):
    input = raw_input()
    print ''.join([input[i] for i in range(0, len(input), 2)] + [input[i] for i in range(1, len(input), 2)])
