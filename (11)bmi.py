pocet_ziakov = 0
podvaha = 0
obezny = 0
subor = open('skola/(11)bmi.txt', 'r')
riadok = subor.readline()
while riadok != '':
    hmotnost, vyska = map(float, riadok.split())
    bmi = hmotnost / (vyska * vyska)
    print(round(bmi, 2))
    pocet_ziakov += 1
    if bmi < 18.5:
        podvaha += 1
    elif 18.5 <= bmi < 25:
        pass
    elif 25 <= bmi < 30:
        obezny += 1
    else:
        obezny += 1
    riadok = subor.readline()
subor.close()
print('Pocet ziakov:', pocet_ziakov)
print('Pocet podvaznych:', podvaha)
print('Pocet obeznych:', (obezny / pocet_ziakov) * 100, '%')