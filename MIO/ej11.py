import funciones as f
from random import randint
num1 = int(randint(0, 1000))
print(
    f'El valor {num1} su inversion es {f.invertir_numero_recursivo(num1)} ')
