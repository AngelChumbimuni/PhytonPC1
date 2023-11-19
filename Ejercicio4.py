"""
Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta N.

"""

Num = int(input("Ingrese un número entero postivo: "))
Suma = (Num*(Num+1))/2
print("La suma de todos los enteros desde 1 hasta ", Num, "  es ", Suma)