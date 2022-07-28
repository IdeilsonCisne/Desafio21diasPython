"""
Leandro tem um posto de combustível e precisa encher o tanque do posto
Faça um programa que digite a quantidade de litros do tanque combustível atual
e receba um valor para preencher o tanque de combustível deixando o mesmo cheio

e quando chegar um cliente, colocar o combustível 
depois mostrar a quantidade de litros que ficou no tanque do posto.

============== Sistema de combustível ==============
Digite a quantidade de litros padrão

Digite a quantidade de litros para preencher a quantidade total:

A quantidade de litros que ficou no posto foi: xxx

:::: Chegou um cliente, bora vender? ::::
Digite o nome do cliente:
Digite o valor que o senhor(a) xxx que deseja colocar de combustível:

:::: Ficou com xxx litros de um total de yyyy de combustível no tanque no posto ::::

"""

print(f" ============== Sistema de combustível ============== ")
print("Digite a quantidade de litros padrão:")
litro_padrao = input()

print("Digite a quantidade de litros para preencher a quantidade total:")
qtde_atual_posto = input()

print("A quantidade de litros que ficou no posto foi: " + qtde_atual_posto)

print(":::: Chegou um cliente, bora vender? ::::")
print("Digite o nome do cliente:\n")
nome = input()

print(f"Digite o valor que o senhor(a) {nome} que deseja colocar de combustível:\n")
qtde_cliente = input()

sobra = float(qtde_atual_posto) - float(qtde_cliente)

print(f":::: Ficou com {sobra} litros de um total de {qtde_atual_posto} de combustível no tanque no posto ::::")