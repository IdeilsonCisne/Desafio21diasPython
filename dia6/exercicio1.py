"""
Claudio é um matemático que precisa de um programa para facilitar
o cálculo de uma tabuada, faça um programa que solicite 1 número
e crie a tabuada do mesmo, exemplo:

Digite um número para calcular a tabuada?
5

1 x 5 = 5
2 x 5 = 10
...
10 x 5 = 50
"""

print(" ====================================================== ")
print(" ================= [Cálculo de tabuada] =============== ")
print(" ==================== [Forma MANUAL] ================== ")
print(" ====================================================== ")

numero = int(input("Digite um número para calcular: "))

print(f"1 x {numero} = {1 * numero}")
print(f"2 x {numero} = {2 * numero}")
print(f"3 x {numero} = {3 * numero}")
print(f"4 x {numero} = {4 * numero}")
print(f"5 x {numero} = {5 * numero}")
print(f"6 x {numero} = {6 * numero}")
print(f"7 x {numero} = {7 * numero}")
print(f"8 x {numero} = {8 * numero}")
print(f"9 x {numero} = {9 * numero}")
print(f"10 x {numero} = {10 * numero}")

print(" ====================================================== ")
print(" ================= [Cálculo de tabuada] =============== ")
print(" ===================== [Forma WHILE] ================== ")
print(" ====================================================== ")

iterador = 1
numero = int(input("Digite um número: "))
while iterador <= 10:
  print(f"{iterador} x {numero} = {iterador * numero}")
  iterador += 1


print(" ====================================================== ")
print(" ================= [Cálculo de tabuada] =============== ")
print(" ===================== [Forma FOR] ================== ")
print(" ====================================================== ")

numero = int(input("Digite um número: "))
for iterador in range(1, 11):
  print(f"{iterador} x {numero} = {iterador * numero}")