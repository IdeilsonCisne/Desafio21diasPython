import utils

def exercicio():
  print(f" ============== Sistema de combustível ============== ")
  print("Digite a quantidade de litros padrão:")
  litro_padrao = input()

  print("Digite a quantidade de litros para preencher a quantidade total:")
  qtde_atual_posto = input()

  print("A quantidade de litros que ficou no posto foi: " + qtde_atual_posto)

  print(":::: Chegou um cliente, bora vender? ::::")
  print("Digite o nome do cliente:\n")
  nome = input()

  print(f"Digite o valor que o senhor(a) {nome} que deseja colocar de combustível:\n")
  qtde_cliente = input()

  sobra = float(qtde_atual_posto) - float(qtde_cliente)

  print(f":::: Ficou com {sobra} litros de um total de {qtde_atual_posto} de combustível no tanque no posto ::::")


if __name__ == '__main__':
  exercicio()