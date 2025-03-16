import ctypes
import math
ctypes.windll.kernel32.SetConsoleTitleW("Kva Calc")

print('Vlož a,b,c pre výpočet kvadratickej rovnice ax²+bx+c = 0: ')


def geta():
    global a
    try:
        a = int(input('a: '))

        if a == 0:
            print('Táto rovnica je lineárna!')
            geta()
    except:
        print('a musí byť číslo!')
        geta()

def getb():
    global b
    try:
        b = int(input('b: '))
    except:
        print('b musí byť číslo!')
        getb()

def getc():
    global c
    try:
        c = int(input('c: '))
    except:
        print('c musí byť číslo!')
        getc()

if __name__ == '__main__':

    geta()
    getb()
    getc()

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