import random
print('Hádaj na čo myslím!')
print('Myslím si číslo medzi 1 a 100!')

number = random.randint(1, 100)
guess = 0
tries = 0

def getguess():
    global guess
    global tries
    global number
    try:
        guess = int(input('Tvoj tip: '))
    except:
        print('Musíš zadať číslo!')
        getguess()

    while tries < 51:
        if guess < 1 or guess > 100:
                print('Tvoj tip musí byť medzi 1 a 100!')
                getguess()
        else:
            if guess < number:
                print('Myslím si vyššie číslo!')
                tries += 1
                getguess()
            elif guess > number:
                print('Myslím si nižšie číslo!')
                tries += 1
                getguess()
            else:
                print('Gratulujem! Uhádol si číslo!')
                print('Počet pokusov: ', tries + 1)
                break
        print('Prehral si!')
        print('Myslel som si číslo: ', number)

if __name__ == '__main__':
    getguess()