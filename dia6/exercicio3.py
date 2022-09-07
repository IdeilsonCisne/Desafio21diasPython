"""
Faça um programa para ter um menu onde
o usuário digitando:
1 = Execute a tabuada
2 = Execute a tabuada com iterador
3 = Saia do programa
"""
import os
import time

def exec():
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

if __name__== 'main':
  exec()