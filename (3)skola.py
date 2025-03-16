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
    global jeprvocislo
    for i in range(2, n):
        if n % i == 0:
            jeprvocislo = False
        else:
            jeprvocislo = True

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
    print(jeprvocislo)
else:
    print("Neplatná možnosť")
