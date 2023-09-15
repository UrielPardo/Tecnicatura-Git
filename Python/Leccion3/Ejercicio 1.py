'''
Pedir al usuario que ingrese un mes del año, el numer debe ser entre 1 y 12,
luego le decimos en que estacion del año esta
'''
estacion = None
mes = int(input("Digite un numero del mes, entre 1 y 12\n"))
if 1 <= mes <= 3:
    estacion = "Verano"
elif 4 <= mes <= 6:
    estacion = "Otoño"
elif 7 <= mes <= 9:
    estacion = "Invierno"
elif 10 <= mes <= 12:
    estacion = "Primavera"
else:
    estacion = "Error. No hay mes correspondiente para el dato ingresado"
print(f'Para el mes {mes}, la estacion correspondiente es {estacion}')