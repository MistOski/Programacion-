#Pide al usuario los siguientes datos:

#Nombre
n = input("Ingrese su nombre: ")

#Edad
e = int(input("Ingrese su edad: "))

#Año actual
a = int(input("Ingrese el año actual: "))

#Muestra una frase con el siguiente formato: 

#"Hola, me llamo {nombre}, tengo {edad} años y en el año {año + 10} tendré {edad + 10} años."
ad = a + 10
ed = e + 10
print(f"Hola mi nombre es {n}, tengo {e} años y en el año {ad} tendre {ed} años.")