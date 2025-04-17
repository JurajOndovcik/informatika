import random

vysledok = 0
body = 0

def gen_prikladu():
    print("Vypočítaj:")
    global vysledok
    global body
    for i in range(random.randint(2,10)):
        n = random.randint(1,100)
        print("+ " + str(n))
        vysledok += n
    
    print(vysledok)
    odpoved = input("Tvoja odpoveď: ")
    if odpoved == str(vysledok):
        print("Správne! + 1 bod")
        body += 1
    elif odpoved == '0':
        print('Nevedel si! + 0 bodov')
    else:
        print("Nesprávne! - 1 bodov")
        body -= 1

def main():
    global vysledok
    global body
    for i in range(10):
        vysledok = 0
        gen_prikladu()
    print('Koniec hry!')
    print("Tvoje body: " + str(body))

if __name__ == "__main__":
    main()