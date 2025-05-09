import random
dlzka_x = 0
dlzka_y = 0

pocet_dni = 0
trasa = 0

subor = open("skola/(24)medved.txt", "w")

for i in range(random.randint(1, 30)):
    subor.write(f"{random.randint(-10,10)}, {random.randint(-10,10)}\n")
subor.close()

subor = open("skola/(24)medved.txt", "r")
for line in subor:
    dlzka_x, dlzka_y = line.split(",")
    dlzka_x = int(dlzka_x)
    dlzka_y = int(dlzka_y)
    pocet_dni += 1
    trasa += (dlzka_x**2 + dlzka_y**2)**0.5
subor.close()

print(f"Počet dní: {pocet_dni}")
print(f"Celková trasa: {trasa:.2f} km") # :.2f formátovanie na 2 desatinné miesta