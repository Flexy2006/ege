q = 0
from itertools import *
for x in product("ЯРОСЛАВ", repeat=5):
    sogl = []
    gl = []
    m = ["ЯО", "ОЯ", "АЯ", "ЯА", "АО", "ОА"]
    if len(set(x)) == len(x):
        for i in x:
            if i in "ЯРСЛВ":
                sogl.append(i)
            if i in "ЯОА":
                gl.append(i)
        if len(sogl)>len(gl):
            if str(x[0]+x[1]) not in m and str(x[1]+x[2]) not in m and str(x[2]+x[3]) not in m and str(x[3]+x[4]) not in m:
                q += 1
print(q)