#Desarrollar un algoritmo con operaciones mixtas con números complejos:

#Ingresar tres valores numéricos diferentes (entero, flotante y complejo)
e = int(input("Ingrese un numero entero: "))
f = float(input("Ingrese un numero (puede usar decimales): "))
c = complex(input("Ingrese un numero complejo: "))

#Calcular y mostrar: 

#Potencia Compleja (Complejo y Entero) 
pc = e ** c 
print(f"La potencia del numero complejo: {c} y el numero entero: {e} es: {pc}")

#Suma Mixta (Complejo y Flotante)
sm = c + f 
print(f"La suma entre el numero complejo: {c} y el numero flotante {f} es de: {sm}")

#Producto Mixto (Complejo y Entero) 
pm = c * e
print(f"El producto entre el numero complejo {c} y el numero entero {e} es de: {pm}")

#Módulo de Potencia Compleja. El módulo se realiza utilizando la función abs(), (Variable Potencia Compleja, con 3 decimales) 
mpc= abs(pc)
print(f"El modulo de potencia compleja es de: {mpc: .3f}")