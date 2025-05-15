#Guia Pythom de variables - Ulagos 2025

#PRIMERA PRUEBA
print("Hola mundo") #Sublime

#DECLARACION DE VARIABLES
nombre = "Ignacio"
apellido = "Millapani" 

#IMPRESION DE VARIABLE
print(nombre)

#UTILIZANDO MAS DE UNA VARIABLE EN UN PRINT
print("Mi nombre es", nombre, "y mi apellido es ", apellido)

#IMPRIMIENDO CON OPERADOR DE CONCATENACION
print("Hola mi nombre es " + nombre + " y mi apellido es " + apellido)

#IMPRIMIENDO CON F-STRINGS (CADENAS LITERALES)
print(f"hola mi nombre es {nombre} y mi apellido es {apellido}") #La "f" permite llamar a las variables dentro de {} sin tener que cerrar comillas

#INICIALIZANDO MULTI VARIABLES EN UNA SOLA LINEA (NO RECOMENDADO)
ciudad, region, pais = "Castro", "Los Lagos", "Chile"
print(f"hola soy de {ciudad}, {region}, {pais}")

peso = 75
edad = 31

#USO DEL INPUT / MUTABILIDAD 
print(nombre)
nombre = input("Ingrese su nombre:\n")  #La "\n" al final permite realizar un salto de linea para que no ingreses tu nombre al lado del texto
print(f"Hola mi nombre es: {nombre}")
print(nombre)