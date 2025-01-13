def ab1(s, f):
    if s > f or s == 12:
        return 0
    elif s == f:
        return 1
    else:
        return ab1(s+1, f) + ab1(s*2, f)


def ab2(s, f):
    if s > f or s == 11:
        return 0
    elif s == f:
        return 1
    else:
        return ab2(s+1, f) + ab2(s*2, f)
print(ab2(2, 12) * ab2(12, 24) + (ab1(2, 11) * ab1(11, 24)))