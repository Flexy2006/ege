t = open('1001.txt').read()
t = t.replace('-0','!')
t = t.replace('0-','!')
t = t.replace('0*','!')
t = t.replace('*0','!')
t = t.replace('*-','!')
t = t.replace('**','!')
t = t.replace('-*','!')
t = t.replace('--','!')
t = t.replace('-!','!')
t = t.replace('!-','!')
t = t.replace('!*','!')
t = t.replace('*!','!')
t = t.split('!')
q = 0
for i in t:
    if len(i) > 3:
        q = max(q, len(i))
print(q)