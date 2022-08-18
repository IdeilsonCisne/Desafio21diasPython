"""
O professor Danilo, necessita organizar os exercícios passados no desafio
de python, com isso deseja que seus alunos faça um programa utilizando
funções para organizar todos os exercícios passados em 1 menu.
Ou seja, crie um programa que organize os exercícios em funções
dos dias 2,3,4,5,6,7,8
e acesso o exercício através de uma organização em menu.
"""
import utils
import dia2
import dia3
import dia4
import dia5
import dia6
import dia7
import dia8

while True:
  print("====== [Bem-vindo aos exercícios do desafio de Python] ======")
  print("Digite uma opção: ")
  print("[1] - Para exercício do dia 2")
  print("[2] - Para exercício do dia 3")
  print("[3] - Para exercício do dia 4")
  print("[4] - Para exercício do dia 5")
  print("[5] - Para exercício do dia 6")
  print("[6] - Para exercício do dia 7")
  print("[7] - Para exercício do dia 8")
  print("[0] - Para sair do programa!")

  opcao = int(input())
  utils.limpar_tela()

  if opcao == 0:
    print("Saindo...")
    utils.espera_em_segundos(2)
    break
  elif opcao == 1:
    dia2.exercicio()
  elif opcao == 2:
    dia3.exercicio()
  elif opcao == 3:
    dia4.exercicio()
  elif opcao == 4:
    dia5.exercicio()
  elif opcao == 5:
    dia6.exercicio()
  elif opcao == 6:
    dia7.exercicio()
  elif opcao == 7:
    dia8.exercicio()
  else:
    print("Opção inválida")

  utils.espera_em_segundos(3)
  utils.limpar_tela()