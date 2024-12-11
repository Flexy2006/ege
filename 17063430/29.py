from itertools import *
q = 0
a = []
b = []
for a1, a2, a3, a4 in product("0123456789", repeat = 4):
    if int(f"3{a1}12{a2}14{a3}5") % 1917 == 0:
        print(int(f"3{a1}12{a2}14{a3}5"), int(f"3{a1}12{a2}14{a3}5") // 1917)
    if int(f"3{a1}12{a2}14{a3}{a4}5") % 1917 == 0:
        print(int(f"3{a1}12{a2}14{a3}{a4}5"), int(f"3{a1}12{a2}14{a3}{a4}5") // 1917)