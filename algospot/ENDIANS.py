#!/usr/bin/env python
for i in range(int(raw_input())):
    input = int(raw_input())
    print (input & (255 << 24)) >> 24 | (input & (255 << 16)) >> 8 \
            | (input & (255 << 8)) << 8 | (input & 255) << 24 
