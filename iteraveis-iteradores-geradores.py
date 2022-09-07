# print("--- Iteradora ---")
# lista = [2,6,7,8]

# print(type(lista))

# print(hasattr(lista, "__iter__"))

# for item in lista:
#   print(item)

# print("--- Iterável ---")
# lista_iteravel = iter(lista)
# print(hasattr(lista_iteravel, "__next__"))
# print(type(lista_iteravel))
# print(lista_iteravel)
# print(next(lista_iteravel))
# print(next(lista_iteravel))
# print(next(lista_iteravel))
# print(next(lista_iteravel))

import time

def gera_lista_dados():
  lista = []
  for n in range(50):
    lista.append(n)
    time.sleep(0.2)
  return lista

numeros = gera_lista_dados()
print(numeros)