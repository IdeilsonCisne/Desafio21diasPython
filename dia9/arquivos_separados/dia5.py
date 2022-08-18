import utils

def exercicio():
  print(" ===================================================== ")
  print(" =========== Sistema para Média Aritmética =========== ")
  print(" ===================================================== ")

  print("Olá aluno, digite seu nome: ")
  nome = input()

  print("Digite a sua primeira nota: ")
  nota1 = float(input())

  print("Digite a sua segunda nota: ")
  nota2 = float(input())

  print("Digite a sua terceira nota: ")
  nota3 = float(input())

  media = (nota1 + nota2 + nota3) / 3

  utils.limpar_tela()

  print(" ===================================================== ")
  print(" ================ Sua Média Aritmética =============== ")
  print(" ===================================================== ")

  if media < 5:
    print(f"Sua nota é {media}\nAluno reprovado")
  elif media >= 5 and media <= 7:
    print(f"Sua nota é {media}\nAluno está em recuperação")
  else:
    print(f"Sua nota é {media}\nAluno está Aprovado")


if __name__ == '__main__':
  exercicio()