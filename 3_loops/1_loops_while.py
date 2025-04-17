
# Permiten ejecutar un bloque de codigo mientras una condicion sea verdadera.

# Bucle con una simple condicion
contador = 0
while contador < 5:
    print("Hola mundo")
    contador += 1 # Incrementar el contador para evitar un bucle infinito

# Bucle while con break (solo cuando no se tiene una condicion de salida)
contador = 0
while True: # Bucle infinito
    contador += 1
    print("Hola mundo")
    if contador == 5: # Condicion de salida
        break

# Bucle con continue (salta a la siguiente iteracion)
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0: # Salta la iteracion cuando el contador es 3
        continue # no muestra los numeros pares
    print(contador)

# Bucle con else (se ejecuta cuando la condicion es falsa)
contador = 0
while contador < 5:
    print(contador)
    contador += 1
    # break # Si se descomenta el break, no se ejecuta el else
else:
    print("El bucle ha terminado")


# Ejercicio: pedirle al usuario que ingrese un numero positivo

numero = -1
while numero < 0:
    numero = int(input("Ingrese un numero positivo: "))
    if numero < 0:
        print("El numero no es positivo, intente de nuevo")

print(f"El {numero} es positivo")

# Usando try y except para manejar errores
numero = -1
while numero < 0:
    try:
        numero = int(input("Ingrese un numero positivo: "))
        if numero < 0:
         print("El numero no es positivo, intente de nuevo")
    except ValueError:
        print("El valor ingresado no es un numero, intente de nuevo")

print(f"El {numero} es positivo")