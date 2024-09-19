a = 9**8 + 3**5 - 2
b = []
while a > 0:
    x = a % 3
    b.append(str(x))
    a //= 3
b = b[::-1]
c = ''.join(str(i) for i in b)
print(c.count("2"))#4