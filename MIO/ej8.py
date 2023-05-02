import funciones as f
from random import randint
num1 = int(randint(0, 1000))
print(f'el numero {num1} en binario es: ', f.decimal_a_binario_recursivo(num1))
