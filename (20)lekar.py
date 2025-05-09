import random

pocet_pacientov = 0
vysky = []
vyskyM = []
vyskyV = []
ppvysokych = 0
pvysokych = 0
npvysokych = 0

while pocet_pacientov < 100:
    vyska = int(input("Zadajte výšku pacienta: "))
    if vyska != 0:
        vysky.append(vyska)
        pocet_pacientov += 1
    else:
        break
dolna_hranica = int(input("Zadajte dolnú hranicu: "))
horna_hranica = int(input("Zadajte hornú hranicu: "))

priemerna_vyska = sum(vysky) / len(vysky)

for vyska in vysky:
    if (vyska - priemerna_vyska) < 2 and (vyska - priemerna_vyska) > -2:
        vyskyM.append(vyska)
    else:
        vyskyV.append(vyska)

for vyska in vysky:
    if vyska <= dolna_hranica:
        ppvysokych += 1
    elif vyska > dolna_hranica and vyska <= horna_hranica:
        pvysokych += 1
    elif vyska > horna_hranica:
        npvysokych += 1

print("Priemerná výška pacientov je: ", priemerna_vyska, "cm")
print("Pacienti s výškou v rozmedzí 2 cm od priemernej výšky: ", vyskyM)
print("Pacienti s výškou mimo rozmedzia 2 cm od priemernej výšky: ", vyskyV)
print("Pacienti s výškou pod dolnou hranicou: ", ppvysokych, (ppvysokych / pocet_pacientov) * 100, "%")
print("Pacienti s výškou v rozmedzí dolnej a hornej hranice: ", pvysokych, (pvysokych / pocet_pacientov) * 100, "%")
print("Pacienti s výškou nad hornou hranicou: ", npvysokych, (npvysokych / pocet_pacientov) * 100, "%")