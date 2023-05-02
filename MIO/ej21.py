import funciones as f
lista = [31, 24, 63, 54, 85]
valor = 1
n = len(lista)-1
booleano = f.busqueda_binaria_recursiva(lista, valor, 0, n)
if booleano:
    print("El elemento está presente en la lista")
else:
    print("El elemento no está presente en la lista")
