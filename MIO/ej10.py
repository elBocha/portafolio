import funciones as f
from random import randint
num1 = int(randint(0, 1000))
print(
    f'El valor {num1} tiene un total de {f.contar_digitos_recursivo(num1)} digitos')
