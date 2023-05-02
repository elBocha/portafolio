import funciones as f
mochila = ["comida", "agua", "sable de luz", "ropa"]
objetos_necesarios = f.usar_la_fuerza(mochila, 0)
if objetos_necesarios == 0:
    print("No se encontró el sable de luz en la mochila")
else:
    print(
        f"Se necesitaron {objetos_necesarios} objetos para encontrar el sable de luz")
