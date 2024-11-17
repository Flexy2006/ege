from itertools import product
q = 0
for x in (product('0123456789ABCDEF', repeat=8)):
    if x[0] != "0" and x.count("0") == 2 and (x.count("0") + x.count("1") + x.count("2") + x.count("3") + x.count("4") + x.count("5") + x.count("6") + x.count("7") + x.count("8") + x.count("9")) >= 4:
        q += 1
print(q)