def fu(a,m):
    if a<=19: return m%2==0
    if m==0:return 0
    h=[fu(a-1,m-1)]
    if a % 3 == 0:
        h.append(fu(a//3,m-1))
    else:
        h.append(fu(a-2,m-1))
    if a % 5 == 0:
        h.append(fu(a//5,m-1))
    else:
        h.append(fu(a-3,m-1))
    return any(h) if (m-1)%2==0 else all(h)

print(19,[s for s in range(20,100) if not fu(s, 1) and fu(s,2)])
print(20,[s for s in range(20,100) if not fu(s,1) and fu(s,3)])
print(21,[s for s in range(20,100) if not fu(s,2) and fu(s,4)])
