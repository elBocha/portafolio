import funciones as f
from random import randint
num1 = int(randint(0, 1000))
num2 = int(randint(0, 1000))
print(
    f'el producto de los numeros {num1} y {num2} = {f.producto_recursivo(num1, num2)}')
