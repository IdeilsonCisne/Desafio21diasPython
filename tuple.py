lista_aberta = []
lista_aberta.append("Ideilson")
lista_aberta.append("Cisne")
lista_aberta.append("Victória")

print(type(lista_aberta))
print(lista_aberta)

print("-"*50)

lista_fechada = ("Nascimento", "Cisne", "Victória")
print(type(lista_fechada))
print(lista_fechada)

print("-----------[Cast de tuple para lista e vice versa]-----------------")
lista_fechada = list(lista_fechada)
print(lista_fechada)
lista_fechada.append("Outro valor")
print(lista_fechada)

print("-"*50)

lista_fechada = tuple(lista_fechada)
print(type(lista_fechada))
print(lista_fechada)