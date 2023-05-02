import funciones as f
from random import randint
num1 = int(randint(0, 1000))
print(
    f'El valor en la sucesión de Fibonacci para {num1} es {f.fibonachi_r(num1)}')
