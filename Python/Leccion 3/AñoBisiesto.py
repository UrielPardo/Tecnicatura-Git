opcion = 0
while (opcion != 1):
    anio = int(input("Digite un año\n"))
    if ((anio % 4 == 0) and (anio % 100 != 0) or (anio % 400 == 0)):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
    opcion = int(input("Para salir digite 1\n"))
