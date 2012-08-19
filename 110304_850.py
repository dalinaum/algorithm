#!/usr/bin/env python

def makeTranDict(enc, target):
    result = {}
    if (len(target) != len(enc)):
        return None 
    for i, j in map(None, enc, target):
        if i in result and result[i] != j:
            return None
        result[i] = j
    return result

def decrypt(enc, td):
    fp = ""
    for e in enc:
        if e in td:
            fp += td[e]
    print fp

def processOneSet():
    ds = []
    text = "the quick brown fox jumps over the lazy dog"

    while 1:
        try:
            line = raw_input()
        except (EOFError):
            break

        if line == "":
            break

        ds.append(line) 

    for d in ds:
        td = makeTranDict(d, text)
        if td != None:
            break

    if td != None:
        for d in ds:
            decrypt(d, td)

n = int(raw_input()) 

for i in range(n):
    processOneSet()
