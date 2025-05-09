def dokonale_cislo(cislo):
    """
    Funkcia vrati True, ak je zadane cislo dokonale, inak vrati False.
    Dokonale cislo je take, ktore je rovne sucet svojich delitelov (okrem seba).
    Priklad: 6 = 1 + 2 + 3
    """
    delitele = [i for i in range(1, cislo) if cislo % i == 0]
    return sum(delitele) == cislo

for i in range(1, 100000):
    if dokonale_cislo(i):
        print(f"{i} je dokonale cislo.")