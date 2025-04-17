
# [: coincide con cualquier caracter dentro de los corchetes]

import re

username = "rub.ius_69+"
pattern = r"[\w._%+-]+$"

match = re.search(pattern, username)
if match:
    print("Username is valid: ", match.group())
else:
    print(f"Username '{username}' is invalid.")


# buscar todas las vocales de una cadena
text = "Hola, ¿cómo estás?"
pattern = r"[aeiou]"
matches = re.findall(pattern, text, re.IGNORECASE)
print("Vocales encontradas:", matches)


