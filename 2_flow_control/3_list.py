
# Secuencias mutables de elementos. Pueden contener elementos de diferentes tipos

# Creacion de listas

list1 = [1, 2, 3] # Lista de enteros
list2 = ["a", "b", "c"] # Lista de cadenas
list3 = [1, "a", True, 2.5] # Lista de diferentes tipos
list4 = [] # Lista vacia
lista_de_lista = [[1, 2], [3, 4], [5, 6]] # Lista de listas o matriz
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz de 3x3


# Acceso a los elementos de una lista por su indice

print(list1[0]) # 1
print(list2[1]) # b
print(list3[2]) # True
print(list3[-1]) # 2.5. Si no sabes el lugar que ocupa el elemento

print(lista_de_lista[0][1]) # 2. Primer parametro: lista, segundo: elemento de la lista



# Slicing de listas
# Permite acceder a un rango de elementos de una lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]	
print(lista[0:3]) # [1, 2, 3]. Desde el 0 hasta el 3 (sin incluir el 3)
print(lista[3:]) # [4, 5, 6, 7, 8, 9]. Desde el 3 hasta el final
print(lista[:3]) # [1, 2, 3]. Desde el principio hasta el 3 (sin incluir el 3)
print(lista[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]. Desde el principio hasta el final


print(lista[::2]) # devolver indice par
print(lista[::-1]) # invertir la lista. Desde el final hasta el principio

# Modificar una lista
lista[110] = 20
print(lista) # fuera del rango, error.

# Añadir elementos a una lista
list1 = [1, 2, 3]
list1 += [4, 5] # Añadir elementos al final de la lista (mas corta y eficiente)
print(list1) # [1, 2, 3, 4, 5]


# Recuperar longitud de una lista
print("Longitud", len(list1)) 


