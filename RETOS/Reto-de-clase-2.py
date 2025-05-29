#DICCIONARIO
inventario = dict(
    manzana = '500' ', 400' ', 600',
    platano = '300' ', 300' ', 250',
    cereza = '200' ', 140' ', 180'
)
tipos_frutas = ['manzana', 'platano', 'cereza']
precios_platano = 300 + 250 / 2
print(inventario)
print(tipos_frutas)
print(precios_platano)
print(f"Su promedio del precio del platano es: {precios_platano: .3f} CLP")