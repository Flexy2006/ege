t = open('1000.txt').read()
t = t.replace('-', '*')
t = t.replace('*0*', '*5*')
t = t.replace('**', 'x')
t = t.replace('*0', 'x')
t = t.replace('x0', 'x')
t = t.replace('x*', 'x')
t = t.replace('*x', 'x')
a = t.split('x')
q = 0
for i in a:
    if len(i) > 3:
        q = max(q, len(i))
print(q)