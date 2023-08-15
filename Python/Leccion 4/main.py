# lista = Ariel, Liliana, Natalia, Osvaldo
nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
"""
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])

#Recorrido de lista
print(nombres[0:2])#Solo muestra desde el primer indice, hasta el anterior del ultimo
print(nombres[ :3])#Desde el inicio hasta el indice indicado(Sin icluirlo)
print(nombres[1: ])#Desde el indice indicado hasta el final

#Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
#iterar una lista
for nombre in nombres: #nombre es singular, la lista es plurar
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')
"""
#Preguntamos cuantos elementos tiene una lista
print(len(nombres)) #le pasamos como parametro la lista

#Agregamos un elemento
nombres.append('Marcelo')
print(nombres)

#Insertamos un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

#Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

#Eliminamos el ultimo elemento
nombres.pop()
print(nombres)

#Eliminar un indice especifico
del nombres[2] #del significa delete (eliminar)
print(nombres)

#Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#Eliminar la lista
del nombres
#print(nombres)