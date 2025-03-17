from itertools import *
q = 0
for x in product("ABCDX", repeat=4):
    if x.count('X') == 1:
        q += 1
print(q)