rodne_cislo = input("Zadajte rodné číslo (RRMMDDXXXX): ")
den = 0
mesiac = 0
rok = 0
pohlavie = ""
generacia = ""

def overenie_rodneho_cisla():
    global rodne_cislo, den, mesiac, rok, pohlavie, generacia
    if len(rodne_cislo) == 10:
        if int(rodne_cislo) % 11 == 0:
            rok = int(rodne_cislo[0:2])
            if rok < 50:
                rok += 2000
            else:
                rok += 1900
            mesiac = int(rodne_cislo[2:4])
            den = int(rodne_cislo[4:6])
            print(f"{den}.{mesiac}.{rok}  ")

            if mesiac - 50 > 0:
                pohlavie = "Žena"
            else:
                pohlavie = "Muž"
            print(f"{pohlavie}")

            if 1928 <= rok <= 1945:
                generacia = "tichá generácia"
            elif 1946 <= rok <= 1964:
                generacia = "baby boomers" 
            elif 1965 <= rok <= 1980:
                generacia = "generácia X"
            elif 1981 <= rok <= 1996:
                generacia = "generácia Y"
            elif 1997 <= rok <= 2010:
                generacia = "generácia Z"
            elif 2011 <= rok <= 2025:
                generacia = "generácia alfa"
            else:
                generacia = "neznáma generácia"

            print(f"{generacia}")

    else:
        print("Neplatné rodné číslo.")
overenie_rodneho_cisla()