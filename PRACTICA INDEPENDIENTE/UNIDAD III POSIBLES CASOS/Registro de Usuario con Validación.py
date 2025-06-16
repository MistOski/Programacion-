#Crear un programa que pida el nombre y la edad de un usuario. Si tiene menos de 18 años, mostrar que es menor de edad. 
#Si tiene entre 18 y 64 años, mostrar que es adulto. Si tiene 65 o más, mostrar que es adulto mayor. 
# Además, indicar cuántos años le faltan para cumplir 100 años.
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

if edad < 18:
    categoria = "Menor de edad"
elif edad < 65:
    categoria = "Adulto"
else:
    categoria = "Adulto mayor"

faltan = 100 - edad

print(f"Hola {nombre}, eres {categoria}. Te faltan {faltan} años para cumplir 100.")

# Se usan condicionales elif, entrada por teclado y operaciones matemáticas.
# Evalúa input, cast de tipos y lógica con condiciones.