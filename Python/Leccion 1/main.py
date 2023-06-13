'''
miVariable = 3
print(miVariable)
miVariable = "Hola a todos los alumnos de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x+y
print(z)
# Las literales se escriben x576, son las 3 ultimas del valor de id
print(id(x))
print(id(y))
print(id(z))
# Tipos de datos
x = 14.5
print(x)
print(type(x))
x = "Hola Alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))
# Manejo de Cadenas (Strnigs)
miGrupoFavorito = "Imagine Dragons"
caracteristicas = "Radioactive"
print("Mi grupo favorito es: ", miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print(int(numero1)+int(numero2))

# Boleanos
miBoleano = 1<2
print(miBoleano)

if miBoleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar entrada de datos del usuario
# funcion input
resultado = input("Digite un numero: ")
print(resultado)

# Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero "))
numero2 = int(input("Escribe el segundo numero "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
'''
operandoA = 8
operandoB = 5

suma = operandoA + operandoB
# print("El resultado de la suma es:", suma)
print(f'El resultado de la suma es: {suma}')

resta = operandoA - operandoB
print(f'El resultado de la resta es: {resta}')

multiplicacion = operandoA * operandoB
print(f'El resultado de la multiplicacion es: {multiplicacion}')

division = operandoA // operandoB
print(f'El resultado de la division(entera) es: {division}')

division = operandoA / operandoB
print(f'El resultado de la division es: {division}')

modulo = operandoA % operandoB
print(f'El modulo de la operacion es: {modulo}')

potenciacion = operandoA ** operandoB
print(f'El resultado de la potenciacion es: {potenciacion}')