
# Bloques de codigo reutilizables y parametizables para hacer tareas especificas

""" Definicion de funciones
def nombre_de_funcion(parametro1, parametro2, ...):
    # Bloque de codigo a ejecutar
    return valor_de_retorno (opcional)
"""

# Definicion de una funcion
def saludar():
    print("Hola")

saludar() # Llamada a la funcion

# Funcion con parametros, reutilizable y parametrizable
def saludar(nombre): # parametro es lo que acepta la funcion
    print("Hola " + nombre)

saludar("Juan") # argumento es lo que se le pasa a la funcion
saludar("Maria")


# Funcion con varios parametros
def sumar(a, b):
    suma = a + b
    return suma

resultado = sumar(5, 3)
print(resultado) # Imprime 8


# Documentar funciones con docstrings
def sumar(a, b):
    """
    Esta funcion suma dos numeros enteros y devuelve el resultado.

    :param a: Primer numero a sumar.
    :param b: Segundo numero a sumar.
    :return: La suma de a y b.
    """
    return a + b

print(sumar.__doc__) # Imprime la documentacion de la funcion


# Parametros por defecto
def multiplicar(a, b=2):
    return a * b

print(multiplicar(5)) # Imprime 10 (5 * 2)


# Argumentos por posicion
def describir_persona(nombre, edad, ciudad):
    print(f"Soy {nombre}, tengo {edad} años, y vivo en {ciudad}")

describir_persona(edad=30, ciudad="Madrid", nombre="Juan") # Argumentos son posicionales 

# Argumentos por clave
describir_persona(nombre="Juan", edad=30, ciudad="Madrid") # Argumentos son por clave

# Argumentos de longitud variable
def sumar_varios(*args): # args es una tupla
    suma = 0
    for num in args:
        suma += num
    return suma

print(sumar_varios(1, 2, 3, 4, 5)) # Imprime 15


# Argumentos de clave-valor variables (**kwargs)
def mostrar_info(**kwargs): # kwargs es un diccionario
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Juan", edad=30, ciudad="Madrid") 