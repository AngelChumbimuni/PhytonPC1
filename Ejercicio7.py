"""
Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta.
"""

Num1 = float(input("Ingrese el primer número: "))
Num2 = float(input("Ingrese el segundo número: "))

print("-"*100)
print("1 : Mostrar una suma de los dos números ")
print("2 : Mostrar una resta de los dos números (el primero menos el segundo)")
print("3 : Mostrar una multiplicación de los dos números")
print("-"*100)

N = int(input("Ingrese la un numero del menu(1,2 o 3):")) 
if N ==1:
 print("---> " ,Num1+Num2)
elif N == 2:
 print("---> " ,Num1 - Num2)
elif N==3:
 print("---> " ,Num1 * Num2)
else:
 print("Opcion incorrecta")

    