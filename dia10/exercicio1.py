''''
Faca um programa para calcular os valores de um pedido
para isso crie um objeto dict de pedido que tenha relacao com um objeto dict de cliente
pedido = {
    "id": 1,
    "cliente": {
        "nome": "Walter"
    },
    "itens": []
}
nesse pedido, coloque uma propriedade de itens, contendo instancias de um dict de produto
no pedido, crie uma função para calcular o valor total
e uma função para mostrar um relatório do pedido, mostrando da seguinte forma:
----------------------------------------------------------------
Pedido Id: 1
Nome: João
Valor Total: R$ 999,99
----------------------------------------------------------------
O que terá no dict de pedido:
- id
- cliente
- itens []

O que terá no dict cliente:
- Nome
- email

O que terá no dict produto:
- Nome
- descrição
- preço

OBS: Este exercício é bastante detalhado e longo. Pegar referência deste exercício em:
# https://github.com/Jo-Alves/exercicio-python-dia10.git
# https://github.com/rhsilva06/Desafio21DiasPython/blob/main/exercicio10.py
# https://github.com/walterpaulo/logica-python/tree/main/aulas/10/exercicio

'''
import os
import time

def listar_produtos():
    produtos = [
        {
            "nome": "Banana", 
            "descrição": "Um cacho de banana prata", 
            "preço": "R$ 2,50"
        },
        {
            "nome": "Uva", 
            "descrição": "Um cacho de uva roxa", 
            "preço": "R$ 8,50"
        },
        {
            "nome": "Maçã", 
            "descrição": "Uma unidade de maçã nacional", 
            "preço": "R$ 1,00"
        }
    ]
    return print(produtos)

def fazer_pedido():
    print(" ---- Bem-vindo a seção de pedidos ---- ")
    print(" ---- Por favor escolha seu pedido ---- ")

print(" ------ Calcular valores de pedido ------ ")
nome = input("Olá cliente, qual seu nome? ")
print(f"Bem-vindo {nome}!")

while True:
    print("====== [MENU] ======")
    print("Digite uma opção: ")
    print("1 - Listar produtos")
    print("2 - Fazer pedido")
    print("3 - Listar meus pedidos")
    print("0 - Sair")

    opcao = int(input())
    # os.system("clear")

    if opcao == 0:
        print("Saindo...")
        time.sleep(1)
        break
    elif opcao == 1:
        listar_produtos()
    elif opcao == 2:
        fazer_pedido()
    else:
        print("Opção inválida")