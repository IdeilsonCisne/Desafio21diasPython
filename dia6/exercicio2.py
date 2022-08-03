"""
Claudio é um matemático que precisa de um programa para facilitar
o cálculo de uma tabuada, faça um programa que solicite 1 número multiplicador
e 1 número do iterador. Crie a tabuada do mesmo, exemplo:
e crie a tabuada do mesmo, exemplo:

Digite um número para calcular a tabuada?
5
Digite um número para o iterador da tabuada
3

1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
"""

print(" ====================================================== ")
print(" ================= [Cálculo de tabuada] =============== ")
print(" ===================== [Forma WHILE] ================== ")
print(" ====================================================== ")

numero = int(input("Digite um número multiplicador: "))
iterador = int(input("Digite um número iterador: "))

i = 1
while i <= iterador:
  print(f"{i} x {numero} = {i * numero}")
  i += 1

print(" ====================================================== ")
print(" ================= [Cálculo de tabuada] =============== ")
print(" ===================== [Forma FOR] ================== ")
print(" ====================================================== ")

for i in range(1, iterador+1):
  print(f"{i} x {numero} = {i * numero}")
