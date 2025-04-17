
# Son colecciones de pares clave-valor, donde cada clave es única y se asocia a un valor.
# Sirven para guardar datos relacionados


# Ejemplo de diccionario
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniero",
    "estudiante": True,
    "calificaciones": [7, 8, 9],
}

# Acceder a los valores de un diccionario
print(persona["nombre"])  # Imprime "Juan"
print(persona["edad"])    # Imprime 30
print(persona["calificaciones"[2]]) # Imprime 9


# Cambiar valores al acceder
persona["edad"] = 31
persona["ciudad"] = "Barcelona"

# Eliminar una propiedad
del persona["profesion"]
print(persona)  # Imprime el diccionario actualizado

is_estudiante = persona.pop("estudiante")
print(is_estudiante)  # Imprime True
print(persona)  # Imprime el diccionario actualizado sin la clave "estudiante"


# sobreescribir un diccionario con otro diccionario
a = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
}

b = {"nombre": "Pedro", "edad": 25, "estudiante": True}
a.update(b)  # Actualiza el diccionario a con los valores de b
print(a) # Imprime {'nombre': 'Pedro', 'edad': 25, 'ciudad': 'Madrid', 'estudiante': True}


# comprobar si una clave existe en un diccionario
print("nombre" in a)  # Imprime True
print("profesion" in a)  # Imprime False

# obtener todas las claves
print(a.keys())  # Imprime dict_keys(['nombre', 'edad', 'ciudad', 'estudiante'])

# obtener todos los valores
print(a.values())  # Imprime dict_values(['Pedro', 25, 'Madrid', True])

# obtener clave y valor
print(a.items())  # Imprime dict_items([('nombre', 'Pedro'), ('edad', 25), ('ciudad', 'Madrid'), ('estudiante', True)]) 
