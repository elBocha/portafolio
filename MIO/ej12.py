import funciones as f
from random import randint
num1 = int(randint(0, 1000))
num2 = int(randint(0, 1000))
print(
    f'el máximo común divisor (MCD) de los numeros {num1} y {num2} es = {f.mcd_euclides_recursivo(num1, num2)}')
