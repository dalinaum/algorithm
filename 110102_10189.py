#!/usr/bin/env python
import re
import sys

fieldCount = 1
while True:
    noM, noN = raw_input().split()
    noM = int(noM)
    noN = int(noN)

    if noM == 0 and noN == 0:
        break

    box = []

    for m in range(noM):
        p = re.compile('\.')
        input = [x for x in p.sub('0', raw_input())]
        box.append(input) 

    for m in range(noM):
        for n in range(noN):
            if box[m][n] == '*':
                if m > 0 and n > 0 and box[m - 1][n - 1] != '*':
                    box[m - 1][n - 1] = int(box[m - 1][n - 1]) + 1
                if m > 0 and box[m - 1][n] != '*':
                    box[m - 1][n] = int(box[m - 1][n]) + 1
                if m > 0 and n < noN - 1 and box[m-1][n + 1] != '*':
                    box[m - 1][n + 1] = int(box[m - 1][n + 1]) + 1
                if n > 0 and box[m][n - 1] != '*':
                    box[m][n - 1] = int(box[m][n - 1]) + 1
                if n < noN - 1 and box[m][n + 1] != '*':
                    box[m][n + 1] = int(box[m][n + 1]) + 1
                if m < noM - 1 and n > 0 and box[m + 1][n - 1] != '*':
                    box[m + 1][n - 1] = int(box[m + 1][n - 1]) + 1
                if m < noM - 1 and box[m + 1][n] != '*':
                    box[m + 1][n] = int(box[m + 1][n]) + 1
                if m < noM - 1 and n < noN - 1 and box[m + 1][n + 1] != '*':
                    box[m + 1][n + 1] = int(box[m + 1][n + 1]) + 1

    print "Field #%d" % fieldCount

    for lineList in box:
        text = ""
        for ch in lineList:
            text += ch if ch == '*' else str(ch)
        print text
    
    fieldCount += 1
