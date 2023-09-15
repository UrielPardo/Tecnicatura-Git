'''
Hagamos un programa que cuando el usuario ingrese su edad le diga, o imprima la etapa de su vida
en una pequeña oracion
'''
edad = int(input("Digite su edad\n"))
mensaje = None
if 0<edad<10:
    mensaje = "La infancia es increible y bella"
elif 10 <= edad <20:
    mensaje = "Tienes muchos cambios, mucho que estudiar"
elif 20 <= edad <30:
    mensaje = "Amor  y comienza el trabajo"
else:
    mensaje = "Error. Etapa de vida no reconocida"
print(f'Tu edad es {edad}, {mensaje}')
