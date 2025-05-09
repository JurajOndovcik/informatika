print("Hlasovanie")
print("[A] - Hlasujem A\n[B] - Hlasujem B\n[C] - Hlasujem C\n")

subor = open("skola/(28)hlasovanie.txt", "a")
def hlasovanie():
    hlas = input("Zadaj svoj hlas: ").upper()
    if hlas == "A":
        subor.write("A\n")
        hlasovanie()
    elif hlas == "B":
        subor.write("B\n")
        hlasovanie()
    elif hlas == "C":
        subor.write("C\n")
        hlasovanie()
    elif hlas == "Q":
        subor.close()
        print("Hlasovanie ukončené.")
        return
    else:
        print("Neplatná možnosť!")
        hlasovanie()

hlasovanie()
subor.close()