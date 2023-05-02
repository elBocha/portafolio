import funciones as f
from random import randint
num1 = int(randint(0, 1000))
print(f'el numero {num1} con sus digitos sumados es: ', f.suma_digitos(num1))
