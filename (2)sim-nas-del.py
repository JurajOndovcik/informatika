def getA():
    global A
    A = input('Vlož A: ')
    try:
        A = int(A)
    except:
        print('A nie je číslo')
        getA()

def getB():
    global B
    B = input('Vlož B: ')
    try:
        B = int(B)
    except:
        print('B nie je číslo')
        getB()

def main():
    global možnosť
    global A
    global B
    možnosť = input(' \nVyber možnosť:\n[1] Simulácia násobenia\n[2] Simulácia delenia\nMožnosť: ')
    if možnosť == '1':
        print(' \nSimulácia násobenia:')
        tempB = ''
        for i in range(B):
            tempB += str(A)
            if i < B - 1:
                tempB += ' + '
        print(f'{A} * {B} = {tempB} = {A * B}')
    elif možnosť == '2':
        print(' \nSimulácia delenia:')
        pocet = 0
        if A < B:
            print(f'{A} : {B} = {pocet} (zv.) {A % B}')
        elif A == B:
            print(f'{A} : {B} = 1 (zv.) 0')
        else:
            tempA = A
            while tempA > B:
                print(f'{tempA} - {B} = {tempA - B}')
                tempA -= B
                pocet += 1
            print(f'{A} : {B} = {pocet} (zv.) {tempA}')
    else:
        print('Zlá možnosť')
        main()

if __name__ == '__main__':
    getA()
    getB()
    main()
