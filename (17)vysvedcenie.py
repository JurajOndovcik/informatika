
try:
    vystup = ""
    priemer = 0
    znamka = ""
    je5 = False
    pocet_znamok = 0
    with open("skola/(17)znamky.txt", "r") as subor:
        for riadok in subor:
            vystup += riadok.strip() + ", "
            priemer += int(riadok.strip())
            pocet_znamok += 1
            if int(riadok.strip()) == 5:
                je5 = True
                znamka = "neprospel"
        
        priemer /= pocet_znamok

        if je5 == False:
            if priemer >= 0 and priemer < 1.5:
                znamka = "prospel s vyznamenaním"
            elif priemer >= 1.5 and priemer <= 2:
                znamka = "prospel veľmi dobre"
            elif priemer > 2:
                znamka = "prospel"
            else:
                znamka = "chyba"
        
        
        print(vystup.strip() + ' - ' +  znamka)
except FileNotFoundError:
    print("Subor 'znamky.txt' neexistuje.")