
# Las variables sirven para guardar datos en memoria y podes utilizarlas en cualquier parte del programa.
# Se pueden cambiar de valor en cualquier momento.
# Python es un lenguaje de tipado dinámico y fuerte.


# Para asignar una variable solo hace falta esto:
my_name = "Angela"
print(my_name)


# Se pueden reasignar. Cambiando el valor.
age = 25
print(age)

age = 30
print(age)


# Tipado dinamico, el tipo de dato se determina en tiempo de ejecucion que no tienes que declararlo explicitamente.
name = "Angela"
print(type(name)) # <class 'str'>

name = 25
print(type(name)) # <class 'int'>


# Tipado fuerte, Python no realiza conversiones de tipo automaticamente.
print("10" + 2) # TypeError

# f-string (literal de cadena de formato) para concatenar variables y cadenas de texto.
print(f"Hola {name}, tienes {age} años.") 
print(f"Hola {name}, tienes {age + 1} años.") 

#Convenciones de nombrado de variables:
mi_nombre_de_variable = "Angela" # snake_case
miNombreDeVariable = "Angela" # camelCase
MiNombreDeVariable = "Angela" # PascalCase
nombre = "Angela" # lowercase

MI_VARIABLE = "Angela" # UPPER_CASE -> constantes. No se recomienda cambiar su valor.

# Nombres no validos
# 1234_nombre = "Angela" # No puede empezar con un numero
# nombre@ = "Angela" # No puede contener caracteres especiales
# nombre espacio = "Angela" # No puede contener espacios
# nombre-espacio = "Angela" # No puede contener guiones
# nombre.espacio = "Angela" # No puede contener puntos
# no usar palabras reservadas como nombre de variable

