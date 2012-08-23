#!/usr/bin/env python
import sys

def calc(first, second):
    lenFirst = len(first)
    lenSecond = len(second)

    carry = 0
    maxCarry = 0

    while 1:
        numPartFirst = 0
        numPartSecond = 0

        if lenFirst > 0:
            numPartFirst = int(first[lenFirst - 1])
        if lenSecond > 0:
            numPartSecond = int(second[lenSecond - 1])
        if lenFirst <= 0 or lenSecond <= 0:
            if carry == 0:
                break

        n = numPartFirst + numPartSecond + carry
        carry = 0

        if n >= 10:
            carry = 1
            maxCarry += 1

        lenFirst -= 1
        lenSecond -= 1

    if maxCarry == 0:
        print "No carry operation."
    else:
        print "{0} carry operation.".format(maxCarry)

while 1:
    countOfCarry = 0

    try:
        numbers = raw_input()
        splitted = numbers.split()
    except (EOFError):
        sys.exit()

    if len(splitted) != 2 or (splitted[0] == "0" and splitted[1] == "0"):
        sys.exit()

    calc(splitted[0], splitted[1])

