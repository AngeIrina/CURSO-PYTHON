
# Casting de types 
# Transfromar un tpo de un valor a otro
# Tipado fuerte, no transforma automaticamente

print("Conversion de tipos:")

print("100" + str(2)) # convierte a string
print(2 + int("100")) # convierte a entero

print(round(2.5)) # redondea al par mas cercano, 2.5 es 2 y 3.5 es 4

print(float("100.5")) # convierte a float

print(bool(1)) # convierte a booleano, 1 es True y 0 es False
print(bool("")) # string vacio es False
print(bool(" ")) # string con espacio es True