#Desarrollar un algoritmo con operaciones mixtas con números complejos:

#Ingresar tres valores numéricos diferentes (entero, flotante y complejo)
e = int(input("Ingresa un valor entero: "))
f = float(input("Ingresa un valor flotante: "))
c = complex(input("Ingresa un valor complejo: "))

#Calcular y mostrar: 

#Potencia Compleja (Complejo y Entero) 
pc = e ** c
print(pc)

#Suma Mixta (Complejo y Flotante)
sm = c + f
print(sm)

#Producto Mixto (Complejo y Entero) 
pm = c * e

#Módulo de Potencia Compleja. El módulo se realiza utilizando la función abs(), (Variable Potencia Compleja, con 3 decimales) 
