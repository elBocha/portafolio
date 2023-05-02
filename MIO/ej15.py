import funciones as f
from random import randint
for i in range(10):
    num1 = int(randint(0, 1000))
    print(
        f'la raiz cuadrada del numero {num1} es aproximado a: ', float(f.raiz_cuadrada_entera(num1)))
