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

lista = []
contador = 1

while contador <= 3:
  aluno = []

  nome = input(f"Digite o nome do {contador}º aluno: ")
  aluno.append(nome)
  nota1 = float(input(f"Digite a {contador}ª nota: "))
  nota2 = float(input(f"Digite a {contador+1}ª nota: "))
  nota3 = float(input(f"Digite a {contador+2}ª nota: "))

  media = (nota1 + nota2 + nota3)/3
  aluno.append(media)

  if media < 5:
    situacao = "Reprovado"
  elif media >=5 and media <=7:
    situacao = "Recuperação"
  else:
    situacao = "Aprovado"
  
  aluno.append(situacao)
  lista.append(aluno)
  contador += 1
  print("-"*30)

print("===========[lista de alunos]===========")
for aluno in lista:
  print(f"Nome: {aluno[0]}")
  print(f"Média: {aluno[1]}")
  print(f"Situação: {aluno[2]}")
  print("-"*30)
