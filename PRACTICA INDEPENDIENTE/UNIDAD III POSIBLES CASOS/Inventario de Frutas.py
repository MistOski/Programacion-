#Objetivo: Aplicar estructuras de datos y funciones como set(), sum(), len().
#Crear un inventario de frutas donde:
#Cada fruta tiene una tupla con 3 precios.
#Obtener los precios únicos de la fruta “Plátano”.
#Calcular el promedio de los precios únicos del plátano.
#Mostrar la lista de frutas disponibles.
inventario = {
    "Manzana": (1000, 1100, 1050),
    "Plátano": (500, 500, 600),
    "Cereza": (2000, 2100, 2050)
}

# Paso 2: Obtener precios únicos
precios_platano = set(inventario["Plátano"])

# Paso 3: Calcular promedio
promedio = sum(precios_platano) / len(precios_platano)

# Paso 4: Listar frutas
tipos_frutas = list(inventario.keys())

print("Inventario completo:", inventario)
print("Precios únicos de Plátano:", precios_platano)
print("Promedio precios plátano:", round(promedio, 2))
print("Frutas disponibles:", tipos_frutas)

# Evalúa uso de diccionarios, sets, tuplas, listas, funciones y formateo.