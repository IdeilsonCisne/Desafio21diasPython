"""
Dado que você aprendeu persistência, crie um programa
para cadastro de clientes, com os campos:
Nome, email

Crie um menu para que você possa orientar o cliente da criação e 
leitura dos clientes cadastrados no disco.

1 - Cadastras
2 - Listar
3 - Sair
"""
import os
import time
import json
from os.path import exists

def verificar_existe_arquivo():
  file_exists = exists("clientes.json")

  print(f"Existe? [{file_exists}]")

  if not file_exists:
    f = open("clientes.json", "w")
    try:
      clientes_json = json.dumps([])
      f.write(clientes_json)
    except Exception as e:
      print(e)
      print("Algo deu errado na escrita do arquivo")
    finally:
      f.close()
  print("")

def cadastrar_clientes():
  nome = input("Digite o nome do cliente: ")
  email = input("Digite o e-mail do cliente: ")

  cliente = {
    "nome": nome,
    "email": email
  }

  clientes = []
  clientes.append(cliente)

  f = open("clientes.json", "w")
  try:
    cliente_json = json.dumps(clientes)
    f.write(cliente_json)
  except Exception as e:
    print(e)
    print("Algo deu errado na escrita do arquivo")
  finally:
    f.close()

def listar_cliente():
  f = open("clientes.json", "r")
  try:
    clientes_json = f.read()
    clientes = json.loads(clientes_json)

    for cliente in clientes:
      print(f"{'=' * 30}")
      print(f"Nome: {cliente['nome']}")
      print(f"Email: {cliente['email']}")

  except Exception as e:
    print(e)
    print("Algo deu errado na leitura do arquivo")
  finally:
    f.close()


while True:
  print("====== [MENU] ======")
  print("Digite uma opção: ")
  print("1 - Cadastrar clientes")
  print("2 - Listar clientes")
  print("0 - Sair")

  opcao = int(input())

  if opcao == 0:
    print("Saindo...")
    time.sleep(1)
    break
  elif opcao == 1:
    cadastrar_clientes()
  elif opcao == 2:
    verificar_existe_arquivo()
    listar_cliente()
  else:
    print("Opção inválida")