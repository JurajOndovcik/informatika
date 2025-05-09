import re

veta = input('Vlozte vetu: ')
vyskyt = 0

def nahrad_mar_na_kral_na_okraji_slova(veta):
  def nahrad(match):
    global vyskyt
    slovo = match.group(0)
    if slovo.startswith('MAR'):
      vyskyt += 1
      return 'KRAL' + slovo[3:]
    elif slovo.endswith('MAR'):
      vyskyt += 1
      return slovo[:-3] + 'KRAL'
    else:
      return slovo

  return re.sub(r'\b\w*MAR\b|\bMAR\w*\b', nahrad, veta, flags=re.IGNORECASE)

print(nahrad_mar_na_kral_na_okraji_slova(veta))
print('Vyskyt:', vyskyt)