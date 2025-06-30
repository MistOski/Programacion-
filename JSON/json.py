import json #Manipulacion de archivos json
import os #Metodos para trabajar en los json

ruta = os.path.join("json", "datos.json") #Ruta relativa

#Leer archivo json
with open(ruta, "r", encoding='utf=8') as archivo: #La r es de read
    datos = json.load(archivo)

#Mostrar los usuarios del archivo JSON
for usuario in datos:
    print(f"ID: {usuario['id'], Nombre: {usuario}['nombre']}, Edad: {usuario}['Edad]")

#Agregar a un usuario
nuevo_usuario = {
    "id" : 5,
    "nombre" : "Fernanda"
    "edad" : 30 
}

datos.append(nuevo_usuario)

#Guardar los cambios en el archivo JSON utilizando json.dump()

with open(ruta, "w" enconding= 'utf=8') as archivo:
    json.dump(
        datos,
        archivo
    )