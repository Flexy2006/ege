for x in "0123456789ABCDEFGHIJKL":
    n = int(f"63{x}59685", 22) + int(f"17{x}53", 22)+int(f"36{x}5", 22)
    if n % 21 == 0:
        print(n // 21)
