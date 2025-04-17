citatel = int(input("Zadajte citatel: "))
menovatel = int(input("Zadajte menovatel: "))

def NSD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def zakladnyTvar():
    global citatel, menovatel
    if citatel == 0:
        return 0, 1
    nsd = NSD(citatel, menovatel)
    citatel //= nsd
    menovatel //= nsd
    return citatel, menovatel

print("Zlomok v zakladnom tvare je: {}/{}".format(*zakladnyTvar()))