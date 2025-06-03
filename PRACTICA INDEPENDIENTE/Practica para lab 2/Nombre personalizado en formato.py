#Solicita un nombre completo.
n = input("Ingrese su nombre completo: ")

#Crea una variable con el nombre todo en minúsculas.
nmin = n.lower()

#Crea otra con el nombre todo en mayúsculas.
nmay = n.upper()

#Crea un string que diga: "Mi nombre tiene {n} letras y contiene la letra 'a' {x} veces"
cl = len(n)
cmin = n.count("a")
cmay = n.count("A")
ct = cmin + cmay

print(f"Mi nombre tiene {cl} caracteres (Los espacios se toman en cuenta) y contiene la letra A {ct} veces.")