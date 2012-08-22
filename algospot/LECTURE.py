#!/usr/bin/env python
for i in range(int(raw_input())):
    input = raw_input()
    print ''.join(sorted([input[j:j+2] for j in range(0, len(input), 2)]))
