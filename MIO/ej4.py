import funciones as f
from random import randint
num1 = int(randint(0, 1000))
num2 = int(randint(0, 1000))
print(
    f'la potencia de la base {num1} y de exponente {num2} = {f.exponente_recursivo(num1, num2)}')
