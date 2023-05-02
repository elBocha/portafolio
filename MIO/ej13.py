import funciones as f
from random import randint
num1 = int(randint(0, 1000))
num2 = int(randint(0, 1000))
print(
    f'el minimo común multiplo de los numeros {num1} y {num2} es = {f.mcm(num1, num2)}')
