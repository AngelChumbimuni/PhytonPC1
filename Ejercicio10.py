"""
Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
encuentran en la posición 0, 4 y 5.
lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
Resultado esperado: ['Verde', 'Blanco', 'Negro']
"""

lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
indices_a_eliminar = [0, 4, 5]

for indice in sorted(indices_a_eliminar, reverse=True):
    del lista_muestra[indice]

print(lista_muestra)