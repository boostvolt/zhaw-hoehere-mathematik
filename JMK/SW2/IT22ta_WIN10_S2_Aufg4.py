# Aufgabe 4 a)
def eps():
    n = 1
    while 1 + 2 ** (-n) != 1:
        n += 1

    return 2 ** (-n)


print(eps())


# Aufgabe 4 b)
def qmin():
    n = 1.0
    while 1 + (2**n) != (2**n):
        n += 1

    return 2**n


print(qmin())
