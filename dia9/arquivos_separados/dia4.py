def exercicio():
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

if __name__ == '__main__':
  exercicio()