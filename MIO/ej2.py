import funciones as f
from random import randint
num1 = int(randint(0, 1000))
print(
    f'la suma de todos los numeros comprendidos entre 0 y {num1} es = {f.suma_recursiva(num1)}')
