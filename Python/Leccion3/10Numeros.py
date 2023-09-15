positivos = 0
negativos = 0
neutros = 0
for i in range(0, 10):
    numero = int(input(f'Ingrese el {i+1}° numero: '))
    if numero < 0:
        negativos += 1
    elif (numero > 0):
        positivos += 1
    else:
        neutros += 1
print(f'Hay {positivos} numeros positivos')
print(f'Hay {negativos} numeros negativos')
print(f'Hay {neutros} numeros neutros')