#Ciclo while
'''
contador = 5

while contador <20 :
    print(f'Repeticion del ciclo N° {contador+1}')
    contador += 1

maximo = 5
while contador <= maximo:
    print("Se ejecuta el ciclo while")
    contador += 1

minimo = 0
while contador >= minimo:
    print(f'Faltan {contador} repeticiones')
    contador -= 1

#Ciclo for
cadena = "Hello world"
for letra in cadena:
    print(letra)
else:
    print("Se cerró el ciclo for")

#Palabra reservada break
for letra in "Alemania":
    if letra == 'a':
        print(f'La letra encontrada es {letra}')
        break
else:
    print("Cierre del ciclo for")
'''
#Palabra reservada continue
for i in range(6):
    if i % 2 == 0:
        print(f'Valor: {i}')
for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')