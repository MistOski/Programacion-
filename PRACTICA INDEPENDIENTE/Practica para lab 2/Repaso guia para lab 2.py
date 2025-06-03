#Crear un algoritmo que sirva de Conversor de Temperatura:

#Solicitar por consola una temperatura en grados Celsius (números flotantes)
c = float(input("Ingrese un numero y se le sera entregado en diferentes grados: "))

#Calcular su equivalente en grados Fahrenheit y Kelvin utilizando las fórmulas correspondientes.

# Farenheit (0 °C × 9/5) + 32 = 32 °F
f = (c * 9/5) + 32 

# Kelvin 0 °C + 273.15 
k = c + 273.15

# Mostrar los tres valores en pantalla, redondeados a 2 decimales.
print(f"El valor que ingresado es de {c: .2f} grados Celcius, equivalente a {f: .2f} grados Farenheit y a {k: .2f} grados Kelvin")



#Desarrollar un algoritmo con operaciones mixtas con números complejos:

#Ingresar tres valores numéricos diferentes (entero, flotante y complejo)
e = int(input("Ingrese un valor entero: "))
d = float(input("Ingrese un valor decimal: "))
c = complex(input("Ingrese un valor complejo: "))

#Calcular y mostrar:

#Potencia Compleja (Complejo y Entero)
pc = e ** c 

#Suma Mixta (Complejo y Flotante)
sm = c + d

#Producto Mixto (Complejo y Entero)
pm = c * e

#Módulo de Potencia Compleja. El módulo se realiza utilizando la función abs() (Variable Potencia Compleja, con 3 decimales)
mpc = abs(pc)
print(f"La potencia compleja es {pc}, la suma mixta {sm}, el producto mixto {pm} y el modulo de potencia compleja es {mpc: .3f}")



#Crear un algoritmo que permita manipular cadenas de texto:

#Ingresar una frase de máximo 30 caracteres.
f = input("Ingrese una frase de no mas de 30 caracteres, aquellos que excedan el limite no seran considerados: ")
f = f[:30]

#Generar dos nuevas variables: una en mayúsculas y otra en minúsculas.
min = f.lower()
may = f.upper()

#Utilizar un método propio para determinar cuántas veces aparece la letra «a» (tanto «a» como «A») en la frase, y muestra el total.
cmin = f.count("a")
cmay = f.count("A")
csum = cmin + cmay
print(f"La letra A aparece {csum} veces en la frase")

#Emplear otro método para imprimir la longitud de la frase original.
l = len(f)
print(f"La frase cuenta con {l} caracteres, los espacios son considerados")



#Desarrollar un programa de gestión de inventario:

#Ingresar el nombre de un producto y su precio unitario
p = input("Ingrese el nombre de un producto: ")
pu = float(input("Ingrese el precio unitario del producto: "))

#Ingresar la cantidad en stock.
s = int(input("Ingrese el stock del producto: "))

#Calcular el valor total de los productos ingresados y mostrarlo con 2 decimales.
vt = pu * s 

#Crear una variable booleana llamada umbral, que entregue un True si el valor_total > 100000 y False en caso contrario..
umbral = vt > 100000

#Imprimir el nombre del producto, la cantidad, el valor total y el estado umbral en un solo print() formateado.
print(format(f"Nombre del producto: {p}, stock del producto: {s}, valor total del producto: {vt: .2f}, umbral: {umbral}"))