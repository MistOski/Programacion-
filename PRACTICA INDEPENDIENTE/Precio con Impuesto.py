#Pide el precio de un producto y la tasa de IVA (porcentaje). Luego:
p = float(input("Ingrese el precio de un producto: "))
t = float(input("Ingrese la tasa de IVA (Sin usar %): "))

#Calcula el IVA (precio × tasa / 100).
pt = (p * t) / 100

#Muestra el precio final (precio + IVA).
pf = p + pt 

#Usa f-string para mostrar los resultados con 2 decimales.
print(f"El precio final es: {pf: .2f} CLP")