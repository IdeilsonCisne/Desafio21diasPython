""""
Jardeclenio é um empresário dono de um Zoológico e precisa
de um programa para cadastrar os seus animais
Faça um programa que persista dos dados dos animais no disco

Exemplo do escopo da classe
Animal
  ##### propriedades ####
  - numero
  - nome
  - descrição

  #### métodos ####
  - gravar
  - buscar
  - mostrar
"""
from models.animalV2 import Animal

animal1 = Animal()
animal1.numero = 1
animal1.nome = "Leão"
animal1.descricao = "O rei da selva"
animal1.gravar()

animais = Animal.buscar()
for animal in animais:
  print(f"=" * 30)
  print(f"Código: {animal.codigo}")
  print(f"Nome: {animal.nome}")
  print(f"Descrição: {animal.descricao}")

# animal = Animal.buscar_por_codigo("7d273227-120e-4b00-b6a4-3d2792c9e657") # não tem
# animal = Animal.buscar_por_codigo("f00ebc16-10e2-4b22-9d81-ab6fc2fe8524") # tem
# if animal != None:
#     print(f"codigo: {animal.codigo}")
#     print(f"Nome: {animal.nome}")
#     print(f"Descrição: {animal.descricao}")
