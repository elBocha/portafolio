import funciones as f
from random import randint
num1 = int(randint(0, 1000))
num2 = int(randint(0, 1000))
print(
    f'el logaritmo del numero entero  {num1} y base {num2} es = {f.producto_recursivo(num1, num2)}')
