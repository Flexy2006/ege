a = open('1002.txt').readline()
w = []
q = ['EQ','EW','ER','ET','EY','EU','EI','EO','EP','EA','ES','ED','EF','EG','EH','EJ','EK','EL','EZ','EX','EC','EV','EB','EN','EM']
for i in q:
    w.append(a.index(i))
print(max(w))