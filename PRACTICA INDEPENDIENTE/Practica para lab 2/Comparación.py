#Solicita dos edades y muestra:
pe = int(input("Ingresa la primera edad: "))
se = int(input("Ingresa la segunda edad: "))

#Si son iguales
i = pe == se

#Si una es mayor que la otra
pm = pe > se
sm = se > pe

#Si ambas edades son mayores de 18 (usa operadores lógicos)
p18 = pe >= 18
s18 = se >= 18

print(f"Las edades son iguales: {i} La primera edad es mayor a la segunda: {pm} La segunda edad es mayor a la primera: {sm} La primera edad es mayor de 18: {p18} La segunda edad es mayor de 18: {s18}")