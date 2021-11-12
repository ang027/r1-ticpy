import json

json_string = input("ingresa el pix de tu img: ")
data= json.loads(json_string)
colorescode= data
lista_comparar = input("ingresa colores: ").split(" ")
numerofinal= int(0)
letrafinal= ""
for elemento in lista_comparar:
  if elemento in colorescode:
    numerofinal += int(colorescode[elemento])
    letrafinal += elemento 
print(int(numerofinal))   
