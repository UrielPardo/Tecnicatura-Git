i = 0
baja = 10
total = 0
while (i < 10):
    calificacion = int(input(f'Digite la {i+1}° calificacion: '))
    if (0 <= calificacion <=10):
        if(calificacion < baja):
            baja = calificacion
        total += calificacion
        i+=1
    else:
        print("Calificacion fuera de rango\n")
print(f'El promedio de las calificaciones es {total/10}, y la nota mas baja es {baja}')
