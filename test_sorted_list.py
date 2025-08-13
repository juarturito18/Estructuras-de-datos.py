from sorted_simple_link_list import Nodo , Sorted_link_list 

#Creamos la lista 01 para probar su funcionamiento
lista_01 = Sorted_link_list()

#Agregamos los datos a la lista
lista_01.add_data(25)
lista_01.add_data(36)
lista_01.add_data(6)
lista_01.add_data(12)
lista_01.add_data(15)
lista_01.add_data(45)
lista_01.add_data(79)
print(lista_01)

lista_01.sort_data()
print(lista_01, "\n")

lista_02 = Sorted_link_list()
lista_02.add_data("python")
lista_02.add_data(15)
lista_02.add_data("javascript")
lista_02.add_data("c++")
lista_02.add_data("html")
lista_02.add_data("css")
lista_02.add_data("php")
print(lista_02)

lista_02.sort_data()
print(lista_02)