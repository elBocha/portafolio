import funciones as f
lista = [31, 24, 63, 54, 85]
buscado = 31
n = len(lista)
booleano = f.bsr(lista, n, buscado)
if booleano:
    print("El elemento está presente en la lista")
else:
    print("El elemento no está presente en la lista")
