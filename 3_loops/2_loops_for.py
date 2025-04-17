
# Permite repetir un bloque de código un número determinado de veces

# Iterar sobre una lista
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)


# Iterar sobre cualquier cosa
cadena = "Angela"
for caracter in cadena:
    print(caracter)


# enumerate(). Permite obtener el índice y el valor al mismo tiempo
numeros = [10, 20, 30, 40]
for indice, numero in enumerate(numeros): # primer valor es el índice y el segundo es el valor
    print(f"El número en el índice {indice} es {numero}")


# Bucles anidados
letras = ["a", "b", "c"]
numeros = [1, 2, 3]
for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}") # Imprime todas las combinaciones de letras y números


# Break
animales = ["perro", "gato", "elefante"]
for animal in animales:
    if animal == "gato":
        break # Sale del bucle cuando encuentra el gato
    print(animal)

# Continue
animales = ["perro", "gato", "elefante"]
for animal in animales:
    if animal == "gato": continue # Salta la iteración cuando encuentra el gato
    print(animal) # Imprime todos los animales excepto el gato


# Comprension de listas (list comprehension)
# Permite crear una nueva lista aplicando una expresión a cada elemento de una lista existente

animales = ["perro", "gato", "elefante"]
animales_mayusculas = [animal.upper() for animal in animales] # Convierte todos los animales a mayúsculas
print(animales_mayusculas) # Imprime ['PERRO', 'GATO', 'ELEFANTE']


# Ej list comprehension: Mostrar numeros pares
pares = [numero for numero in [1, 2, 3, 4, 5] if numero % 2 == 0] # Crea una lista de números pares del 0 al 9
