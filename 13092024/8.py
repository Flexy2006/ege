from itertools import product
a = list(product("АВТОР", repeat=4))
print(a.index(("Т", "А", "Р", "А")) + 1)#271