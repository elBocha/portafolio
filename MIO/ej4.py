import funciones as f
num1 = int(input('Ingrese un primer número: '))
num2 = int(input('Ingrese un segundo número: '))
print(
    f'la potencia de la base {num1} y de exponente {num2} = {f.exponente_recursivo(num1, num2)}')
