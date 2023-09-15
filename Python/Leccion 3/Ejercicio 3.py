'''
El objetivo del programa sera crea un sistema de calificaciones de la siguiente manera:
Le pedimos al usuario que ingrese un valor del 0 al 10.
Luego si ingreso 9 o 10 imprimimos A
Entre 8 y menor a 9 imprimimos B
Entre 7 y menor a 8 imprimimos C
Entre 6 y menor a 7 imprimimos D
Entre 0 y menor a 6 imprimimos F
De lo contrario El valor ingresado es incorrecto
'''
valor = float(input("Digite un valor entre 0 y 10\n"))
mensaje = None
if 0<= valor <6:
    mensaje = 'F'
elif 6<= valor <7:
    mensaje = 'D'
elif 7<= valor < 8:
    mensaje = 'C'
elif 8<= valor <9:
    mensaje = 'B'
elif 9<= valor <= 10:
    mensaje ='A'
else:
    mensaje = "El valor ingresado es incorrecto"
print(f'La calificacion correspondiente es {mensaje}')