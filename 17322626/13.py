a = 0
for i in range(2048):
    b = bin(int(i))[2:]
    if (8 + b.count('1')) % 5 != 0:
        a += 1
print(a)