maternos= input("Inserte Genes maternos: ")
paternos= input("Inserte Genes paternos: ")
cadena_adn= input("Inserte cadena ADN: ")
mami=0
papi=0
CGA_validacion = ""

for letra in cadena_adn:
  for letraX in maternos:
    if letraX == letra:
      mami = mami + 1
for letra in cadena_adn:
  for letraY in paternos:
    if letraY == letra:
      papi = papi + 1
    if mami>papi:
      CGA_validacion = CGA_validacion + "X"
    elif papi>mami:
      CGA_validacion = CGA_validacion + "Y"  
    else:
      CGA_validacion = CGA_validacion + "N"  

print(CGA_validacion)