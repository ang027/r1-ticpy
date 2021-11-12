#dada una lista de los tipos de alimentos, retorne una lista con los tipos de alimentos sin repetición.

def tipos_alimentos (Tipos_de_Alimentos):
  resultado= []
  for alimento in Tipos_de_Alimentos:
    if alimento not in resultado:
      resultado.append(alimento)
  return resultado

  # dada una lista con los códigos de los alimentos que faltan, la lista de los tipos de cada alimento y un tipo de alimento (en ese orden)
# retorne una lista con los códigos de los alimentos del tipo dado que faltan
def faltantes_x_tipo (Listacodigo, Tiposalimento, el_Alimento):
  resultado= []
  for alimento in Listacodigo:
    if Tiposalimento[alimento] == el_Alimento:
      resultado.append(alimento)
  return resultado

  #dada dos listas t1 y t2 con los códigos de los alimentos de la tienda 1 y de la tienda 2,
# retorna una lista con los códigos que hay en t1 y que no hay en t2.
def cotejar_stock (t1, t2):
  resultado= []
  for alimento in t1:
    if alimento not in t2:
      resultado.append(alimento)
  return resultado

  #dada dos listas t1 y t2 con los códigos de los alimentos de la tienda 1 
#y de la tienda 2, cuenta el número de alimentos que pueden intercambiar las tiendas.

def intercambios (t1, t2):
  conteo_1 = 0
  conteo_2 = 0
  resultado = 0
  for codigo in t1:
    if codigo not in t2:
      conteo_1 +=1
  for codigo in t2:
    if codigo not in t1:
      conteo_2 +=1
  if conteo_1 <= conteo_2:
      resultado = +conteo_1
  else:
      resultado = +conteo_2
  return (resultado) 