from itertools import *
q = 0
for x in product("УОА", repeat=6):
    q += 1
    if ''.join(str(i) for i in x) == "ОУУУОО":
        print(q)
        break
