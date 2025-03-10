def f(x, y):
    if x % y == 0:
        return True
    else:
        return False
for A in range(1000, 1, -1):
    b = 0
    for x in range(100):
        if f(120, A) and ((not(f(x, A))) <= (f(x, 18) <= (not(f(x, 24))))):
                b += 1
    if b == 100:
        print(A)
        break