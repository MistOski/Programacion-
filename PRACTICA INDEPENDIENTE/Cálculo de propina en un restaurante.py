#Pide el valor de una cuenta (float) y el porcentaje de propina (float).
vc = float(input("Ingresa el valor de la cuenta: "))
pp = float(input("Ingresa el porcentaje de propina: "))

#Calcula:

#Monto de la propina
mp = (vc * pp) / 100

#Total a pagar (cuenta + propina)
tp = vc + mp 

#Muestra ambos valores con 2 decimales.
print(f"El monto total es de {vc: .2f} CLP y el monto total con la propina es de {tp: .2f} CLP")