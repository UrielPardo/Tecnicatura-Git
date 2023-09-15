#Calcular el factorial de un numero mayor o igual a 0
num = int(input("Digite un numero\n"))
if (num >= 0):
    factorial = 1
    for i in range(1,num+1):
        factorial = factorial * i
print(f'El valor de factorial es {factorial}')