from asyncio import constants
from collections import namedtuple

Constantes = namedtuple('Constantes', ['NOME', 'TIPO'])
constantes = Constantes('Desafio Python', "Utilizando constantes")

print(constantes.NOME)
print(constantes.TIPO)