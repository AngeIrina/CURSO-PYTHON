
# Se utilian para especificar cuantas ocurrencias de un caracter o grupo de caracteres se deben encontrar en una cadena 

import re

# *: puede aparecer 0 o mas veces
text = "abbbbc"
pattern = "a*" 
matches = re.findall(pattern, text)
print(matches)

# +: puede aparecer 1 o mas veces
text = "abbbb aaa aa c a"
pattern = "a+"
matches = re.findall(pattern, text)
print(matches)


# ? : puede aparecer 0 o 1 vez
text = "abbbbcb"
pattern = "a?b"
matches = re.findall(pattern, text)
print(matches)

# {n}: debe aparecer exactamente n veces
text = "aaaabbbb aa aaaacb"
pattern = "a{3}" # 3 a consecutivos
matches = re.findall(pattern, text)
print(matches)

# {n, m}: debe aparecer entre n y m veces
text = "aaaabbbb aa aaaacb"
pattern = "a{2,4}" # entre 2 y 4 a consecutivos
matches = re.findall(pattern, text)
print(matches) 

# Ej: encontrar palabras de de 2 a 4 letras a consecutivas
words = "casa barco ala vaca azul"
pattern = "a{2,4}" # entre 2 y 4 a consecutivos
matches = re.findall(pattern, words)
print(matches)

# {n,}: debe aparecer al menos n veces
text = "aaaabbbb aa aaaacb"
pattern = "a{2,}" # al menos 2 a consecutivos
matches = re.findall(pattern, text)
print(matches)