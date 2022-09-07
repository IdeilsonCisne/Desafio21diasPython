"""
Danilo é dono de uma escola de programação, faça um programa que
solicite a quantidade de alunos, capture 3 notas de alunos, 
no final do programa, mostre um relatório identificando se os alunos
estão aprovados, reprovados ou em recuperação.

cálculo da média
média = (n1+n2+n3)/3

regra de aprovação
notas abaixo de 5 = reprovado
notas de 5 até 7 = recuperação
notas acima de 7 = aprovado

Exemplo de lista
===========[lista de alunos]===========
Nome: Danilo
Média:  7.5
Situação: aprovado
---------------------
Nome: Lana
Média:  5.5
Situação: recuperação
"""

def exec():
  aluno = []
  contador = 1

  while contador <= 3:

    if contador == 1:
      nome = input(f"Digite o nome do {contador}º aluno: ")
      aluno.append(nome)

      for nota_aluno in range(3):
        nota = int(input(f"Digite a {nota_aluno+1}ª nota do aluno: "))
        aluno.append(nota)

      media = (aluno[1] + aluno[2] + aluno[3])/3
      aluno.append(media)

      if media < 5:
        situacao = "Reprovado"
      elif media >= 5 and media <= 7:
        situacao = "Recuperação"
      else:
        situacao = "Aprovado"
      
      aluno.append(situacao)

    elif contador == 2:
      nome = input(f"Digite o nome do {contador}º aluno: ")
      aluno.append(nome)

      for nota_aluno in range(3):
        nota = int(input(f"Digite a {nota_aluno+1}ª nota do aluno: "))
        aluno.append(nota)

      media = (aluno[7] + aluno[8] + aluno[9])/3
      aluno.append(media)

      if media < 5:
        situacao = "Reprovado"
      elif media >= 5 and media <= 7:
        situacao = "Recuperação"
      else:
        situacao = "Aprovado"
      
      aluno.append(situacao)

    else:
      nome = input(f"Digite o nome do {contador}º aluno: ")
      aluno.append(nome)

      for nota_aluno in range(3):
        nota = int(input(f"Digite a {nota_aluno+1}ª nota do aluno: "))
        aluno.append(nota)

      media = (aluno[13] + aluno[14] + aluno[15])/3
      aluno.append(media)

      if media < 5:
        situacao = "Reprovado"
      elif media >= 5 and media <= 7:
        situacao = "Recuperação"
      else:
        situacao = "Aprovado"
      
      aluno.append(situacao)

    contador += 1

  print(aluno)
  print("========[lista de alunos]===========")
  for i in range(3):
    if i == 0:
      print(f"Nome: {aluno[0]}")
      print(f"Média: {aluno[4]}")
      print(f"Situação: {aluno[5]}")
    elif i == 1:
      print(f"Nome: {aluno[6]}")
      print(f"Média: {aluno[10]}")
      print(f"Situação: {aluno[11]}")
    else:
      print(f"Nome: {aluno[12]}")
      print(f"Média: {aluno[16]}")
      print(f"Situação: {aluno[17]}")

if __name__== 'main':
  exec()