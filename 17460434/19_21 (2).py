def fu(a,b,m):
    if a+b>=82: return m%2==0
    if m==0:return 0
    h=[fu(a+1,b,m-1),fu(a*4,b,m-1),fu(a,b+1,m-1),fu(a,b*4,m-1)]
    return any(h) if (m-1)%2==0 else all(h)

print(19,[s for s in range(1,77+1) if fu(4,s,2)])
print(20,[s for s in range(1,77+1) if not fu(4,s,1) and fu(4,s,3)])
print(21,[s for s in range(1,77+1) if not fu(4,s,2) and fu(4,s,4)])
