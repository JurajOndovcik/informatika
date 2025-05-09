import random

nosnost = 1200
mvytah = 0
osoby = 0

while mvytah < nosnost:
    vaha = random.randint(30, 120)
    mvytah += vaha
    osoby += 1
    print('Vstupila osoba s hmotností', vaha, 'kg')

    if mvytah > nosnost:
        mvytah -= vaha
        osoby -= 1
        print('NOSNOST JE PREKROCENA, POSLEDNY PROSIM VYSTUPTE!')
        print('OSTAVA HMOTNOST:', nosnost - mvytah, 'kg')
        print('NASTUPILO', osoby, 'OSOB')
        break
    else:
        if mvytah == nosnost:
            print('Výtah je plný, nemůžeš nastoupit.')
            break