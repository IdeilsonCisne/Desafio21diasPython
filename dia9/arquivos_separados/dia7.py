def exercicio():
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


if __name__ == '__main__':
  exercicio()