from random import randint
import funciones as f
a1 = 2
r = -3
n = int(randint(0, 1000))
print(f'la sucicion geometrica hasta el numero {n}  es: ', f.sucesion_geometrica(
    a1, r, n))
