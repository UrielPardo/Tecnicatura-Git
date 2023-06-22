'''Ejercicio1
Ejercicio 1:
Escribir la siguiente expresión en forma de expresión algorítmica.
a3 x (b2 – 2ac)/2b
Pedimos al usuario 3 valores = a, b, c
Mostramos el resultado final
'''
a = float(input("Digite el valor de la variable a\n"))
b = float(input("Digite el valor de la variable b\n"))
c = float(input("Digite el valor de la variable c\n"))
resultado = (a**3 * b**2 - 2*a*c)/(2*b)
print(f'El resultado de la operacion es {resultado}')