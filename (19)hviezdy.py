import string

def HVIEZDICKUJ(veta):
    print(veta)
    # Nahradíme interpunkčné znamienka a medzery znakom '*'
    for znamienko in string.punctuation:
        veta = veta.replace(znamienko, '*')
    veta2 = veta.replace(' ', '*')  # Nahradenie medzier
    return veta2

def POZMEN(veta, znak):
    print(veta)
    # Nahradíme interpunkčné znamienka a medzery znakom '*'
    for znamienko in string.punctuation:
        veta = veta.replace(znamienko, znak)
    veta = veta.replace(' ', znak)  # Nahradenie medzier
    return veta

print(HVIEZDICKUJ("Ahoj, ako sa máš? Dúfam, že všetko je v poriadku!"))
print(POZMEN("Ahoj, ako sa máš? Dúfam, že všetko je v poriadku!", '-'))