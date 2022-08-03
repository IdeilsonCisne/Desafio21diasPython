#https://www.w3schools.com/python/python_for_loops.asp

# Eu não sei exatamente quando tenho que terminar
print("Exemplo while")
while True:
  numero = int(input("Digite 0 para sair\n"))
  print(f"Você digitou o númerop {numero}")
  if numero == 0:
    break

# Exemplo de while que poderia ser utilizado como for
i = 1
while i < 6:
  print(i)
  i += 1

# Eu sei exatamente quando começa e termina
print("Exemplo for")
inicial = int(input("Digite o número inicial\n"))
final = int(input("Digite o número final\n"))
for x in range(inicial, final+4):
  print(x)