n = int(input("Zadejte n: "))

def zvysok3():
    global jezvysok3
    if n % 10 == 3:
        jezvysok3 = True
    else:
        jezvysok3 = False

def delitelne12():
    global jedelitelne12
    if n % 12 == 0:
        jedelitelne12 = True
    else:
        jedelitelne12 = False

def dvojcifernecislo():
    global jedvojciferne
    if n > 9 and n < 100:
        jedvojciferne = True
    else:
        jedvojciferne = False

def jeprvocislo():
    global jeprvocisloo
    if n < 2:
        jeprvocisloo = False
    else:
        for i in range(2, int(n**0.5) + 1): #Generuje čísla od 2 po √n (vrátane), pretože ak má n nejakého deliteľa okrem 1 a n, určite je menší alebo rovný √n.
            if n % i == 0:
                jeprvocisloo = False #Ak n je deliteľné číslom i, nie je to prvočíslo → nastaví sa jeprvocisloo = False a cyklus sa preruší (break).
                break
        else:
            jeprvocisloo = True

            #n = 7
            # skúsi 2, 3 (√7 ≈ 2.64, takže int(√n)+1 = 3)
            # 7 % 2 ≠ 0
            # 7 % 3 ≠ 0
            # -> nenašiel žiadneho deliteľa, jeprvocisloo = True

možnosť = input("Zadajte možnosť: ")
if možnosť == "zvysok3":
    zvysok3()
    print(jezvysok3)
elif možnosť == "delitelne12":
    delitelne12()
    print(jedelitelne12)
elif možnosť == "dvojcifernecislo":
    dvojcifernecislo()
    print(jedvojciferne)
elif možnosť == "jeprvocislo":
    jeprvocislo()
    print(jeprvocisloo)
else:
    print("Neplatná možnosť")
