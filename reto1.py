Polacos= int (input("Candidatos Polacos: "))
Hungaros= int ((Polacos*2)+4)
Lituanos= int ((Polacos + Hungaros)/5)
print(Polacos, Hungaros, Lituanos)
if Lituanos in range(0,20):
  print("Uno")
if Lituanos in range(21,30):
  print("Dos")
if Lituanos in range(31,50):
  print("Tres")
if (Lituanos>50):
  print("Cuatro")