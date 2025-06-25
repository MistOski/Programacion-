# 1. Una clínica veterinaria requiere registrar a los siguientes gatitos en su registro: 

# N° Ingreso Nombre Peso(Kg) Edad(Meses) Tamaño (cm) 
#    101     Luna   1.2      3           30 
#    102     Michi  0.8      2           25 
#    103     Pepito 2.5      5           35

# A) Crear un diccionario cuyas claves sean los números de ingreso y cuyos valores sean 
# sub-diccionarios con las claves: "Nombre", "Peso", "Edad" y "Tamaño". Luego imprimir el diccionario. (20 Pts)


Diccionario = {
    101 : {"Nombre" : "Luna", "Peso" : 1.2, "Edad" : 3, "Tamaño" : 30},
    102 : {"Nombre" : "Michi", "Peso" : 0.8, "Edad" : 2, "Tamaño" : 25},
    103 : {"Nombre" : "Pepito", "Peso" : 2.5, "Edad" : 5, "Tamaño" : 35}
}
print(Diccionario)
print("-" * 150) 

# B) Recorrer el diccionario principal con un bucle y, en cada sub-diccionario, añadir la clave 
# "Clasificación-Peso" según: (20 Pts) 
# ● < 1 kg → "Bajo Peso" 
# ● 1 ≤ peso ≤ 4 kg → "Normal" 
# ● > 4 kg → "Sobre Peso"
#for clave, valor in Diccionario.items():
Diccionario[101]["Clasificacion-Peso"] = ["Normal"]
Diccionario[102]["Clasificacion-Peso"] = ["Bajo-Peso"]
Diccionario[103]["Clasificacion-Peso"] = ["Normal"]

print(Diccionario)
print("-" * 150)
# C) Crear otro bucle para agregar la clave "Categoría-Etaria" basada en la edad:  (10 Pts) 
# ● < 4 meses → "Cachorro" 
# ● 4 ≤ edad ≤ 12 meses → "Joven" 
# ● > 12 meses → "Adulto"
Diccionario[101]["Categoria-Etaria"] = ["Cachorro"]
Diccionario[102]["Categoria-Etaria"] = ["Cachorro"]
Diccionario[103]["Categoria-Etaria"] = ["Joven"]
print(Diccionario)

# Dentro del bucle, utilizar un try/except para asignar "Desconocida" si ocurre un error al ingresar una edad no válida.

# D) Crear una lista de tuplas, donde el primer elemento de la tupla es el “N° de Ingreso”, y el 
# segundo valor es el “Peso”. Luego, ordenarla de menor a mayor peso, utilizando: (10 Pts) 
# ● Un método adecuado de Python para ordenar la estructura de datos. 
# ● Imprimir la lista ordenada

# E) Implementar un bucle que pida al usuario datos de nuevos gatitos, con todos los datos 
# de la tabla: “N° de Ingreso”, “Nombre”, “Peso”, “Edad”, y “Tamaño”. Después de cada 
# ingreso, preguntar “¿Desea agregar otro gatito? (s/n)”: (20 Pts) 
# ● Convertir los valores de ingreso al tipo correcto. 
# ● Agregar cada nuevo registro al diccionario gatitos (por asignación directa o usando .update().




# F) Pedir al usuario el número de ingreso de un gatito existente y el nuevo tamaño:  (5 Pts) 
# ● Buscar el sub-diccionario correspondiente (Utilizando un bucle o acceso directo). 
# ● Actualizar "Tamaño" con el método adecuado.






# G) Crear una lista con todos los valores de "Peso", y luego calcular e imprimir: 
# ● Promedio de pesos. 
# ● Máximo y mínimo de pesos. 
# ● Número de ingreso del gatito con más bajo peso. (15 Pts)
print("-" * 150)
listapesos = [1.2, 0.8, 2.5]
promedio = sum(listapesos) / 3
maximopeso = max(listapesos)
minimopeso = min(listapesos)
if minimopeso ==0.8:
    print("El numero de ingreso con el gato de peso minimo es 102")
elif minimopeso ==1.2:
    print("El numero de ingreso con el gato de peso minimo es 101")
else:
    print("El numero de ingreso con el gato de peso minimo es 103")

print(f"El promedio de peso entre los gatos es de {promedio}kg, el peso maximo alcanzado por los gatos es de {maximopeso}kg, el minimo es de {minimopeso}kg")
listapesos = [1.2, 0.8, 2.5]
promedio = sum(listapesos) / 3
maximopeso = max(listapesos)
minimopeso = min(listapesos)
if minimopeso ==0.8:
    print("El numero de ingreso con el gato de peso minimo es 102")
elif minimopeso ==1.2:
    print("El numero de ingreso con el gato de peso minimo es 101")
else:
    print("El numero de ingreso con el gato de peso minimo es 103")
# Finalmente, imprimir el diccionario completo, ordenado por número de ingreso, utilizando un método propio de Python.
print("-" * 150)
print(Diccionario)














