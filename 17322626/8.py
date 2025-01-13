from itertools import *
q = 0
for x in product("01A", repeat=8):
    if x.count("0") == 2 and x[0] != "0" and x.count("A") <= 4:
        q += 9**x.count("1")*5**(x.count("A"))
print(q)