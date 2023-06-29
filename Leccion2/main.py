#Veremos la sentencia if/else
'''condicion = 'Hola alumnos'
if condicion == True:
    print("Condicion verdadera")
elif condicion == False:
    print("Condicion falsa")
else:
    print("Condcion sin especificar")
'''
'''
#Ejercicio conversion de numero a texto
num = int(input("Digite un numero del 1 al 3\n"))
numTexto = ''
if num == 1:
    numTexto = "Numero uno"
elif num == 2:
    numTexto = "Numero dos"
elif num == 3:
    numTexto = "Numero tres"
else:
    print("Has ingresado un valor fuera de rango")
print(f'El numero ingresado es {num} - {numTexto}')
'''
#Operacion ternaria
condicion = False
# if condicion:
#     print("Condicion Verdadera")
# else:
#     print("Condicion Falsa")
print("Condicion Verdadera") if condicion else print("Condcion Falsa")