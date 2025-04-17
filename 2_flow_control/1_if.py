
# Sentencias condicionales (if, elif, else)
# Permiten ejecutar un bloque de código si se cumple una condición.
# La condición se evalúa como True o False. 

print("Sentencia simple")
age = 18

if age >= 18:
    print("Eres mayor de edad")


(print("Sentencia condicional compuesta con else"))
age = 18

if age >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


print("Sentencia condicional compuesta con elif")
nota = int(input("Introduce la nota: "))

if nota >= 7:
    print("Aprobado")
elif nota >= 4:
    print("Regular")
elif nota >= 0:
    print("Desaprobado")
else: # no es obligatorio, pero es una buena práctica
    print("Nota inválida")


# CONDICIONES MULTIPLES (and, or, not)

edad = 18
tengo_carnet = True

if edad >= 18 and tengo_carnet:
    print("Puedes conducir")
else:
    print("No puedes conducir")


if edad >= 18 or tengo_carnet:
    print("Puedes conducir")
else:
    print("No puedes conducir")

is_weekend = False

if not is_weekend:
    print("Es un día laborable")



print("Condicionales anidados")
# Se pueden anidar condicionales dentro de otros condicionales

edad = 18
tiene_dinero = True

if edad >= 18:
    print("Eres mayor de edad")
    if tiene_dinero:
        print("Puedes comprar un coche")
else:
    print("No tienes dinero para comprar un coche")


numero = 3 # Asignacion de variable
is_tres = numero == 3 # Comparacion de variable


# TERMARIO
# Forma corta de escribir una sentencia if-else

# [ codigo si cumple la condicion ] if [ condicion ] else [ codigo si no cumple la condicion ]

edad = 17
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje) 
