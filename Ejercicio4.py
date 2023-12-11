"""
Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta N.

"""

# Leer un entero positivo desde el usuario
N = int(input("Ingrese un entero positivo, N: "))

# Verificar si N es un entero positivo
if N <= 0:
    print("Por favor, ingrese un entero positivo.")
else:
    # Crear una cadena con la expresión de la suma
    suma_expresion = '+'.join(map(str, range(1, N + 1)))
sum = N*(N+1)/2

    # Mostrar la expresión de la suma en pantalla
print(f"La suma de todos los enteros desde 1 hasta {N} es: {suma_expresion} = {sum:.0f}")
