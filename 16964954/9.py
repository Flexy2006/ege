from itertools import product
q = 0
p = ["12", "32", "52", "72", "21", "23", "25", "27"]
for x in (product('012345678', repeat=5)):
    if x[0] != "0" and x.count("3") == 2:
        for i in range(0, 4):
            if x[i]+x[i+1] not in p:
                q += 1
        
print(q)