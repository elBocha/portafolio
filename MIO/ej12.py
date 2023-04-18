import funciones as f
num1 = int(input('Ingrese un primer número: '))
num2 = int(input('Ingrese un segundo número: '))
print(
    f'el máximo común divisor (MCD) de los numeros {num1} y {num2} es = {f.mcd_euclides_recursivo(num1, num2)}')
