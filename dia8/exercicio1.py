"""
Utilizando Dict, faça:

Danilo é dono de uma escola de programação, faça um programa
solicite a quantidade de alunos, capture 3 notas de alunos
no final do programa mostre um relatório identificando se os alunos
estão aprovados, reprovados ou em recuperação

Calculo da média
media = (n1+n2+n3)/3

Regra de aprovação:
Notas abaixo de 5 = Reprovado
Notas de 5 até 7 = Recuperção
Notas acima de 7 = Aprovado

Exemplo de lista:

=============[Lista de alunos]==============
Nome: Danilo
Média: 7.5
Situação: Aprovado
-----------------------
Nome: Lana
Média: 5.5
Situação: Recuperacao
-----------------------
"""

print("=========[Bem vindo ao programa de alunos]=========")
qtd = int(input("Digite a quantidade de alunos:\n"))
alunos = {}
for indice in range(0, qtd):
  nome = input(f"Digite o nome do {indice+1}º aluno: \n")
  alunos["nome"] = nome

  notas = []
  for i in range(0, 3):
    notas.append(float(input(f"Digite a nota {i+1} do(a) {nome}\n")))
  
  alunos["notas"] = notas
  media = sum(notas) / len(notas)
  alunos["media"] = media

  if media < 5:
    situacao = "Reprovado"
  elif media >=5 and media <=7:
    situacao = "Recuperação"
  else:
    situacao = "Aprovado"

  alunos["situacao"] = situacao
  
  # alunos.append(aluno)
  # alunos["/"]

# print("===============[Lista de Alunos]===============")
# for aluno in alunos:
#   print(f"Nome: {aluno["nome"]}")
#   print(f"Notas: {aluno["notas"]}")
#   print(f"Média: {aluno[2]}")
#   print(f"Situação: {aluno[3]}")
#   print("------------------------")