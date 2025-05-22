import random

pocet = int(input("Zadaj pocet studentov: "))
hranica = int(input("Zadaj hranicu: "))
kody_ziakov = []

def list(kod, body):
    l = 0
    if body >= hranica:
        vysledok = "Prijaty"
    else:
        vysledok = "Neprijaty"

    body = str(body)
    for letter in body:
        l += 1
    if l == 1:
        body += '  '
    elif l == 2:
        body += ' '
    print(f'{kod}   {body}     {vysledok}')


for i in range(pocet):
    kod = input("Zadaj kod studenta: ")
    kody_ziakov.append(kod)

print("Vysledky prijimacich skusok")
print("Kriterium prijatia: " + str(hranica) + " bodov")
print("------------------------------------------------")
print("KOD     BODY    VYSLEDOK")

for ziak in kody_ziakov:
    body = random.randint(0, 150)
    list(ziak, body)
