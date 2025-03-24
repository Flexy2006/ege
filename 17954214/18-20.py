def fu(a,m):
    if a>62: return m%2==0
    if m==0: return 0
    h = [fu(a+1,m-1),fu(a+4,m-1),fu(a*5,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print([s for s in range(1,63) if not(fu(s,1)) and fu(s,2)])
print([s for s in range(1,63) if not(fu(s,1)) and fu(s,3)])
print([s for s in range(1,63) if not(fu(s,2)) and fu(s,4)])