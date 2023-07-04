'''
Ejercicio 3:
Intercambiar el valor de dos variables.
Por ejemplo:
a = 10        a = 5
b = 5              b = 10

'''
a = float(input("Digite el valor de la variable a\n"))
b = float(input("Digite el valor de la variable b\n"))
aux = a
a = b
b = aux
print(f'El nuevo valor de a: {a}, y el nuevo valor de b: {b}')