#Una tienda de productos tecnológicos maneja la siguiente información:

#Productos: Smartphone, Laptop, Tablet, Smartwatch
#Precios (USD): 300, 800, 150, 200
p = {
    "Smarthphone" : 300,
    "Laptop" : 800,
    "Tablet" : 150,
    "Smarthwatch" : 200
    }

#Stock disponible (unidades):
#Smartphone: 25
#Notebook: 12
#Tablet: 8
#Smartwatch: 4
s = {
    "Smarthphone" : 25,
    "Laptop" : 12,
    "Tablet" : 8,
    "Smarthwatch" : 4
}

#Se solicita desarrollar un algoritmo que:
#Imprima el nombre y precio del artículo más caro y del más barato, utilizando métodos de Python visto en clases.
pmax = max(p, key=p.get)
pmin = min(p, key=p.get)
print(f"El articulo con el precio maximo es {pmax} = {p[pmax]} y el articulo con el precio minimo es {pmin} = {p[pmin]}")

#Para cada artículo, muestre su categoría de precio según las siguientes condiciones:

#Producto Económico: 
# precio < 200
#Producto Estándar: 200 ≤ precio ≤ 500
#Producto Premium: precio > 500
for nombre, precio in p.items():
    if precio < 200:
        categoria = "Económico"
    elif precio <= 500:
        categoria = "Estándar"
    else:
        categoria = "Premium"
    print(f"{nombre}, {precio} = {categoria}")

#Liste los artículos con stock bajo (menos de 10 unidades)
for nombre, cantidad in s.items():
    if cantidad < 10:
        print(f"{nombre} : {cantidad} = unidades")
