print("Digite um nome")
nome = input().lower().strip() # o lower() deixará a nome minúsculo, já o strip() removerá espaços vazios da esquerda e direita

if nome == "Victória":
  print("Encontrei o nome procurado")
elif nome == "Ideilson" or nome.find("ideilson") != -1:
  print("Encontrei o nome procurado")
else:
  print("Não encontrei o nome procurado")