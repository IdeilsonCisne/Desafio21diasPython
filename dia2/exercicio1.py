# Dado que o professor Danilo, precise mostrar algumas informações 
# importantes na tela, faça um programa que capture estas informações
# e mostre na tela de forma organizada, exemplo de organização:
# ================= Programa de formatação de dados =================
# Nome: XXXXXX
# Telefone: XXXXXXXX
# Endereço: XXXXXXX
# ===================================================================
import os

def exec():

  print(" ================= Bem vindo ao sistema de cadastros ================= ")
  print("Digite seu nome: ")
  nome = input()
  print("Digite seu telefone: ")
  telefone = input()
  print("Digite seu Endereço: ")
  endereço = input()

  os.system('clear')

  print(" ================= Programa de formatação de dados ================= ")
  print("Nome:" + nome)
  print("Telefone:" + telefone)
  print("Endereço:" + endereço)
  print(" =================================================================== ")

if __name__== 'main':
  exec()