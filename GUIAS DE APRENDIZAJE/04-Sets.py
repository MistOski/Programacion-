#CREANDO SETS
colores = {'Azul', 'Rojo', 'Azul', 'Verde'}

colors = {'Azul', 'Naranjo'}

#IMPRIMIENDO SET COLORES
print(colores)

#AGREGANDO UN NUEVO ELEMENTO AL SET
colores.add('Blanco')
print(colores)

#ELIMINANDO UN ELEMENTO DEL SET
colores.discard('Blanco')
print(colores)

#APLICANDO EL METODO DIFFERENCE 
diferencia = colores.difference(colors)
print(diferencia)