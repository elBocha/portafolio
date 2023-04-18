import funciones as f
num1 = input('Ingrese un número romano: ')
B = 'False'
f.validar_numero_romano(num1, B)
if B == 'False':
    print(
        f'el numero romano {num1} en decimal es {f.roman_to_decimal(num1, B)}')
