"""
Danilo, um professor de tecnologia, empresário no torne-se um programador,
deseja um software que ajude a calcaular a média de nota de um aluno, 
faça um programa onde solicite o nome do aluno, tres notas do mesmo
depois faça o cálculo para saber se o mesmo está aprovado:

regras para a aprovação

se o aluno tirou a média aritmética < 5, aluno está reprovado.
se o aluno tirou a média aritmética entre 5 e 7, aluno está em recuperação.
se o aluno tirou a média aritmética > 7, aluno está aprovado.

utilize a sua criatividade e agrade o seu professor, com a melhor experiência.

"""
import os

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

# if media > 7:
#   print(f"Sua nota é {media}\nAluno está Aprovado")
# elif media >= 5 or media <= 7:
#   print(f"Sua nota é {media}\nAluno está em recuperação")
# else:
#   print(f"Sua nota é {media}\nAluno reprovado")

if media < 5:
  print(f"Sua nota é {media}\nAluno reprovado")
elif media >= 5 and media <= 7:
  print(f"Sua nota é {media}\nAluno está em recuperação")
else:
  print(f"Sua nota é {media}\nAluno está Aprovado")
