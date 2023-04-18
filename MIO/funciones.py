# 1- Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un
# número dado.
def fibonachi_r(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        return fibonachi_r(numero - 1) + fibonachi_r(numero-2)

# 2-Implementar una función que calcule la suma de todos los números enteros comprendidos
# entre cero y un número entero positivo dado.


def suma_recursiva(n):
    if n == 0:
        return 0
    else:
        return n + suma_recursiva(n-1)


# 3- Implementar una función para calcular el producto de dos números enteros dados.


def producto_recursivo(a, b):
    if b == 0:
        return 0
    elif b > 0:
        return a + producto_recursivo(a, b - 1)
    elif b < 0:
        return -producto_recursivo(a, -b)


# 4-Implementar una función para calcular la potencia dado dos números enteros, el primero re-
# presenta la base y segundo el exponente.

def exponente_recursivo(a, b):
    if b == 0:
        return 0
    elif b > 0:
        return a * producto_recursivo(a, b - 1)
    elif b < 0:
        return -producto_recursivo(a, -b)

# 5- Desarrollar una función que permita convertir un número romano en un número decimal.


romano = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'd': 500, 'c': 100, 'm': 1000}


def contar_caracteres(s1):
    contador = {}
    for letra in s1:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    return contador


def validar_numero_romano(s, b):
    contador = contar_caracteres(s)
    print(
        f"La cantidad de veces que se repiten los caracteres en el string '{s}' es: ")
    for letra, cantidad in contador.items():
        print(f"'{letra}': {cantidad}")
        if (contador[letra] > 3) or (((letra) in ['v', 'l', 'd']) and contador[letra] > 1):
            b = 'true'
            return print('numero romano no valido')

    if (b == 'true'):
        return print('numero romano no valido')


def roman_to_decimal(s, b):
    if len(s) == 0:
        return 0
    elif (len(s) == 1):
        return romano[s]
    else:
        if (s[0] == 'i' and (s[1] == 'v' or s[1] == 'x')) or (s[0] == 'x' and (s[1] == 'l' or s[1] == 'c')) or (s[0] == 'c' and (s[1] == 'd' or s[1] == 'm')):
            return - romano[s[0]] + roman_to_decimal(s[1:], b)
        else:
            return romano[s[0]] + roman_to_decimal(s[1:], b)


# 6. Dada una secuencia de caracteres, obtener dicha secuencia invertida.

def invertir_secuencia(secuencia):
    if len(secuencia) == 0:
        return ""
    else:
        return secuencia[-1] + invertir_secuencia(secuencia[:-1])

# 7. Desarrollar un algoritmo que permita calcular la siguiente serie:1/1+1/2+1/3..


def suma_serie_recursiva(n):
    if n == 1:
        return 1
    else:
        return (1/n) + suma_serie_recursiva(n-1)

# 8. Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a siste-
# ma binario.


def decimal_a_binario_recursivo(decimal):
    if decimal == 0:
        return "0"
    elif decimal == 1:
        return "1"
    else:
        return decimal_a_binario_recursivo(decimal // 2) + str(decimal % 2)


# 9. Implementar una función para calcular el logaritmo entero de número n en una base b.

def logaritmo_entero_recursivo(n, b):
    if n < b:
        return 0
    else:
        return 1 + logaritmo_entero_recursivo(n // b, b)

# 10. Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.


def contar_digitos_recursivo(n):
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos_recursivo(n // 10)

# 11. Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.


def invertir_numero_recursivo(n, invertido=0):
    if n == 0:
        return invertido
    else:
        return invertir_numero_recursivo(n // 10, invertido * 10 + n % 10)

# 12. Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos
# número entero.


def mcd_euclides_recursivo(a, b):
    if b == 0:
        return a
    else:
        return mcd_euclides_recursivo(b, a % b)


# 13. Desarrollar el algoritmo de Euclides para calcular también el mínimo común múltiplo (MCM)
# de dos número entero.


def mcm(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        # Calcular el MCD utilizando el algoritmo de Euclides recursivo
        mcd = mcd_euclides_recursivo(a, b)

        # Calcular el MCM utilizando la fórmula
        mcm = (a * b) // mcd
        return mcm


# 14. Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no
# se puede convertir el número a cadena.

def suma_digitos(n):
    if n < 10:
        return n
    else:
        ultimo_digito = n % 10
        resto_numero = n // 10
        return ultimo_digito + suma_digitos(resto_numero)

# 15. Desarrollar una función que permita calcular la raíz cuadrada entera de un número entero.
# Puede utilizar una función auxiliar para que la función principal solo reciba como parámetro
# el número a calcular su raíz.
