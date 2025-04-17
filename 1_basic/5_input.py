
# Permite obtenes datos del usuario por consola.

name = input("¿Cuál es tu nombre?\n")
print(f"Hola {name}, ¿cómo estás?")

age = int(input("¿Cuántos años tienes?\n"))
print(f"Tienes {age} años.")

print("Obtener multiples valores a la vez")
name, age = input("¿Cuál es tu nombre y cuántos años tienes?\n").split()
print(f"Hola {name}, tienes {age} años.")



