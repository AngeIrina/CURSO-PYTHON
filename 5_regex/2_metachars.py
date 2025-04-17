
# Meta caracteres
# Son simbolos especiales que tienen un significado especial en las expresiones regulares.

import re

# 1. . (punto): Coincide con cualquier caracter excepto el salto de línea.
text = "hola mundo, h0la de n uevo, h$la otra vez"
pattern = r"ho.a"  # Coincide con "hola", "h0la", "h$la"

matches = re.findall(pattern, text)

if matches:
    print(f"Coincidencias encontradas: {matches}")
else:
    print("No se encontraron coincidencias.")



# Buscar el punto en el texto
text = "Hola. Soy angela."
pattern = r"\."

matches = re.findall(pattern, text)
print(matches)

# \d coincide con cualqiier digito (0-9)
text = "El num es 1234567890"
found = re.findall(r"\d{9}", text)
print(found)  # ['123456789']

# \w coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)
user_name = "angela_123"
pattern = r"\w"
found = re.findall(pattern, user_name)
print(found) 

# \s coincide con cualquier espacio en blanco (espacio, tabulador, salto de línea)
text = "Hola mundo\nHola de nuevo"
pattern = r"\s"
found = re.findall(pattern, text)
print(found) 

# ^: coincide con el principio de la cadena 
user_name = "angela_123"
pattern = r"^angela"

valid = re.match(pattern, user_name)
if valid: print("El nombre de usuario es válido.")
else: print("El nombre de usuario no es válido.")


phone = "+34 123456789"
pattern = r"^\+\d{2,3}$"  # Coincide con el formato +XX XXXXXXXXX

valid = re.match(pattern, phone)

if valid: print("El número de teléfono es válido.")
else: print("El número de teléfono no es válido.")

# $: coincide con el final de la cadena
text = "Hola mundo"
pattern = r"mundo$"
valid = re.search(pattern, text)
if valid: print("La cadena termina con 'mundo'.")
else: print("La cadena no termina con 'mundo'.")


# \b: Coincide con un límite de palabra (inicio o final de una palabra).
text = "Hola mundo, hola de nuevo"
pattern = r"\bho"  # Coincide con "ho" al inicio de una palabra
matches = re.findall(pattern, text)
if matches:
    print(f"Coincidencias encontradas: {matches}")
else:
    print("No se encontraron coincidencias.")


# |: Coincide con cualquiera de las opciones separadas por el símbolo |.
text = "banana, manzana, naranja, pera, piña"
pattern = r"banana|manzana|p..a" # devuelve banana, manzana y p..a (cualquier palabra de 4 letras que empiece por p y termine en a)
matches = re.findall(pattern, text)
if matches:
    print(f"Coincidencias encontradas: {matches}")
else:
    print("No se encontraron coincidencias.")