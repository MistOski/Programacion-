#Operaciones con Tipos Mixtos

#Solicita los siguientes datos:

#Un número entero.
e = int(input("Ingresa un numero entero: "))

#Un número decimal.
d = float(input("Ingresa un numero decimal: "))

#Un número complejo (ej. 2+5j).
c = complex(input("Ingresa un numero complejo: "))

#Calcula y muestra:

#La suma del entero y el decimal.
s = d + e

#La resta del número complejo menos el decimal.
r = c - d

#El producto del entero por el número complejo.
p = e * c

#Imprime los 3 resultados.
print(f"La suma del entero y decimal es de: {s}, la resta del numero complejo menos el decimal es: {r} y el producto del entero por el complejo es: {p}")