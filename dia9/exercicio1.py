"""
O professor Danilo, necessita organizar os exercícios passados no desafio
de python, com isso deseja que seus alunos faça um programa utilizando
funções para organizar todos os exercícios passados em 1 menu.
Ou seja, crie um programa que organize os exercícios em funções
dos dias 2,3,4,5,6,7,8
e acesso o exercício através de uma organização em menu.
"""
import os
import time

def exercicio_d2():
  print(" ================= Bem vindo ao sistema de cadastros ================= ")
  print("Digite seu nome: ")
  nome = input()
  print("Digite seu telefone: ")
  telefone = input()
  print("Digite seu endereço: ")
  endereço = input()

  os.system('clear')

  print(" ================= Programa de formatação de dados ================= ")
  print("Nome:" + nome)
  print("Telefone:" + telefone)
  print("Endereço:" + endereço)
  print(" =================================================================== ")


def exercicio_d3():
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


def exercicio_d4():
  print("================== Sistema para calcular números ==================")
  print("Digite seu nome: ")
  nome = input()

  print("Digite o primeio número:")
  numero1 = float(input())

  print("Digite o segundo número:")
  numero2 = float(input())

  print("Digite o terceiro número:")
  numero3 = float(input())

  print("Digite o quarto número:")
  numero4 = float(input())

  soma = numero1 + numero4
  multiplicacao = numero2 * numero3

  resultado_soma_multiplicacao = soma + multiplicacao

  if resultado_soma_multiplicacao > 100:
    print(f"O resultado alcançado foi {resultado_soma_multiplicacao}, parabéns!!")
  elif resultado_soma_multiplicacao <= 100:
    print(f"O resultado alcançado foi {resultado_soma_multiplicacao}, e ficou abaixo da expectativa.")


def exercicio_d5():
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

  os.system('clear')

  print(" ===================================================== ")
  print(" ================ Sua Média Aritmética =============== ")
  print(" ===================================================== ")

  if media < 5:
    print(f"Sua nota é {media}\nAluno reprovado")
  elif media >= 5 and media <= 7:
    print(f"Sua nota é {media}\nAluno está em recuperação")
  else:
    print(f"Sua nota é {media}\nAluno está Aprovado")


def exercicio_d6():
  i = 0
  while i != 3:
    print(" ====================================================== ")
    print(" ================== [MENU INTERATIVO] ================= ")
    print(" ====================================================== ")
    print("\n")
    print(" 1 - Execute a tabuada ================================ ")
    print(" 2 - Execute a tabuada com iterador =================== ")
    print(" 3 - Sair do programa ================================= ")
    escolha = int(input("Digite a opção desejada: "))
    os.system("clear")

    if escolha == 1:
      iterador = 1
      numero = int(input("Digite um número para calcular a tabuada: "))
      while iterador <= 10:
        print(f"{iterador} x {numero} = {iterador * numero}")
        iterador += 1
    elif escolha == 2:
      numero = int(input("Digite um número multiplicador para calcular a tabuada: "))
      iterador = int(input("Digite quantas vezes deseja multiplicar: "))

      i = 1
      while i <= iterador:
        print(f"{i} x {numero} = {i * numero}")
        i += 1
    elif escolha == 3:
      print("Saindo do programa...")
      break
    time.sleep(5)
    os.system("clear")


def exercicio_d7():
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


def exercicio_d8():
  lista_de_aluno = []
  quantidade_de_notas = 3

  os.system("clear")

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


while True:
  print("====== [Bem-vindo aos exercícios do desafio de Python] ======")
  print("Digite uma opção: ")
  print("1 - Exercício do dia 2")
  print("2 - Exercício do dia 3")
  print("3 - Exercício do dia 4")
  print("4 - Exercício do dia 5")
  print("5 - Exercício do dia 6")
  print("6 - Exercício do dia 7")
  print("7 - Exercício do dia 8")
  print("0 - Para sair do programa!")

  opcao = int(input())
  os.system("clear")

  if opcao == 0:
    print("Saindo...")
    time.sleep(2)
    break
  elif opcao == 1:
    exercicio_d2()
  elif opcao == 2:
    exercicio_d3()
  elif opcao == 3:
    exercicio_d4()
  elif opcao == 4:
    exercicio_d5()
  elif opcao == 4:
    exercicio_d6()
  elif opcao == 4:
    exercicio_d7()
  elif opcao == 4:
    exercicio_d8()
  else:
    print("Opção inválida")

  time.sleep(2)
  os.system("clear")