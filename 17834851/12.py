a = '21' * 10 + '2' * 100
q = 0
while '21' in a:
    a = a.replace('21', '5', 1)
    q += 1
    if q * 5 + a.count('1') == 34:
        print(q)