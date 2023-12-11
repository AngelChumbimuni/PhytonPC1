"""
En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
dejar como propina.

"""
Consumo = float(input("¿Cuánto consumiste?(En soles):"))
Porc_Propina_str = input("¿Qué porcentaje de propina quieres dar?:")
if Porc_Propina_str.endswith('%'):
    Porc_Propina = float(Porc_Propina_str.rstrip('%'))
    Monto_Propina = Consumo*Porc_Propina/100
else:
    Porc_Propina = float(Porc_Propina_str)
    Monto_Propina = Consumo * Porc_Propina
    
print("---> La propina que debes dar es de ", Monto_Propina,"soles")