#Desarrollar un programa de gestión de inventario: 

#Ingresar el nombre de un producto y su precio unitario. 
n = input("Ingrese el nombre del producto: ")
pu = int(input("Ingrese el precio unitario del producto: "))

#Ingresar la cantidad en stock. 
cd = int(input("Ingrese la cantidad disponible del producto: "))

#Calcular el valor total de los productos ingresados y mostrarlo con 2 decimales. 
vt = cd * pu 

#Crear una variable booleana llamada umbral, que entregue un True si el valor_total > 100000 y False en caso contrario.. 
umbral = vt > 100000

#Imprimir el nombre del producto, la cantidad, el valor total y el estado umbral en un solo print() formateado. 
print(format(f"Nombre de producto: {n}, valor total: {vt} cantidad en el stock: {cd}, umbral: {umbral}"))