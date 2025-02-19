def fu(a,b,m):
    if a>=48 or b >= 48: return m%2==0
    if m==0:return 0
    h=[]
    if a > b:
        h.append(fu(a+1,b,m-1))
        h.append(fu(a+2,b,m-1))
        h.append(fu(a+3,b,m-1))
        h.append(fu(a,b*2,m-1))
    else:
        h.append(fu(a,b+1,m-1))
        h.append(fu(a,b+2,m-1))
        h.append(fu(a,b+3,m-1))
        h.append(fu(a*2,b,m-1))
    return any(h) if (m-1)%2==0 else any(h)

# print(19,[s for s in range(1,47) if not fu(s, 1) and fu(s,2)])
print(20,[s for s in range(1,47) if not fu(13,s,1) and fu(13,s,3)])
print(21,[s for s in range(1,47) if not fu(39,s,2) and fu(39,s,4)])