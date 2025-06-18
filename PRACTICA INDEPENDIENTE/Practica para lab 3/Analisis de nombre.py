# Solicita el nombre completo
n = input("Ingrese su nombre: ")

# Nombre en minúsculas y mayúsculas
nmin = n.lower()
nmay = n.upper()

# Cuenta total de caracteres y cantidad de veces que aparece la letra "e" o "E"
tl = len(n)
ce = nmin.count("e")

print(f"{n} en minusculas: {nmin} En mayusculas: {nmay} Cantidad de caracteres: {tl} Veces que aparece la E o e: {ce}")