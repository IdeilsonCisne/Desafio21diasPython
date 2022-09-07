# Aula 10 - Constantes imutável

from asyncio import constants
from collections import namedtuple

Constantes = namedtuple('Constantes', ['NOME', 'TIPO'])
constantes = Constantes('Desafio Python', "Utilizando Constantes")

print(constantes.NOME)
print(constantes.TIPO)