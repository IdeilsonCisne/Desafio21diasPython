print("1 - Forma de utilizar o print")

b = "um dado"
c = 1
print("2 - Forma de utilizar o print", "concatenando", b, "com outros", c)

nome = "Um nome"
print("3 - Forma de utilizar o print: " + nome)

print("4 - Forma de utilizar o print: {} de {}".format("valor1","valor2"))

print("5 - Ola Sr.{1} {0}".format("Cordeiro", "Leonardo")) # são índices, ordem dos índices, muda a ordem

print("6 - R$ {:7.1f}".format(1000.12))
print("7 - R$ {:07.2f}".format(4.11))

var = "Um valor"
print(f"8 - nova forma de utilizar {var}") # outra forma de usar o .format