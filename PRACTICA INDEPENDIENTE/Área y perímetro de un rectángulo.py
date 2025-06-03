#Solicita el ancho y alto de un rectángulo (como números decimales).
an = float(input("Ingrese el ancho de un rectangulo: "))
al = float(input("Ingrese el alto de un rectangulo: "))

#Calcula

#Área (ancho * alto)
ar = an * al

#Perímetro (2 * (ancho + alto))
p = (2*(an + al))

#Muestra ambos resultados con 2 decimales, usando f-string.
print(f"El area de los caracteres ingresados en el rectangulo es de {ar} cm y el perimetro es de {p} cm.")