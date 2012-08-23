#!/usr/bin/env python
for i in range(int(raw_input().strip())):
    stack = []
    for j in raw_input().strip():
        if j == '(' or j =='{' or j =='[':
            stack.append(j)
        elif len(stack) > 0:
            last = stack[-1]
            if (last == '(' and j == ')') or \
                (last == '[' and j == ']') or \
                (last == '{' and j == '}'):
                stack.pop()
            else:
                break
        else:
            stack.append(j)
            break
    print "YES" if len(stack) == 0 else "NO" 
