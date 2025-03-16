a = int(input("Zadaj stranu a: "))
b = int(input("Zadaj stranu b: "))
c = int(input("Zadaj stranu c: "))

def jetrojuholnik():
    templist = [a, b, c]
    templist.sort()
    if templist[0] + templist[1] > templist[2]:
        print("Trojuholník je možný")
        return True
    else:
        print("Trojuholník nie je možný")
        return False

def jerovnostranny():
    if a == b == c:
        print("Trojuholník je rovnostranný")
        return True
    else:
        print("Trojuholník nie je rovnostranný")
        return False

def jepravouhly():
    if jetrojuholnik() == False or jerovnostranny() == True:
        return False
    else:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Trojuholník je pravouhlý")
            return True
        else:
            print("Trojuholník nie je pravouhlý")
            return False

jetrojuholnik()
jerovnostranny()
jepravouhly()