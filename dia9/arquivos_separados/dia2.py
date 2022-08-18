import utils

def exercicio():
  print(" ================= Bem vindo ao sistema de cadastros ================= ")
  print("Digite seu nome: ")
  nome = input()
  print("Digite seu telefone: ")
  telefone = input()
  print("Digite seu endereço: ")
  endereço = input()

  utils.limpar_tela()

  print(" ================= Programa de formatação de dados ================= ")
  print("Nome:" + nome)
  print("Telefone:" + telefone)
  print("Endereço:" + endereço)
  print(" =================================================================== ")

  if __name__ == '__name__':
    exercicio()