q = 0
for A in range(300):
    a = True
    for x in range(300):
        for y in range(300):
            if not(((x < 6) <= (x**2 < A)) and ((y**2 <= A) <= (y <= 6))):
                a = False
                break
    if a == True:
        q += 1
print(q)