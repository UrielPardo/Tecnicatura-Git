"""
#Operador and
a = False
b = False
resultado = a and b
print(resultado)

#Operador or
resultado = a or b
print(resultado)

#Operador not
resultado = not a
print(resultado)

#Ejercicio: Valor dentro de un rango
valor = int(input("Digite un numero entre 0 y 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = valor >= valorMinimo and valor <=valorMaximo
if dentroRango:
    print(f'El valor {valor} esta dentro del rango')
else:
    print(f'El valor {valor} no esta dentro del rango')

#Ejercicio con el operador or, Operador not
vacaciones = True
diaDescanso = False
if not (vacaciones or diaDescanso):
    print("Tiene trabajo que hacer")
else:
    print("Puede asistir al juego")

#Ejercicio: Rango entre edades 20 y 30 años
edad = int(input("Digite su edad: "))
#veinte = edad >= 20 and edad < 30
#print(veinte)
#treinta = edad >=30 and edad <40
#print(treinta)
#if veinte or treinta:
#    if veinte:
#       print("Estas dentro del rango de los (20'0) años")
#    elif treinta:
#       print("Estas dentro del rango de los (30'0) años")
#else:
#    print('No estas dentro del rango entre los (20\'0) a los (30\'0) años')
#if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
#    print("Estas dentro del rango de los (20'0) a (30'0) años")
#else:
#    print('No estas dentro del rango entre los (20\'0) a los (30\'0) años')
#Sintaxis simpificada del operador and
if (20 <= edad <30) or (30<= edad < 40):
    print('Estas dentro del rango entre los (20\'0) a los (30\'0) años')
else:
    print('No estas dentro del rango entre los (20\'0) a los (30\'0) años')

#Ejercicio: El mayor de dos numeros
num1 = input("Digite el primer numero: ")
num2 = input("Digite el segundo numero: ")
if (num1> num2):
    print('El numero 1 es mayor')
else:
    print('El numero 2 es mayor')
"""
#Ejercicio: Tienda de libros
print('Digite los siguientes datos del libro: ')
nombre = input('Digite el nombre del libro: ')
id = int(input('Digite el ID del libro: '))
precio = float(input('Digite el precio del libro: '))
envioGratuito = input('Indique si el envio es gratuito: (True/False): ')
if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    print('El valor es incorecto, debe ingresar True/False')
print(f'''
    Nombre: {nombre}
    Id: {id}
    Precio: ${precio}
    Envio gratuito: {envioGratuito}
''')