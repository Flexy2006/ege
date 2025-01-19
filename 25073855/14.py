for x in "0123456789ABCDEFGHIJKLMNO":
    n = int(f"11353{x}12", 25) + int(f"135{x}21", 25)
    if n % 24 == 0:
        print(n // 24)
