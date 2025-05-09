import matplotlib.pyplot as plt

subor = open("skola/(28)hlasovanie.txt", "r")
a = 0
b = 0
c = 0

while True:
    riadok = subor.readline()
    if not riadok:
        break
    if riadok == "A\n":
        a += 1
    elif riadok == "B\n":
        b += 1
    elif riadok == "C\n":
        c += 1
subor.close()

pocet = a + b + c
stlpce = [1, 2, 3]
vysky = [(a/pocet)*100, (b/pocet)*100, (c/pocet)*100]
popisky = ["A", "B", "C"]

graf = plt.bar(stlpce, vysky, tick_label = popisky,
        width = 0.8, color = ['red', 'green', 'blue'])

plt.xlabel("Možnosti")
plt.ylabel("Počet hlasov")
plt.title("Hlasovanie")

for rect in graf:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{height:.2f} %', ha='center', va='bottom')

print("A: ", a)
print("B: ", b)
print("C: ", c)

plt.show()