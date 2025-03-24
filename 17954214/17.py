a = open('1001.txt')
b = [int(i) for i in a]
mina = 1000000000
maxa = 0
for k in b:
    if k % 21 == 0:
        mina = min(mina, k)
q = 0
for j in range(0, len(b) - 1):
    if b[j] % mina == 0 or b[j+1] % mina == 0:
        q += 1
        maxa = max(maxa, b[j] + b[j+1])
print(q, maxa)