from itertools import groupby

pixel=input("ingresa tu CMYK: ").split(" ")
contador=['']
for letra in pixel:
  if letra == contador[0]:
    continue 
  else:
    contador.append(letra)
print(' '.join(contador))

grupo= groupby(pixel)

for a in grupo:
  repetido = tuple (a[1])
  resultado = (len(repetido))
  numero= int(resultado)
  print(numero, end= ' ')