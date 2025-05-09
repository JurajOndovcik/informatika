pocet = 0
prospelo = 0
neprospelo = 0
priemer1 = 0

subor = open("skola/(25)maturita.txt", "r", encoding="utf-8")
for riadok in subor:
    pocet += 1
    meno, sjl, cuj, vp1, vp2 = riadok.split(" ")
    sjl = int(sjl)
    cuj = int(cuj)
    vp1 = int(vp1)
    vp2 = int(vp2)

    if sjl == 5 or cuj == 5 or vp1 == 5 or vp2 == 5:
        neprospelo += 1
    else:
        prospelo += 1

    if sjl == 1 and cuj == 1 and vp1 == 1 and vp2 == 1:
        priemer1 += 1
subor.close()

subor = open("skola/(25)maturita.txt", "a", encoding="utf-8")
subor.write(f"\n")
subor.write(f"\n")
subor.write(f"Počet žiakov: {pocet}\n")
subor.write(f"Počet žiakov, ktorí prospeli: {prospelo}\n")
subor.write(f"Počet žiakov, ktorí neprospeli: {neprospelo}\n")
subor.write(f"Počet žiakov, ktorí mali všetky predmety 1: {priemer1}\n")
subor.close()