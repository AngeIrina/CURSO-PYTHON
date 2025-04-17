
# Permite crear una lista de números enteros en un rango específico.
# Util para el for

nums = range(10)  # No crea una lista, solo un objeto iterable. Crea los números sobre la marcha.


# Generando una secuencia de numeros del 0 al 9
for nums in range(10):
    print(nums) 

# range(inicio, fin, paso)
for nums in range(0, 10, 2):  # números del 0 al 9 con un paso de 2
    print(nums)

# Numeros negativos
for nums in range(-10, -1):  # números del -10 al -2
    print(nums)


# Range y list
nums = range(5)
list_of_nums = list(nums)
print(list_of_nums)  # [0, 1, 2, 3, 4]


for _ in range(5):
    print(_)