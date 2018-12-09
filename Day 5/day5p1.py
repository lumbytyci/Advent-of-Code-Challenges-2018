#dabAaCBAcCcaDA 

from string import *


def collapse(s):
    char_stack = ['.']
    for u in s:
        v = char_stack[-1]
        if v != u and v.lower() == u.lower():
            char_stack.pop()
        else:
            char_stack.append(u)
    return len(char_stack) - 1 # Do not count the dot in the begining


s = open('input.txt').read().strip()
print(collapse(s))
print(min(collapse(c for c in s if c.lower() != x) for x in ascii_lowercase))

