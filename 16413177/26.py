from itertools import *
q = 0
a = []
b = []
for a1, a2, a3, a4 in product("0123456789", repeat = 4):
    if int(f"1{a1}21574") % 2024 == 0:
        print(int(f"1{a1}21574"), int(f"1{a1}21574") // 2024)
    if int(f"1{a1}2157{a2}4") % 2024 == 0:
        print(int(f"1{a1}2157{a2}4"), int(f"1{a1}2157{a2}4") // 2024)
    if int(f"1{a1}2157{a2}{a3}4") % 2024 == 0:
        print(int(f"1{a1}2157{a2}{a3}4"), int(f"1{a1}2157{a2}{a3}4") // 2024)
    if int(f"1{a1}2157{a2}{a3}{a4}4") % 2024 == 0:
        print(int(f"1{a1}2157{a2}{a3}{a4}4"), int(f"1{a1}2157{a2}{a3}{a4}4") // 2024)