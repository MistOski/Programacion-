#Desarrollar un programa de gestión de inventario: 

#Ingresar el nombre de un producto y su precio unitario. 
p = input("Ingrese el producto: ")
pu = float(input("Ingrese el precio unitario del producto: "))

#Ingresar la cantidad en stock. 
s = int(input("Ingrese la cantidad disponible de ese producto: "))

#Calcular el valor total de los productos ingresados y mostrarlo con 2 decimales. 
t = pu * s 
tt = round(t, 2)
print(f"La ganancia total respecto al valor del producto y su cantidad disponible es {t:.2f} CLP")

#Crear una variable booleana llamada umbral, que entregue un True si el valor_total > 100000 y False en caso contrario.. 
umbral = t>100000
print(umbral)

#Imprimir el nombre del producto, la cantidad, el valor total y el estado umbral en un solo print() formateado. 
print(f"En resumen, el producto: {p} cuenta con un stock de {s}, el valor total del stock es de {tt} CLP y el estado del umbral es: {umbral}")