from itertools import product

n = 0
for i, p in enumerate(product('АВНРЬЯ', repeat=5), 1):
    w = ''.join(p)
    if w[0] != 'Я' and w.count('Ь') < 2 and 'ЯЯ' not in w:
        n = i
print(n)