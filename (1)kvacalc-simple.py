import math

print('Vlož a,b,c pre výpočet kvadratickej rovnice ax²+bx+c = 0: ')


a = int(input('a: '))
if a == 0:
    print('Táto rovnica je lineárna!')

else:
    b = int(input('b: '))
    c = int(input('c: '))
    
    diskriminant = ((b**2) + (-4*a*c))
    print(diskriminant)
    
    if diskriminant >= 0:
        x1 = round((-b + math.sqrt(diskriminant)) / 2*a, 2)
        x2 = round((-b - math.sqrt(diskriminant)) / 2*a, 2)
        print(f'Korene sú {x1} a {x2}')
    elif diskriminant == 0:
        x = round((-b + math.sqrt(diskriminant)) / 2*a, 2)
        print(f'Jediný koreň rovnice je {x}')
    else:
        print('Diskriminant je záporný, rovnica nemá riešenie!')