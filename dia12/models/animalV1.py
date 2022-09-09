
import os
import time
import json
from os.path import exists

class Animal():
  def __init__(self):
    self.numero = ""
    self.nome = ""
    self.descricao = ""

  def verificar_existe_arquivo(self):
    file_exists = exists("clientes.json")

    print(f"Existe? [{file_exists}]")

    if not file_exists:
      f = open("animais.json", "w")
      try:
        animais_json = json.dumps([])
        f.write(animais_json)
      except Exception as e:
        print(e)
        print("Algo deu errado na escrita do arquivo")
      finally:
        f.close()
    print("")


  def gravar(self):
    self.numero = str(input("Digite o númedo do animal: "))
    self.nome = str(input("Digite a espécie do animal: "))
    self.descricao = str(input("Digite a descrição do animal: "))

    animal = {
      "Número": self.numero,
      "Nome": self.nome,
      "Descrição": self.descricao
    }

    animais = []
    animais.append(animal)

    f = open("animais.json", "w")
    try:
      animal_json = json.dumps(animais)
      f.write(animal_json)
    except Exception as e:
      print(e)
      print("Algo deu errado na escrita do arquivo")
    finally:
      f.close()

  def buscar(self):
    ""

  def mostrar(self):
    f = open("animais.json", "r")
    try:
      animais_json = f.read()
      animais = json.loads(animais_json)

      for animal in animais:
        print(f"{'=' * 30}")
        print(f"Número: {animal['numero']}")
        print(f"Nome: {animal['nome']}")
        print(f"Descrição: {animal['descricao']}")

    except Exception as e:
      print(e)
      print("Algo deu errado na leitura do arquivo")
    finally:
      f.close()


obj = Animal()

while True:
  print("====== [MENU] ======")
  print("Digite uma opção: ")
  print("1 - Cadastrar animais")
  print("2 - Mostrar animais")
  print("3 - Buscar animais")
  print("0 - Sair")

  opcao = int(input())

  if opcao == 0:
    print("Saindo...")
    time.sleep(1)
    break
  elif opcao == 1:
    obj.gravar()
  elif opcao == 2:
    obj.verificar_existe_arquivo()
    obj.mostrar()
  else:
    print("Opção inválida")