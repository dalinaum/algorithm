#!/usr/bin/env python
for i in range(int(raw_input())):
    special = ""
    output = ""
    for j in raw_input():
        if j == '%' or (len(special) > 0 and len(special) < 3):
            special += j
            if len(special) == 3:
                if special == '%20':
                    output += " "
                elif special == '%21':
                    output += "!"
                elif special == '%24':
                    output += "$"
                elif special == '%25':
                    output += "%"
                elif special == '%28':
                    output += "("
                elif special == '%29':  
                    output += ")"
                elif special == '%2a':
                    output += "*"
                special = ""
        else:
            output += j
    print output

