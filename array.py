# https://www.w3schools.com/python/python_arrays.asp

a = [1,2,3,4,5,6,7,8,9]
print("Criando array...:")

# Tamanho maximo, depende da quantidade de memoria que tem em um computador.
import six
print(six.MAXSIZE)

cars = ["Ford", "Volvo", "BMW"]

#cars[2] = "Mercedes"
#cars[3] = "Mercedes"

#Acrescenta um novo item do array
cars.append("Mercedes")
cars.append("Cherry")
cars.append("Kia")

#Tira um item da lista baseado no índice
car1 = cars.pop(1)
# tira o último da lista
car2 = cars.pop()
# Remove o item expecífico.
cars.remove("Cherry")
# Remove todos os itens da lista
# cars.clear()

copy_of_cars = cars
qtd = copy_of_cars.count("Ford")
qtd2 = len(copy_of_cars)
print(qtd2)

new_cars = ["Honda", "Fiat"]
copy_of_cars.extend(new_cars) # Faz um merge na lista
copy_of_cars.insert(1, 'Yahha') # Insere um item na lista pelo indice
copy_of_cars.sort() # Ordena as informações da lista
copy_of_cars.reverse() # Inverte as informações da lista
