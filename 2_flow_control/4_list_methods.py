

lista1 = ['a', 'b', 'c', 'd']

# Añade un elemeto al final
lista1.append( 'e')

# Insertar en una posicion especifica
lista1.insert(1, '@') 
print(lista1) # ['a', '@', 'b', 'c', 'd', 'e']

# Añadir varios elementos al final de la lista
lista1.extend(['f', 'g'])

# Eliminar el primer elemento de la lista
lista1.remove('@') # Elimina la primera aparicion de '@', las demas las deja. Se pasa el elemento que aparece en la lista
print(lista1) # ['a', 'b', 'c', 'd', 'e', 'f', 'g']

lista1.pop() # Elimina el ultimo elemento de la lista y lo devuelve.
lista1.pop(1) # Se puede pasar un indice para eliminar un elemento en una posicion especifica


lista1.clear() # Elimina todos los elementos de la lista.

# Eliminar un rango
lista2 = ['perro', 'gato', 'raton', 'loro', 'pez']
del lista2[1:3] # Elimina desde el indice 1 hasta el 3 (sin incluir el 3)
print(lista2) # ['perro', 'loro', 'pez'] 


# Mas metodos utiles
print('Ordenar lista modificando la original')
numbers = [5, 2, 3, 1, 4]
numbers.sort()
print(numbers) # [1, 2, 3, 4, 5]


print('Ordenar lista creando una nueva')
numbers = [5, 2, 3, 1, 4]
sorted_numbers = sorted(numbers) # Crea una nueva lista ordenada, no modifica la original
print(sorted_numbers) # [1, 2, 3, 4, 5]


print('Ordenar lista de cadena de texto')
frutas = ['pera', 'manzana', 'banana', 'kiwi']
sorted_frutas = sorted(frutas)
print(sorted_frutas) # ['banana', 'kiwi', 'manzana', 'pera']



print('Ordenar lista de cadena de texto (mezcla mayusculas y minusculas)')
# En este caso, la lista se ordena de acuerdo al valor ASCII de cada letra.
# Las mayusculas tienen un valor ASCII menor que las minusculas, por lo que se ordenan primero.
frutas = ['pera', 'Manzana', 'banana', 'kiwi']
frutas.sort(key=str.lower) # Ordena la lista ignorando mayusculas y minusculas

# Mas Metodos utiles
animals = ['perro', 'gato', 'perro' 'raton', 'loro', 'pez']
print(len(animals))
print(animals.count('perro')) # Cuenta el numero de veces que aparece un elemento en la lista
print('perro' in animals) # Devuelve True si el elemento esta en la lista, False si no