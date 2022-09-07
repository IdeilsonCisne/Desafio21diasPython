# Aula 10 - Revisar este assunto

# print("--- Iteradora ---")
# lista = [2,6,7,8]

# print(type(lista))

# print(hasattr(lista, "__iter__")) # mostra se a lista/array tem o método "__iter__"

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
import os

print("----- Segura o processamento ----")
print("----- Processando... ----")

def gera_lista_dados():
  lista = []
  for n in range(50):
    lista.append(n)
    time.sleep(0.2)
  return lista

numeros = gera_lista_dados()
for item in numeros:
  print(item)

print("----- Fim da ação ----")
os.system('clear')
time.sleep(3)


# Gerador - Execução preguiçosa, só chama o resultado quando executa
print("----- Não segura o processamento ----")

def gera_lista_dados():
  lista = []
  for n in range(50):
    yield n # Armazena os dados dentro do yield
    time.sleep(0.2)
  return lista

numeros = gera_lista_dados()
for item in numeros:
  print(item)
# ou usando o método next
# print(next(numeros))
# print(next(numeros))
# print(next(numeros))

# gera uma lista com 1000 índices
lista_comum = [i for i in range(1000)]
print(lista_comum)
print(sys.getsizeof(lista_comum)) # retorna o tamanho em bytes

# gera um objeto geradora
lista_geradora = (i for i in range(1000))
print(lista_comum)
print(sys.getsizeof(lista_geradora))
