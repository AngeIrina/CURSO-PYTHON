
# Expresiones regulares. Se usan para buscar patrones en cadenas de texto.
# Se pueden usar para validar datos, buscar y reemplazar texto, etc.

""" Por que aprender regex?
- Busqueda avanzada: busca patrones complejos en texto de forma rapida y precisa.
- Validacion de datos: valida formatos de datos como correos, telefonos, etc.
- Manipulacion de texto: permite extraer, reemplazar y modificar partes de la cadena de texto facilmente.
- 
"""


# 1. Importar el modulo re
import re
# 2. Crear un patron, cadena de texto que describe lo que queremos encontrar
pattern = "Hola"
# 3. Texto donde queremos buscar el patron
text = "Hola mundo, Hola a todos"
# 4. Usar la funcion de busqueda de regex
result = re.search(pattern, text)
# 5. Comprobar si se encontro el patron
if result:
    print("Patron encontrado:", result.group())
else:
    print("Patron no encontrado")


# grup() devuelve la cadena que coincide con el patron
print(result.group())

# start() devuelve la posicion de inicio de la coincidencia
print(result.start())

# end() devuelve la posicion de fin de la coincidencia
print(result.end())


# encontrar todas las coincidencias de un patron
# findall() devuelve una lista con todas las coincidencias
text = "Python es genial, Python es facil de aprender, Python es divertido"
pattern = "Python"
result = re.findall(pattern, text)
print("Coincidencias encontradas:", result) 


# iter() devuelve un iterador con todas las coincidencias
text = "Python es genial, Python es facil de aprender, Python es divertido"
pattern = "Python"
result = re.finditer(pattern, text)

for match in result:
    print("Coincidencia encontrada:", match.group())
    print("Posicion de inicio:", match.start())
    print("Posicion de fin:", match.end())



# Modificadores 
# Son opciones que se pueden agregar a un patron para cambiar su comportamiento

# re.IGNORECASE: Ignora mayusculas y minusculas
text = "Hola mundo, hola a todos"
pattern = "hola"
result = re.findall(pattern, text, re.IGNORECASE)
if result: print(result)


# Reemplazar el texto
# sub() reemplaza todas las coincidencias de un patron por otro texto
text = "Hola mundo, Hola a todos"
pattern = "Hola"
replacement = "Chau"

new_text = re.sub(pattern, replacement, text)
print("Texto modificado:", new_text)
