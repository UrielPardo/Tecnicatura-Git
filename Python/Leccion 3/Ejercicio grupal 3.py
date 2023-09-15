'''
Dadas las horas trabajadas de 5 personas y la tarifa de pago,
calcular el salario y la sumatoria de todos los salarios
'''
sumaSalario = 0
for i in range (0, 5):
    horas = int(input(f'Digite la cantidad de horas trabajadas de la {i+1}° persona\n'))
    tarifa = int(input(f'Digite la tarifa pagada por hora de la {i+1}° persona\n'))
    salario = horas * tarifa
    sumaSalario = sumaSalario+salario
    print(f'El salario de la {i+1}° persona es {salario}')
print(f'La sumatoria de salarios es {sumaSalario}')
