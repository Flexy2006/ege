def fu(a,m):
    if a>=132: return m%2==0
    if m==0:return 0
    h=[fu(a+3,m-1), fu(a+6, m-1), fu(a*3, m-1)]
    return any(h) if (m-1)%2==0 else all(h)

print(19,[s for s in range(1,131) if not fu(s, 1) and fu(s,2)])
print(20,[s for s in range(1,131) if not fu(s,1) and fu(s,3)])
print(21,[s for s in range(1,131) if not fu(s,2) and fu(s,4)])
print(3742 % (((16*1024*1024*1024*8) % (3742*3840*2160*24)) // (3840*2160*24)))