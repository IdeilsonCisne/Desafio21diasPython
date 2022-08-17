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
Situação: aprovador
---------------------
Nome: Lana
Média:  5.5
Situação: recuperação
"""

print("=========[Bem vindo ao programa de alunos]=========")
qtd = int(input("Digite a quantidade de alunos:\n"))
alunos = []
for indice in range(0, qtd):
  aluno = []
  nome = input(f"Digite o nome do {indice+1}º aluno: \n")
  aluno.append(nome)

  notas = []
  for i in range(0, 3):
    notas.append(float(input(f"Digite a nota {i+1} do(a) {nome}\n")))
  
  aluno.append(notas)
  media = sum(notas) / len(notas)
  aluno.append(media)

  if media < 5:
    situacao = "Reprovado"
  elif media >=5 and media <=7:
    situacao = "Recuperação"
  else:
    situacao = "Aprovado"

  aluno.append(situacao)
  
  alunos.append(aluno)

print("===============[Lista de Alunos]===============")
for aluno in alunos:
  print(f"Nome: {aluno[0]}")
  print(f"Notas: {aluno[1]}")
  print(f"Média: {aluno[2]}")
  print(f"Situação: {aluno[3]}")
  print("------------------------")