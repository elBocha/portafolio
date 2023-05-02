import funciones as f
from random import randint
num1 = int(randint(0, 1000))
print(f'la suma de 1/1+1/2..1/{num1} es: ', f.suma_serie_recursiva(num1))
