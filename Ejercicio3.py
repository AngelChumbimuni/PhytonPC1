"""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
último pedido y calcule el peso total del paquete que será enviado"""
Cant_Payaso = float(input("Ingrese la cantidad de Payasos: "))
Cant_Muñeca = float(input("Ingrese la cantidad de Muñecas: "))
Peso_Payaso = Cant_Payaso  *112
Peso_Muñeca = Cant_Muñeca  *112
Peso_Total = Peso_Payaso + Peso_Muñeca
print('----> El peso total del paquete que sera enviado sera de {:.3f}  gramos'.format(Peso_Total))