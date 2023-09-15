'''
INgresar N enteros, visualizar la suma de los numeros pares de la lista, cuantos numeros pares
existen y cual es el promedio de los numeros impares
'''
enteros = int(input("Digite la cantidad de enteros\n"))
impares = 0
pares = 0
contadorPar = 0
contadorImpar = 0
for i in range(0, enteros):
    numero = int(input(f'Digite el {i+1}° numero\n'))
    if (numero % 2 == 0):
        pares = pares + numero
        contadorPar += 1
    else:
        impares = impares + numero
        contadorImpar += 1
print(f'La cantidad de numeros pares es {contadorPar}, su suma es {pares}, y el promedio de los impares es {impares/contadorImpar}')