#Solicita:

#El monto total del crédito.
mc = float(input("Ingrese el monto total de credito: "))

#El número de cuotas (entero).
nc = int(input("Ingrese la cantidad de cuotas: "))

#Calcula

#El valor de cada cuota (división).
vc = mc / nc

#El valor total pagado si se aplica un interés de 1.5% sobre el total.
i = mc * 0.015
mi = mc + i

#Muestra:

#Cuota mensual redondeada a 2 decimales.
print(f"La cuota mensual es de {vc: .2f} CLP")

#Total a pagar con interés (también redondeado).
print(f"El total a pagar con los intereses es de {mi: .2f} CLP")