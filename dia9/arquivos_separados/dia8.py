import utils

def exercicio():
  lista_de_aluno = []
  quantidade_de_notas = 3

  utils.limpar_tela()

  print("============[ CADASTRO DE NOTA ]================\n")
  quantidade_aluno = int(input("Informe a quantidade de alunos:"))
  for i in range(0, quantidade_aluno):
      media = 0
      notas = []
      situacao = "Aprovado"
      aluno = {}

      aluno["nome"] = input(f"\nInforme nome do aluno {i+1}:")

      for y in range(0, quantidade_de_notas):
          nota = 0
          notas.append(float(input(f"Digite nota {y + 1}: ")))

      media = float("{:0.2f}".format(sum(notas) / quantidade_de_notas))
      aluno["media"] = media
      aluno["notas"] = notas

      if media >= 5 and media <= 7:
          situacao = "Recuperação"
      elif media < 5:
          situacao = "Reprovado"

      aluno["situacao"] = situacao
      lista_de_aluno.append(aluno)
      del aluno

  print("\n============[ Lista de alunos ]================\n")
  for aluno in lista_de_aluno:
      for chave, valor in aluno.items():
          print(f"{chave}: {valor}")
      print("\n")
  print("===============================================\n")


if __name__ == '__main__':
  exercicio()