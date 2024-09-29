a = 25**5 + 5**14 - 5
q = ""
while a > 0:
    q += str(a%5)
    a = a // 5
b = q[::-1]
b = list(map(int, str(b)))
print(b.count(4))#9